# NEET UG 2027 Master Theory Suite — Test Infrastructure Specification (`TEST_INFRA.md`)

**Document Version:** 1.0.0  
**Status:** Active & Verified  
**Author:** Test Writer & QA Specialist (`test_writer_m0`)  
**Scope:** Opaque-box Verification Engine, 7-Gate Quality Harness & Syllabus Scanner  

---

## 1. Overview & Verification Philosophy

The NEET UG 2027 Study Materials Master Theory Suite requires publication-grade mathematical and chemical rigor, 100% syntactic compliance, exact editorial attribution, and strict adherence to the rationalized NMC syllabus.

To guarantee these invariants across all authoring milestones (M1 through M5), an independent, requirement-driven, opaque-box test harness is established at:
```bash
/home/spdedsec/neet-study-materials/scripts/validate_modules.py
```

### Core Testing Invariants:
1. **Zero-Facade Guarantee:** Every test is genuine. No test returns hardcoded passes or mock outputs for unverified content.
2. **Deterministic Strictness:** Tests enforce clean LIFO environment nesting, exact curly brace counting, mandatory author attribution in banner and header, full deployment of all five custom breakable semantic callout boxes, and rigorous exclusion of all deleted NMC syllabus topics.
3. **End-to-End Compilation:** Validates that LaTeX source compiles cleanly via Tectonic into a readable, non-empty `.pdf` file.

---

## 2. Test Architecture & Toolchain Components

| Script / Tool | Location | Primary Role | Output Artifact |
|---|---|---|---|
| **Syntax Gate** | `scripts/validate_latex.py` | Environment stack closure (LIFO) and brace balancing | Terminal Exit Code `0` or `1` |
| **E2E 7-Gate Validator** | `scripts/validate_modules.py` | Full 7-Gate semantic, attribution, exclusion, and compilation test harness | Terminal / Structured JSON report |
| **TeX Compiler Engine** | `/home/spdedsec/.local/bin/tectonic` | Modern XeTeX-based automated typesetting engine | Publication-grade `.pdf` (A4) |
| **Batch Builder** | `scripts/compile_all.sh` | End-to-end repository compiler shell script | All module `.pdf` files |
| **Style Package** | `styles/neet_style.sty` | Global layout, margins, colors, and 5 tcolorbox callout environments | Formatted layout |

---

## 3. The 7 Verification Gates Specification

Every module in `chapters/physics/` and `chapters/chemistry/` is subjected to the following seven sequential gates:

### Gate 1: Syntax & Environment Stack Validation
- **Requirement:** Every `\begin{<env>}` must have an exact matching `\end{<env>}` in strict LIFO order.
- **Handling:** Comments (`%...`) are stripped prior to regex scanning. Supports starred environments (`align*`, `equation*`) and nested custom environments.
- **Pass Criteria:** Stack is completely empty at EOF with zero mismatched closures.

### Gate 2: Non-comment Curly Brace Matching
- **Requirement:** Total opening braces `{` must equal total closing braces `}` on non-comment lines.
- **Handling:** Escaped braces (`\{` and `\}`) are sanitized prior to tallying. Real-time balance is monitored to identify the exact line where imbalance originates.
- **Pass Criteria:** `count('{') == count('}')`.

### Gate 3: Front Banner Attribution
- **Requirement:** The front title banner must feature:
  ```latex
  Prepared, Compiled \& Authored by Satya Prakash
  ```
- **Handling:** Scans front matter following `\begin{document}` for exact attribution string with escaped ampersand `\&`.
- **Pass Criteria:** Exact attribution string present in front banner.

### Gate 4: Running Header Attribution
- **Requirement:** Upper-right running header on interior pages must display `Satya Prakash`.
- **Handling:** Extracts the balanced argument of `\fancyhead[...R...]` or `\rhead` and checks for `Satya Prakash`, supporting arbitrary nested macros like `\fancyhead[R]{\small \textbf{Satya Prakash}}` or `\rhead{\small\textbf{\color{accentblue}Satya Prakash}}`.
- **Pass Criteria:** Top-right running header contains `Satya Prakash`.

