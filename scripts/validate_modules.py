#!/usr/bin/env python3
"""
scripts/validate_modules.py - Comprehensive E2E Test Runner & Module Validator
Strictly calibrated for NEET UG 2027 Master Chapter Theory Modules.

Executes 7 distinct verification gates:
  - Check 1: Syntax & Environment Stack Validation
  - Check 2: Non-comment Curly Brace Matching
  - Check 3: Front Banner Attribution ('Prepared, Compiled \\& Authored by Satya Prakash')
  - Check 4: Running Header Attribution ('Satya Prakash' top-right header)
  - Check 5: Semantic Callout Presence (conceptbox, formulabox, usecasebox, trapbox, ncertbox)
  - Check 6: Deleted Syllabus Exclusion Scanner (strictly zero positive formulations outside trapbox)
  - Check 7: Tectonic Compilation & PDF generation verification
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple


@dataclass
class CheckResult:
    check_id: int
    name: str
    passed: bool
    message: str
    details: List[str] = field(default_factory=list)


@dataclass
class ModuleReport:
    filepath: str
    all_passed: bool
    checks: List[CheckResult] = field(default_factory=list)

    def summary_dict(self) -> Dict:
        return {
            "filepath": self.filepath,
            "all_passed": self.all_passed,
            "checks": [asdict(c) for c in self.checks],
        }


# =========================================================================
# DELETED NMC SYLLABUS TOPIC RULES (Strict Zero-Tolerance Scanner)
# =========================================================================
DELETED_NMC_PATTERNS = [
    # --- PHYSICS DELETED TOPICS ---
    (
        "Carnot Engine / Cycle / Refrigerator",
        re.compile(r"\bcarnot(\'s)?\b", re.IGNORECASE),
        "Physics: Carnot engine, cycle, and refrigerator are deleted from NEET UG 2027 NMC syllabus.",
    ),
    (
        "Doppler Effect",
        re.compile(r"\bdoppler(\'s)?(\s+effect|\s+shift)?\b", re.IGNORECASE),
        "Physics: Doppler effect in sound/waves is deleted from NEET UG 2027 NMC syllabus.",
    ),
    (
        "Potentiometer",
        re.compile(r"\bpotentiometer(s)?\b", re.IGNORECASE),
        "Physics: Potentiometer principle and applications are deleted from NEET UG 2027 NMC syllabus.",
    ),
    (
        "Cyclotron",
        re.compile(r"\bcyclotron(s)?\b", re.IGNORECASE),
        "Physics: Cyclotron is deleted from NEET UG 2027 NMC syllabus.",
    ),
    (
        "Transistors / BJT",
        re.compile(
            r"\b(transistors?|bjt|npn\s+transistor|pnp\s+transistor|transistor\s+as\s+an\s+amplifier)\b",
            re.IGNORECASE,
        ),
        "Physics: Transistors (bipolar junction transistors, logic gates with transistors) are deleted.",
    ),
    (
        "Radioactivity / Radioactive Decay",
        re.compile(
            r"\b(radioactiv(e|ity)|(?:alpha|beta|gamma)\s+decay|decay\s+constant\s+of\s+radio|radionuclides?|law\s+of\s+radioactive\s+decay)\b",
            re.IGNORECASE,
        ),
        "Physics: Radioactivity (alpha, beta, gamma decay, decay law) is deleted from NEET UG 2027 NMC syllabus.",
    ),
    (
        "Van de Graaff Generator",
        re.compile(r"\bvan\s*de\s*graaff\b", re.IGNORECASE),
        "Physics: Van de Graaff generator is deleted from NEET UG 2027 NMC syllabus.",
    ),
    (
        "Earth's Magnetic Elements",
        re.compile(
            r"\b(earth(\'s)?\s+magnetic\s+elements?|magnetic\s+(?:declination|inclination|dip)|horizontal\s+component\s+of\s+earth(\'s)?\s+magnetic\s+field)\b",
            re.IGNORECASE,
        ),
        "Physics: Earth's magnetic elements and dip circle are deleted from NEET UG 2027 NMC syllabus.",
    ),
    (
        "Resolving Power of Optical Instruments",
        re.compile(
            r"\bresolving\s+power\s+of\s+(?:a\s+)?(?:microscope|telescope)\b",
            re.IGNORECASE,
        ),
        "Physics: Resolving power of microscope and astronomical telescope is deleted.",
    ),
    (
        "Polarization of Light / Devices",
        re.compile(
            r"\b(brewster(\'s)?\s+law|malus(\'s)?\s+law|polaroids?\s+and\s+polarization)\b",
            re.IGNORECASE,
        ),
        "Physics: Brewster's law, Malus's law, and polaroids are deleted from NEET UG 2027 NMC syllabus.",
    ),
    # --- CHEMISTRY DELETED TOPICS ---
    (
        "Solid State Unit",
        re.compile(
            r"\b(solid\s+state|unit\s+cells?|schottky\s+defect|frenkel\s+defect|bragg(\'s)?\s+law|close\s+packing\s+in\s+solids?)\b",
            re.IGNORECASE,
        ),
        "Chemistry: The entire Solid State unit is deleted from NEET UG 2027 NMC syllabus.",
    ),
    (
        "States of Matter (Gaseous & Liquid States Unit)",
        re.compile(
            r"\b(states\s+of\s+matter|liquefaction\s+of\s+gases|critical\s+temperature\s+and\s+critical\s+pressure)\b",
            re.IGNORECASE,
        ),
        "Chemistry: States of matter (macroscopic gas laws / liquids unit) is deleted.",
    ),
    (
        "Surface Chemistry Unit",
        re.compile(
            r"\b(surface\s+chemistry|adsorption\s+isotherm|freundlich\s+isotherm|langmuir\s+isotherm|peptization|coagulation\s+value|hardy[- ]schulze(\'s)?\s+rule|lyophilic\s+and\s+lyophobic\s+colloids?)\b",
            re.IGNORECASE,
        ),
        "Chemistry: Surface Chemistry (adsorption, colloids, emulsions) is deleted.",
    ),
    (
        "Hydrogen Unit",
        re.compile(
            r"\b(heavy\s+water|hydrogen\s+economy|ortho[- ]hydrogen|para[- ]hydrogen|water\s+gas\s+shift|(?:ionic|covalent|interstitial)\s+hydrides?|hydrogen\s+peroxide\s+(?:preparation|structure|properties|storage))\b|\\(?:section|subsection)\*?\{\s*(?:Unit\s+\d+\s*:\s*)?Hydrogen(?:\s*\}|\s*:\s*(?:Occurrence|Isotopes|Preparation|Compounds)|\s+and\s+its\s+Compounds)",
            re.IGNORECASE,
        ),
        "Chemistry: The Class 11 Hydrogen unit (hydrides, heavy water, hydrogen economy) is deleted.",
    ),
    (
        "s-Block Elements Unit",
        re.compile(r"\bs[- ]block(\s+elements?)?\b", re.IGNORECASE),
        "Chemistry: s-Block elements unit is deleted from NEET UG 2027 NMC syllabus.",
    ),
    (
        "Metallurgy / General Principles of Isolation",
        re.compile(
            r"\b(metallurg(y|ical)|ellingham\s+diagram|extraction\s+of\s+metals?|blast\s+furnace|froth\s+floatation|calcination\s+and\s+roasting|zone\s+refining|mond(\'s)?\s+process|van\s+arkel(\'s)?\s+process)\b",
            re.IGNORECASE,
        ),
        "Chemistry: General Principles and Processes of Isolation of Elements (Metallurgy) is deleted.",
    ),
    (
        "Polymers Unit",
        re.compile(
            r"\b(synthetic\s+polymers?|addition\s+polymeri[sz]ation|condensation\s+polymeri[sz]ation|vulcanization|nylon[- ]?(?:6|66|6,6)|dacron|bakelite|neoprene|buna[- ]?[sn]|teflon|glyptal|novolac)\b|\\(?:section|subsection|subsubsection)\*?\{[^\}]*\bPolymers?\b[^\}]*\}",
            re.IGNORECASE,
        ),
        "Chemistry: The Class 12 Polymers unit is deleted from NEET UG 2027 NMC syllabus.",
    ),
    (
        "Chemistry in Everyday Life Unit",
        re.compile(
            r"\b(chemistry\s+in\s+everyday\s+life|antipyretics?|tranquili[sz]ers?|antiseptics\s+and\s+disinfectants|antifertility\s+drugs?|artificial\s+sweeten(ing|ers?))\b",
            re.IGNORECASE,
        ),
        "Chemistry: Chemistry in Everyday Life unit is deleted from NEET UG 2027 NMC syllabus.",
    ),
]


def strip_latex_comments(line: str) -> str:
    """Strips unescaped LaTeX comments (%...) from a line."""
    return re.sub(r"(?<!\\)%.*", "", line)


def extract_braced_group(text: str, start_index: int) -> Optional[str]:
    """Finds the first '{' at or after start_index and returns the content inside the balanced braces."""
    brace_start = text.find("{", start_index)
    if brace_start == -1:
        return None
    depth = 0
    for i in range(brace_start, len(text)):
        if text[i] == "{" and (i == 0 or text[i - 1] != "\\"):
            depth += 1
        elif text[i] == "}" and (i == 0 or text[i - 1] != "\\"):
            depth -= 1
            if depth == 0:
                return text[brace_start + 1 : i]
    return None


# =========================================================================
# CHECK 1: SYNTAX & ENVIRONMENT STACK VALIDATION
# =========================================================================
def check_1_syntax_and_env_stack(content: str, lines: List[str]) -> CheckResult:
    env_stack: List[Tuple[str, int]] = []
    begin_re = re.compile(r"\\begin\{([a-zA-Z0-9_\*]+)\}")
    end_re = re.compile(r"\\end\{([a-zA-Z0-9_\*]+)\}")
    errors: List[str] = []

    for idx, line in enumerate(lines, 1):
        uncommented = strip_latex_comments(line)
        begins = begin_re.findall(uncommented)
        ends = end_re.findall(uncommented)

        for b in begins:
            env_stack.append((b, idx))

        for e in ends:
            if not env_stack:
                errors.append(f"Line {idx}: Unexpected \\end{{{e}}} with empty environment stack.")
            else:
                last_b, last_idx = env_stack.pop()
                if last_b != e:
                    errors.append(
                        f"Line {idx}: Mismatched environment. Expected \\end{{{last_b}}} "
                        f"(opened at line {last_idx}), found \\end{{{e}}}."
                    )

    while env_stack:
        b, idx = env_stack.pop()
        errors.append(f"Unclosed \\begin{{{b}}} opened at line {idx}.")

    if errors:
        return CheckResult(
            check_id=1,
            name="Syntax & Environment Stack Validation",
            passed=False,
            message=f"Failed with {len(errors)} environment nesting/stack error(s).",
            details=errors,
        )
    return CheckResult(
        check_id=1,
        name="Syntax & Environment Stack Validation",
        passed=True,
        message="All LaTeX environments properly nested and closed in strict LIFO order.",
    )


# =========================================================================
# CHECK 2: NON-COMMENT CURLY BRACE MATCHING
# =========================================================================
def check_2_curly_brace_matching(content: str, lines: List[str]) -> CheckResult:
    open_braces = 0
    close_braces = 0
    imbalance_points: List[str] = []

    running_balance = 0
    for idx, line in enumerate(lines, 1):
        uncommented = strip_latex_comments(line)
        # ignore escaped braces \{ and \}
        clean = re.sub(r"\\[\{\}]", "", uncommented)
        opens = clean.count("{")
        closes = clean.count("}")
        open_braces += opens
        close_braces += closes
        running_balance += opens - closes
        if running_balance < 0 and len(imbalance_points) < 3:
            imbalance_points.append(
                f"Line {idx}: Running brace balance dropped below zero ({running_balance}). Extra '}}' detected."
            )

    if open_braces != close_braces:
        details = [
            f"Total open '{{': {open_braces}",
            f"Total close '}}': {close_braces}",
            f"Net discrepancy: {open_braces - close_braces}",
        ]
        details.extend(imbalance_points)
        return CheckResult(
            check_id=2,
            name="Non-comment Curly Brace Matching",
            passed=False,
            message=f"Brace count mismatch: {open_braces} open '{{' vs {close_braces} close '}}'.",
            details=details,
        )
    return CheckResult(
        check_id=2,
        name="Non-comment Curly Brace Matching",
        passed=True,
        message=f"Exact curly brace match verified: {open_braces} open '{{' and {close_braces} close '}}'.",
    )


# =========================================================================
# CHECK 3: FRONT BANNER ATTRIBUTION
# =========================================================================
def check_3_front_banner_attribution(content: str) -> CheckResult:
    pattern = re.compile(
        r"Prepared,\s+Compiled\s+\\\&\s+Authored\s+by\s+Satya\s+Prakash",
        re.IGNORECASE,
    )
    match = pattern.search(content)

    if match:
        return CheckResult(
            check_id=3,
            name="Front Banner Attribution",
            passed=True,
            message="Verified mandatory banner attribution: 'Prepared, Compiled \\& Authored by Satya Prakash'.",
        )

    partial = "Satya Prakash" in content
    details = []
    if partial:
        details.append(
            "Found 'Satya Prakash' in file, but missing exact banner string: "
            "'Prepared, Compiled \\& Authored by Satya Prakash'."
        )
    else:
        details.append("Name 'Satya Prakash' was completely absent from document banner.")

    return CheckResult(
        check_id=3,
        name="Front Banner Attribution",
        passed=False,
        message="Missing mandatory attribution banner 'Prepared, Compiled \\& Authored by Satya Prakash'.",
        details=details,
    )


# =========================================================================
# CHECK 4: RUNNING HEADER ATTRIBUTION
# =========================================================================
def check_4_running_header_attribution(content: str) -> CheckResult:
    # Match \fancyhead with R option or \rhead
    header_cmd_re = re.compile(
        r"(?:\\fancyhead\s*\[[^\]]*R[^\]]*\]|\\rhead)",
        re.IGNORECASE,
    )

    for match in header_cmd_re.finditer(content):
        header_text = extract_braced_group(content, match.end())
        if header_text and re.search(r"Satya\s+Prakash", header_text, re.IGNORECASE):
            return CheckResult(
                check_id=4,
                name="Running Header Attribution",
                passed=True,
                message=f"Verified upper-right running header attribution for 'Satya Prakash'.",
            )

    return CheckResult(
        check_id=4,
        name="Running Header Attribution",
        passed=False,
        message="Missing upper-right running header specifying 'Satya Prakash'. Expected \\fancyhead[R]{...Satya Prakash...} or \\rhead{...Satya Prakash...}.",
        details=["Check document preamble and pagestyle configuration."],
    )


# =========================================================================
# CHECK 5: SEMANTIC CALLOUT PRESENCE
# =========================================================================
def check_5_semantic_callouts(content: str, allow_missing: bool = False) -> CheckResult:
    required_boxes = [
        "conceptbox",
        "formulabox",
        "usecasebox",
        "trapbox",
        "ncertbox",
    ]
    counts: Dict[str, int] = {}
    missing: List[str] = []

    for box in required_boxes:
        pattern = re.compile(rf"\\begin\{{{box}\}}")
        count = len(pattern.findall(content))
        counts[box] = count
        if count == 0:
            missing.append(box)

    summary_counts = ", ".join(f"{k}: {v}" for k, v in counts.items())

    if not missing:
        return CheckResult(
            check_id=5,
            name="Semantic Callout Presence",
            passed=True,
            message=f"All 5 semantic callouts present ({summary_counts}).",
            details=[f"{k}: {v} instance(s)" for k, v in counts.items()],
        )

    if allow_missing:
        return CheckResult(
            check_id=5,
            name="Semantic Callout Presence",
            passed=True,
            message=f"Missing boxes permitted by flag ({summary_counts}). Missing: {', '.join(missing)}.",
            details=[f"Missing: {', '.join(missing)} (permitted by --allow-missing-boxes)"],
        )

    return CheckResult(
        check_id=5,
        name="Semantic Callout Presence",
        passed=False,
        message=f"Missing mandatory semantic callout environment(s): {', '.join(missing)} ({summary_counts}).",
        details=[
            f"Missing required box environments: {missing}",
            "Master chapter modules must include at least one instance of conceptbox, formulabox, usecasebox, trapbox, and ncertbox.",
        ],
    )


# =========================================================================
# CHECK 6: DELETED SYLLABUS EXCLUSION SCANNER (Non-trapbox)
# =========================================================================
def check_6_deleted_syllabus_exclusion(content: str, lines: List[str]) -> CheckResult:
    violations: List[str] = []
    in_trapbox_depth = 0

    begin_trap_re = re.compile(r"\\begin\{trapbox\}")
    end_trap_re = re.compile(r"\\end\{trapbox\}")

    for idx, line in enumerate(lines, 1):
        uncommented = strip_latex_comments(line)

        begins = len(begin_trap_re.findall(uncommented))
        ends = len(end_trap_re.findall(uncommented))

        # If line contains \begin{trapbox} or is currently within a trapbox
        if in_trapbox_depth > 0 or begins > 0:
            # Update trapbox depth
            in_trapbox_depth = max(0, in_trapbox_depth + begins - ends)
            # Skip checking deleted topics inside trapboxes
            continue

        # Line is completely outside any trapbox
        in_trapbox_depth = max(0, in_trapbox_depth + begins - ends)

        for topic_name, pattern, reason in DELETED_NMC_PATTERNS:
            match = pattern.search(uncommented)
            if match:
                matched_token = match.group(0)
                snippet = uncommented.strip()
                if len(snippet) > 80:
                    snippet = snippet[:77] + "..."
                violations.append(
                    f"Line {idx} [{topic_name}]: Found forbidden mention '{matched_token}' outside trapbox -> \"{snippet}\""
                )

    if violations:
        return CheckResult(
            check_id=6,
            name="Deleted Syllabus Exclusion Scanner",
            passed=False,
            message=f"Detected {len(violations)} positive formulation(s) of deleted NMC topics outside trapbox.",
            details=violations,
        )
    return CheckResult(
        check_id=6,
        name="Deleted Syllabus Exclusion Scanner",
        passed=True,
        message="Strict zero-tolerance exclusion verified: 0 deleted NMC topics detected outside trapbox.",
    )


# =========================================================================
# CHECK 7: TECTONIC COMPILATION & PDF VERIFICATION
# =========================================================================
def find_tectonic_compiler() -> Optional[str]:
    user_bin = "/home/spdedsec/.local/bin/tectonic"
    if os.path.isfile(user_bin) and os.access(user_bin, os.X_OK):
        return user_bin
    system_tectonic = shutil.which("tectonic")
    if system_tectonic:
        return system_tectonic
    return None


def check_7_tectonic_compilation(filepath: str, compiler_path: Optional[str] = None) -> CheckResult:
    if not compiler_path:
        compiler_path = find_tectonic_compiler()

    if not compiler_path:
        return CheckResult(
            check_id=7,
            name="Tectonic Compilation",
            passed=False,
            message="Tectonic compiler executable not found at /home/spdedsec/.local/bin/tectonic or on PATH.",
            details=["Ensure tectonic is installed and executable."],
        )

    abs_path = os.path.abspath(filepath)
    file_dir = os.path.dirname(abs_path)
    base_name = os.path.basename(abs_path)
    expected_pdf = os.path.splitext(abs_path)[0] + ".pdf"

    try:
        proc = subprocess.run(
            [compiler_path, base_name],
            cwd=file_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=180,
        )
    except subprocess.TimeoutExpired:
        return CheckResult(
            check_id=7,
            name="Tectonic Compilation",
            passed=False,
            message="Compilation timed out after 180 seconds.",
            details=["Tectonic compilation exceeded maximum allowed duration."],
        )
    except Exception as exc:
        return CheckResult(
            check_id=7,
            name="Tectonic Compilation",
            passed=False,
            message=f"Failed to execute compiler: {str(exc)}",
            details=[str(exc)],
        )

    if proc.returncode != 0:
        output_tail = proc.stdout.splitlines()[-15:] if proc.stdout else []
        return CheckResult(
            check_id=7,
            name="Tectonic Compilation",
            passed=False,
            message=f"Tectonic compilation failed with exit code {proc.returncode}.",
            details=output_tail,
        )

    if not os.path.isfile(expected_pdf):
        return CheckResult(
            check_id=7,
            name="Tectonic Compilation",
            passed=False,
            message=f"Compilation exited with 0 but expected PDF was not found at {expected_pdf}.",
            details=["PDF artifact missing."],
        )

    pdf_size = os.path.getsize(expected_pdf)
    if pdf_size == 0:
        return CheckResult(
            check_id=7,
            name="Tectonic Compilation",
            passed=False,
            message="Produced PDF is completely empty (0 bytes).",
            details=[f"PDF Path: {expected_pdf}"],
        )

    pdf_size_kb = pdf_size / 1024.0
    return CheckResult(
        check_id=7,
        name="Tectonic Compilation",
        passed=True,
        message=f"Tectonic compilation PASSED. Generated valid PDF: {os.path.basename(expected_pdf)} ({pdf_size_kb:.1f} KiB).",
        details=[f"PDF Path: {expected_pdf}", f"Size: {pdf_size} bytes"],
    )


# =========================================================================
# MODULE RUNNER
# =========================================================================
def validate_single_module(
    filepath: str,
    run_compilation: bool = True,
    allow_missing_boxes: bool = False,
    compiler_path: Optional[str] = None,
) -> ModuleReport:
    """Runs all 7 checks on a single LaTeX module file."""
    if not os.path.isfile(filepath):
        res = CheckResult(
            check_id=0,
            name="File Existence",
            passed=False,
            message=f"File not found: {filepath}",
        )
        return ModuleReport(filepath=filepath, all_passed=False, checks=[res])

    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    lines = content.splitlines()
    checks: List[CheckResult] = []

    # Check 1: Syntax & Environment Stack
    checks.append(check_1_syntax_and_env_stack(content, lines))

    # Check 2: Curly Brace Balance
    checks.append(check_2_curly_brace_matching(content, lines))

    # Check 3: Front Banner Attribution
    checks.append(check_3_front_banner_attribution(content))

    # Check 4: Running Header Attribution
    checks.append(check_4_running_header_attribution(content))

    # Check 5: Semantic Callouts
    checks.append(check_5_semantic_callouts(content, allow_missing=allow_missing_boxes))

    # Check 6: Deleted Syllabus Exclusion
    checks.append(check_6_deleted_syllabus_exclusion(content, lines))

    # Check 7: Tectonic Compilation
    if run_compilation:
        checks.append(check_7_tectonic_compilation(filepath, compiler_path=compiler_path))
    else:
        checks.append(
            CheckResult(
                check_id=7,
                name="Tectonic Compilation",
                passed=True,
                message="Compilation check SKIPPED by flag (--skip-compile).",
                details=["Skipped."],
            )
        )

    all_passed = all(c.passed for c in checks)
    return ModuleReport(filepath=filepath, all_passed=all_passed, checks=checks)


# =========================================================================
# REPORTING & FORMATTING
# =========================================================================
def print_module_report(report: ModuleReport, use_color: bool = True) -> None:
    GREEN = "\033[92m" if use_color else ""
    RED = "\033[91m" if use_color else ""
    YELLOW = "\033[93m" if use_color else ""
    BOLD = "\033[1m" if use_color else ""
    RESET = "\033[0m" if use_color else ""

    status_tag = f"{GREEN}[PASS]{RESET}" if report.all_passed else f"{RED}[FAIL]{RESET}"
    print(f"\n{BOLD}======================================================================{RESET}")
    print(f"Module: {BOLD}{report.filepath}{RESET} -> {status_tag}")
    print(f"{BOLD}======================================================================{RESET}")

    for c in report.checks:
        tag = f"{GREEN}PASS{RESET}" if c.passed else f"{RED}FAIL{RESET}"
        print(f"  [{tag}] Check {c.check_id}: {BOLD}{c.name}{RESET}")
        print(f"         {c.message}")
        if not c.passed and c.details:
            for d in c.details[:5]:
                print(f"         {YELLOW}* {d}{RESET}")
            if len(c.details) > 5:
                print(f"         {YELLOW}* ... and {len(c.details) - 5} more issue(s){RESET}")


def collect_target_files(paths: List[str], scan_all: bool, base_dir: str) -> List[str]:
    targets = []
    if paths:
        for p in paths:
            if os.path.isfile(p):
                targets.append(p)
            elif os.path.isdir(p):
                targets.extend(str(x) for x in Path(p).glob("**/*.tex"))
    elif scan_all:
        chapters_dir = os.path.join(base_dir, "chapters")
        targets.extend(str(x) for x in Path(os.path.join(chapters_dir, "physics")).glob("*.tex"))
        targets.extend(str(x) for x in Path(os.path.join(chapters_dir, "chemistry")).glob("*.tex"))
    return sorted(list(set(targets)))


# =========================================================================
# CLI ENTRYPOINT
# =========================================================================
def main():
    parser = argparse.ArgumentParser(
        description="NEET UG 2027 E2E Module Validator & 7-Gate Quality Test Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="Specific .tex module path(s) to validate.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Scan and validate all .tex files in chapters/physics/ and chapters/chemistry/.",
    )
    parser.add_argument(
        "--file",
        dest="explicit_file",
        help="Optional explicit single file flag.",
    )
    parser.add_argument(
        "--skip-compile",
        action="store_true",
        help="Skip Check 7 (Tectonic compilation) for rapid offline syntax checks.",
    )
    parser.add_argument(
        "--compile",
        action="store_true",
        help="Explicitly enable Check 7 (Tectonic compilation). Defaults to true unless --skip-compile is passed.",
    )
    parser.add_argument(
        "--allow-missing-boxes",
        action="store_true",
        help="Do not fail Check 5 if some semantic callout boxes are missing (useful for lab manuals).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output structured JSON results instead of terminal human-readable format.",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable ANSI terminal colors.",
    )

    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(script_dir, ".."))

    input_paths = list(args.files)
    if args.explicit_file:
        input_paths.append(args.explicit_file)

    target_files = collect_target_files(input_paths, args.all, base_dir)

    if not target_files:
        print("No target .tex files specified or found. Use --all or specify file path(s).", file=sys.stderr)
        parser.print_help(sys.stderr)
        sys.exit(1)

    run_compilation = not args.skip_compile
    use_color = (sys.stdout.isatty() or os.environ.get("FORCE_COLOR") == "1") and not args.no_color

    reports: List[ModuleReport] = []
    overall_passed = True

    for fpath in target_files:
        report = validate_single_module(
            fpath,
            run_compilation=run_compilation,
            allow_missing_boxes=args.allow_missing_boxes,
        )
        reports.append(report)
        if not report.all_passed:
            overall_passed = False
        if not args.json:
            print_module_report(report, use_color=use_color)

    if args.json:
        output_payload = {
            "overall_passed": overall_passed,
            "total_modules": len(reports),
            "passed_modules": sum(1 for r in reports if r.all_passed),
            "failed_modules": sum(1 for r in reports if not r.all_passed),
            "modules": [r.summary_dict() for r in reports],
        }
        print(json.dumps(output_payload, indent=2))
    else:
        print(f"\n======================================================================")
        print(f"E2E VALIDATION SUITE SUMMARY:")
        print(f"Total Evaluated Modules: {len(reports)}")
        print(f"Passed: {sum(1 for r in reports if r.all_passed)}")
        print(f"Failed: {sum(1 for r in reports if not r.all_passed)}")
        print(f"Overall Result: {'PASSED (READY)' if overall_passed else 'FAILED'}")
        print(f"======================================================================\n")

    sys.exit(0 if overall_passed else 1)


if __name__ == "__main__":
    main()
