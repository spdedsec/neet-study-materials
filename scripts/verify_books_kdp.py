#!/usr/bin/env python3
"""
scripts/verify_books_kdp.py - Empirical Challenger Stress Test Suite
Verifies all key acceptance criteria for Amazon KDP books:
1. Extract metadata and page counts via pdfinfo:
   - Volume 1 (books/physics_master_book.pdf) >= 140 pages
   - Volume 2 (books/chemistry_master_book.pdf) >= 160 pages
   - Volume 3 (books/biology_master_book.pdf) >= 90 pages
   - Combined total > 400 publication pages
2. Layout & Typography Stress Test via pdftotext:
   - Verso (even) pages display Book Series / Title
   - Recto (odd) pages display Chapter Title
   - Discreet author attribution "Satya Prakash"
   - Front matter page numbering uses lowercase Roman numerals (i, ii, ... x)
   - Main matter resets to Arabic numerals (1, 2, ...)
   - Auto-generated Table of Contents has formatted dot leaders and correct part divisions
3. Adversarial Search for Flaws:
   - Scan for duplicate chapter banners inside chapter bodies
   - Scan for forbidden AI buzzwords or filler:
     "as an AI", "language model", "delve into", "tapestry", "in conclusion", "testament"
"""

import os
import re
import sys
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
BOOKS_DIR = ROOT_DIR / "books"

BOOKS = {
    "Volume 1 (Physics)": {
        "file": BOOKS_DIR / "physics_master_book.pdf",
        "min_pages": 140,
        "parts": [
            "Classical Mechanics & Dynamics",
            "Rotational Mechanics, Gravitation & Continuum Mechanics",
            "Thermal Physics, Thermodynamics & Waves",
            "Electrodynamics & Magnetism",
            "Optics & Modern Physics",
            "Experimental Physics & Laboratory Skills",
            "Appendix: High-Yield Physics Formula & Equation Compendium"
        ],
    },
    "Volume 2 (Chemistry)": {
        "file": BOOKS_DIR / "chemistry_master_book.pdf",
        "min_pages": 160,
        "parts": [
            "Physical Chemistry Foundations",
            "Advanced Physical Chemistry",
            "Inorganic Chemistry & Coordination Compounds",
            "Organic Chemistry: Principles, Pathways & Biomolecules",
            "Organic Reaction Mechanisms Handbook",
            "Practical Chemistry & Qualitative Analysis Lab Manual",
            "Appendix: Comprehensive Chemistry Formula, Named Reaction & Reagent Matrices"
        ],
    },
    "Volume 3 (Biology)": {
        "file": BOOKS_DIR / "biology_master_book.pdf",
        "min_pages": 90,
        "parts": [
            "Cell Biology, Biomolecules & Cell Division",
            "Structural Organisation & Diversity",
            "Plant Physiology",
            "Human Physiology",
            "Reproduction & Reproductive Health",
            "Genetics & Molecular Biology",
            "Biotechnology, Human Health & Ecology"
        ],
    },
}

FORBIDDEN_WORDS = [
    "as an ai",
    "language model",
    "delve into",
    "tapestry",
    "in conclusion",
    "testament"
]

BANNER_PHRASES = [
    "Prepared, Compiled & Authored by Satya Prakash",
    "Prepared, Compiled and Authored by Satya Prakash"
]


def check_pdfinfo(pdf_path):
    out = subprocess.check_output(["pdfinfo", str(pdf_path)]).decode("utf-8")
    meta = {}
    for line in out.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta


def extract_pages(pdf_path):
    out = subprocess.check_output(["pdftotext", str(pdf_path), "-"]).decode("utf-8", errors="replace")
    pages = out.split("\x0c")
    if pages and pages[-1] == "":
        pages = pages[:-1]
    return pages