### Gate 5: Semantic Callout Presence
- **Requirement:** Master chapter theory modules must integrate all five custom `tcolorbox` callout environments defined in `styles/neet_style.sty`:
  1. `\begin{conceptbox}` — Core principle, definition, or postulate
  2. `\begin{formulabox}` — Master equation, step-by-step mathematical derivation
  3. `\begin{usecasebox}` — Application regime, boundary conditions, calculation shortcut
  4. `\begin{trapbox}` — NEET exam trap, common pitfall, sign error, A/R misconception
  5. `\begin{ncertbox}` — Direct NCERT textual anchor, high-yield line extraction
- **Pass Criteria:** Count of each environment $\ge 1$. Missing boxes trigger failure unless `--allow-missing-boxes` is explicitly declared.

### Gate 6: Deleted NMC Syllabus Exclusion Scanner
- **Requirement:** Complete omission of all deleted NMC NEET UG 2027 topics from positive theoretical formulations.
- **Isolation Rule:** Lines enclosed within `\begin{trapbox} ... \end{trapbox}` are safely excluded, allowing explicit student alerts (e.g. *"Note: Carnot engine has been deleted by NMC"*).
- **Non-Trapbox Strict Exclusion Rules (18 Rule Patterns):**
  - **Physics:**
    - Carnot engine / cycle / refrigerator (`\bcarnot(\'s)?\b`)
    - Doppler effect in sound/light (`\bdoppler(\'s)?\b`)
    - Potentiometer principle and wire comparisons (`\bpotentiometer(s)?\b`)
    - Cyclotron acceleration (`\bcyclotron(s)?\b`)
    - Transistors, BJT, npn/pnp transistors (`\b(transistors?|bjt|npn\s+transistor|pnp\s+transistor)\b`)
    - Radioactivity, radioactive decay laws, $\alpha/\beta/\gamma$ decay (`\b(radioactiv(e|ity)|(?:alpha|beta|gamma)\s+decay|decay\s+constant\s+of\s+radio|radionuclides?)\b`)
    - Van de Graaff generator (`\bvan\s*de\s*graaff\b`)
    - Earth's magnetic elements, dip circle (`\b(earth(\'s)?\s+magnetic\s+elements?|magnetic\s+(?:declination|inclination|dip)|horizontal\s+component\s+of\s+earth(\'s)?\s+magnetic\s+field)\b`)
    - Resolving power of microscope/telescope (`\bresolving\s+power\s+of\s+(?:a\s+)?(?:microscope|telescope)\b`)
    - Polarization devices, Brewster's/Malus's laws (`\b(brewster(\'s)?\s+law|malus(\'s)?\s+law|polaroids?\s+and\s+polarization)\b`)
  - **Chemistry:**
    - Solid State unit, unit cells, Bragg's law, Schottky/Frenkel defects (`\b(solid\s+state|unit\s+cells?|schottky\s+defect|frenkel\s+defect|bragg(\'s)?\s+law|close\s+packing\s+in\s+solids?)\b`)
    - States of Matter (macroscopic gas/liquids unit, liquefaction of gases) (`\b(states\s+of\s+matter|liquefaction\s+of\s+gases|critical\s+temperature\s+and\s+critical\s+pressure)\b`)
    - Surface Chemistry unit, adsorption isotherms, peptization, Hardy-Schulze rule (`\b(surface\s+chemistry|adsorption\s+isotherm|freundlich\s+isotherm|langmuir\s+isotherm|peptization|coagulation\s+value|hardy[- ]schulze(\'s)?\s+rule)\b`)
    - Hydrogen unit (heavy water, hydrogen economy, hydrides, hydrogen peroxide properties/prep, or standalone unit heading)
    - s-Block elements unit (`\bs[- ]block(\s+elements?)?\b`)
    - Metallurgy / Isolation of elements, Ellingham diagram, blast furnace, froth floatation, refining methods (`\b(metallurg(y|ical)|ellingham\s+diagram|extraction\s+of\s+metals?|blast\s+furnace|froth\s+floatation|calcination\s+and\s+roasting|zone\s+refining|mond(\'s)?\s+process|van\s+arkel(\'s)?\s+process)\b`)
    - Polymers unit, synthetic polymers, Bakelite, Nylon, Buna, Dacron (`\b(synthetic\s+polymers?|addition\s+polymeri[sz]ation|condensation\s+polymeri[sz]ation|vulcanization|nylon[- ]?(?:6|66|6,6)|dacron|bakelite|neoprene|buna[- ]?[sn]|teflon|glyptal|novolac)\b`)
    - Chemistry in Everyday Life, analgesics, tranquilizers, antiseptics, artificial sweeteners (`\b(chemistry\s+in\s+everyday\s+life|antipyretics?|tranquili[sz]ers?|antiseptics\s+and\s+disinfectants|antifertility\s+drugs?|artificial\s+sweeten(ing|ers?))\b`)
- **Pass Criteria:** Exactly zero matches detected outside `trapbox` environments.

### Gate 7: Tectonic Compilation & PDF Output Verification
- **Requirement:** Invokes `/home/spdedsec/.local/bin/tectonic` on target file from within its native directory.
- **Pass Criteria:**
  1. Process exit code is `0`.
  2. Generated `.pdf` file exists at `<base>.pdf`.
  3. Generated `.pdf` file size is strictly $> 0$ bytes.

---

## 4. Test Suite Invocation Commands

### 4.1 Validate Single Module (Full 7 Gates)
```bash
python3 scripts/validate_modules.py chapters/physics/mechanics_master_theory.tex
```

### 4.2 Validate Multiple Modules (Full 7 Gates)
```bash
python3 scripts/validate_modules.py \
  chapters/physics/mechanics_master_theory.tex \
  chapters/physics/rotational_gravitation_fluids_theory.tex \
  chapters/chemistry/physical_chemistry_master_theory.tex
```

### 4.3 Validate All Chapters in Fast Syntax/Semantic Mode (Skips Compilation)
```bash
python3 scripts/validate_modules.py --all --skip-compile
```

### 4.4 Validate Legacy Lab Handbooks (Allows Missing Callout Boxes)
```bash
python3 scripts/validate_modules.py --allow-missing-boxes chapters/physics/experimental_physics_unit_20.tex
```

### 4.5 Machine-Readable JSON Output (CI / Toolchain Integration)
```bash
python3 scripts/validate_modules.py --json chapters/chemistry/physical_chemistry_master_theory.tex
```

### 4.6 Unit Test Suite for the Test Harness
```bash
python3 .agents/teamwork/test_writer_m0/test_validate_modules.py
```

---

## 5. Traceability Matrix

| Feature ID | Feature Description | Covered By Verification Gates | Status |
|---|---|---|---|
| **F-E2E-TEST** | Comprehensive test runner `scripts/validate_modules.py` | Gates 1, 2, 3, 4, 5, 6, 7 | **VERIFIED & OPERATIONAL** |
| **F-STYLE-CALLOUTS** | 5 semantic breakable callouts (`conceptbox`, `formulabox`, `usecasebox`, `trapbox`, `ncertbox`) | Gate 5 | **VERIFIED & OPERATIONAL** |
| **F-AUTH-ATTRIB** | Banner attribution `Prepared, Compiled \& Authored by Satya Prakash` & header `Satya Prakash` | Gates 3 & 4 | **VERIFIED & OPERATIONAL** |
| **F-NMC-EXCLUSION** | Strict exclusion of deleted NMC topics outside trapboxes | Gate 6 | **VERIFIED & OPERATIONAL** |
| **F-COMPILATION** | Error-free Tectonic compilation into publication-quality `.pdf` | Gate 7 | **VERIFIED & OPERATIONAL** |

---

## 6. Exit Codes & CI Integration

- `0`: All tested modules passed all active gates. Ready for publication.
- `1`: One or more verification gates failed. Details logged with specific line numbers and error excerpts.