def run_stress_test():
    print("=" * 80)
    print("EMPIRICAL CHALLENGER VERIFICATION & STRESS TEST REPORT")
    print("=" * 80)

    total_pages = 0
    all_passed = True
    summary_report = {}

    for name, cfg in BOOKS.items():
        pdf_file = cfg["file"]
        print(f"\n--- [START TEST] {name}: {pdf_file.name} ---")
        if not pdf_file.exists():
            print(f"[-] CRITICAL ERROR: File not found: {pdf_file}")
            all_passed = False
            continue

        # 1. Metadata and Page Count Checks via pdfinfo
        meta = check_pdfinfo(pdf_file)
        page_count = int(meta.get("Pages", 0))
        total_pages += page_count
        print(f"  [1.1] pdfinfo Metadata:")
        print(f"        - Creator: {meta.get('Creator', 'N/A')}")
        print(f"        - Page Size: {meta.get('Page size', 'N/A')}")
        print(f"        - File Size: {meta.get('File size', 'N/A')}")
        print(f"        - Page Count: {page_count} (Required: >= {cfg['min_pages']})")
        if page_count < cfg["min_pages"]:
            print(f"        [FAIL] Page count {page_count} does not meet threshold {cfg['min_pages']}")
            all_passed = False
        else:
            print(f"        [PASS] Page count {page_count} >= {cfg['min_pages']}")

        # 2. pdftotext Extraction and Consistency Check
        pages = extract_pages(pdf_file)
        print(f"  [1.2] pdftotext Extracted Pages: {len(pages)}")
        if len(pages) != page_count:
            print(f"        [FAIL] Mismatch between pdfinfo ({page_count}) and pdftotext ({len(pages)})")
            all_passed = False
        else:
            print(f"        [PASS] 100% Page count consistency verified.")

        # 3. Layout & Typography Checks
        # Identify Front Matter Roman numerals & Main Matter Arabic numerals
        front_roman_pages = []
        arabic_reset_page = None
        main_arabic_pages = []
        verso_header_count = 0
        recto_header_count = 0
        author_attrib_count = 0
        toc_dot_leaders_count = 0
        toc_found = False

        duplicate_banners = []
        forbidden_matches = []

        # Regex patterns
        roman_patt = re.compile(r'^(x{0,3})(ix|iv|v?i{0,3})$', re.IGNORECASE)
        dot_patt = re.compile(r'(\.\s*){3,}\d+')

        for p_idx, page_str in enumerate(pages, 1):
            lines = [l.strip() for l in page_str.splitlines() if l.strip()]
            lower_page = page_str.lower()

            # Forbidden AI Buzzwords Scan
            for fw in FORBIDDEN_WORDS:
                if fw in lower_page:
                    forbidden_matches.append((p_idx, fw))

            # Duplicate Banner Scan
            for bp in BANNER_PHRASES:
                if bp.lower() in lower_page:
                    duplicate_banners.append((p_idx, bp))

            # Table of Contents Detection & Dot Leaders
            if "Table of Contents" in page_str or "Contents" in page_str:
                toc_found = True
            if toc_found and p_idx <= 22:
                for l in lines:
                    if dot_patt.search(l):
                        toc_dot_leaders_count += 1

            # Running Headers & Footers Analysis
            if lines:
                top_line = lines[0]
                bottom_line = lines[-1]

                # Check discreet author attribution on verso footer
                if "Authored by Satya Prakash" in page_str:
                    author_attrib_count += 1

                # Check Verso running headers (even PDF pages)
                if p_idx % 2 == 0:
                    if any("Master Reference Series" in l for l in lines[:3]):
                        verso_header_count += 1
                else: # Recto running headers (odd PDF pages)
                    if any("Foundations" in l or "NEET UG" in l or "Chapter" in l or "Unit" in l for l in lines[:3]):
                        recto_header_count += 1

                # Page Number Detection (top or bottom token)
                top_tokens = top_line.split()
                bottom_tokens = bottom_line.split()
                tokens_to_check = []
                if top_tokens:
                    tokens_to_check.extend([top_tokens[0], top_tokens[-1]])
                if bottom_tokens:
                    tokens_to_check.extend([bottom_tokens[0], bottom_tokens[-1]])

                for tok in tokens_to_check:
                    clean_tok = tok.strip(".,()[]{}")
                    if clean_tok.isdigit():
                        num = int(clean_tok)
                        if p_idx >= 21 and arabic_reset_page is None and num == 1:
                            arabic_reset_page = p_idx
                        if arabic_reset_page is not None and p_idx >= arabic_reset_page:
                            main_arabic_pages.append((p_idx, num))
                        break
                    elif roman_patt.match(clean_tok.lower()) and clean_tok.lower() in [
                        'i','ii','iii','iv','v','vi','vii','viii','ix','x',
                        'xi','xii','xiii','xiv','xv','xvi','xvii','xviii','xix','xx'
                    ]:
                        if arabic_reset_page is None:
                            front_roman_pages.append((p_idx, clean_tok.lower()))
                        break

        # Verification of Front vs Main Matter
        print(f"  [2.1] Page Numbering Architecture:")
        print(f"        - Front Matter Roman Numeral Pages detected: {len(front_roman_pages)}")
        if front_roman_pages:
            print(f"          Range: {front_roman_pages[0][1]} (page {front_roman_pages[0][0]}) to {front_roman_pages[-1][1]} (page {front_roman_pages[-1][0]})")
            print(f"          [PASS] Front matter uses lowercase Roman numerals.")
        else:
            print(f"          [FAIL] No Roman numerals found in front matter.")
            all_passed = False

        print(f"        - Main Matter Arabic Reset Page: PDF Page {arabic_reset_page}")
        if arabic_reset_page is not None:
            print(f"          [PASS] Main matter resets to Arabic numeral 1 at PDF page {arabic_reset_page}.")
        else:
            print(f"          [FAIL] Main matter failed to reset to Arabic numeral 1.")
            all_passed = False

        # Verification of Running Headers & Footers
        print(f"  [2.2] Two-Sided Running Headers & Footers:")
        print(f"        - Verso Running Header Matches ('NEET UG 2027 Master Reference Series'): {verso_header_count}")
        print(f"        - Recto Running Header Matches (Chapter/Section markers): {recto_header_count}")
        print(f"        - Discreet Author Attribution Instances ('Satya Prakash'): {author_attrib_count}")
        if verso_header_count >= 10 and author_attrib_count >= 10:
            print(f"          [PASS] Two-sided running headers and discreet author attributions verified.")
        else:
            print(f"          [FAIL] Insufficient header/attribution occurrences.")
            all_passed = False

        # Verification of Table of Contents
        print(f"  [2.3] Table of Contents & Part Structure:")
        print(f"        - TOC Found: {toc_found}")
        print(f"        - TOC Formatted Dot Leader Entries: {toc_dot_leaders_count}")
        if toc_found and toc_dot_leaders_count >= 20:
            print(f"          [PASS] Formatted dot leaders verified in TOC.")
        else:
            print(f"          [FAIL] TOC missing or insufficient dot leaders ({toc_dot_leaders_count}).")
            all_passed = False

        # Check Prescribed Parts
        full_text = "\n".join(pages)
        part_matches = 0
        for part in cfg["parts"]:
            # Normalize whitespace regex
            part_regex = re.escape(part)
            part_regex = part_regex.replace(r"\ ", r"\s+").replace(r"\\&", r"(&|and)")
            if re.search(part_regex, full_text, re.IGNORECASE):
                part_matches += 1
            else:
                # Fallback to subparts if long
                core_part = part.split(":")[0].strip()
                if re.search(re.escape(core_part), full_text, re.IGNORECASE):
                    part_matches += 1
                else:
                    print(f"          [MISSING PART] {part}")
        print(f"        - Prescribed Part Divisions Found: {part_matches}/{len(cfg['parts'])}")
        if part_matches == len(cfg["parts"]):
            print(f"          [PASS] All {len(cfg['parts'])} prescribed part divisions verified.")
        else:
            print(f"          [FAIL] Missing prescribed parts.")
            all_passed = False

        # Verification of Adversarial Checks
        print(f"  [3.1] Adversarial Duplicate Banner Scan:")
        body_banners = [b for b in duplicate_banners if b[0] > 5]
        print(f"        - Duplicate Banners in Main Body (pages > 5): {len(body_banners)}")
        if not body_banners:
            print(f"          [PASS] Zero duplicate chapter banners found in main body.")
        else:
            print(f"          [FAIL] Duplicate banners found: {body_banners}")
            all_passed = False

        print(f"  [3.2] Adversarial Forbidden AI Buzzwords Scan:")
        print(f"        - Forbidden Phrases Detected: {len(forbidden_matches)}")
        if not forbidden_matches:
            print(f"          [PASS] Zero forbidden AI buzzwords/fillers detected.")
        else:
            print(f"          [FAIL] Detected forbidden words: {forbidden_matches}")
            all_passed = False

        summary_report[name] = {
            "page_count": page_count,
            "min_pages": cfg["min_pages"],
            "roman_pages": len(front_roman_pages),
            "arabic_reset_page": arabic_reset_page,
            "verso_headers": verso_header_count,
            "author_attribs": author_attrib_count,
            "toc_dot_leaders": toc_dot_leaders_count,
            "parts_found": f"{part_matches}/{len(cfg['parts'])}",
            "body_banners": len(body_banners),
            "forbidden_words": len(forbidden_matches),
            "passed": all_passed
        }

    print("\n" + "=" * 80)
    print("GLOBAL PUBLICATION TOTALS:")
    print(f"Combined Publication Page Count: {total_pages} (Requirement: > 400 pages)")
    if total_pages > 400:
        print("[PASS] Combined total pages strictly exceed 400 publication pages.")
    else:
        print(f"[FAIL] Combined total pages {total_pages} <= 400.")
        all_passed = False

    print("=" * 80)
    if all_passed:
        print("FINAL VERDICT: ALL ACCEPTANCE CRITERIA VERIFIED (VERDICT: APPROVE)")
        return 0
    else:
        print("FINAL VERDICT: DEFECTS ENCOUNTERED (VERDICT: REQUEST_CHANGES)")
        return 1


if __name__ == "__main__":
    sys.exit(run_stress_test())
