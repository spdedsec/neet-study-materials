# Project: NEET UG 2027 Study Materials Master Theory Suite

## Architecture
The project delivers a comprehensive, publication-grade LaTeX suite of thematic chapter-by-chapter theory modules, mathematical derivations, and high-yield problem archetypes strictly calibrated to the revised NMC NEET UG 2027 syllabus.

The system is organized into a Dual Track structure:
1. **E2E Testing & Quality Verification Track:**
   - Requirement-driven, opaque-box test runner and verification suite (`scripts/validate_latex.py`, `scripts/validate_modules.py`, and automated syllabus compliance / exclusion scans).
   - Publishes `TEST_READY.md` upon completion.
2. **Implementation Track:**
   - Authoring of 8 publication-grade master volumes (5 Physics volumes, 3 Chemistry volumes).
   - Strict adherence to `styles/neet_style.sty`, 5 custom breakable callout environments (`conceptbox`, `formulabox`, `usecasebox`, `trapbox`, `ncertbox`), author attribution banner `Prepared, Compiled \& Authored by Satya Prakash`, and running upper-right header `Satya Prakash`.
   - Complete exclusion of deleted NMC topics.
   - Compilation into publication-quality PDFs via `/home/spdedsec/.local/bin/tectonic`.
   - Repository synchronization: updating `README.md` and pushing all deliverables to GitHub `origin main`.

---

## Code Layout
```
/home/spdedsec/neet-study-materials/
├── styles/
│   └── neet_style.sty                   # Core style package (geometry, colors, callout boxes)
├── scripts/
│   ├── validate_latex.py               # Syntax & brace balance validator
│   ├── fix_ampersands.py               # Pre-compiler ampersand normalizer
│   ├── compile_all.sh                  # Batch compiler shell runner
│   └── validate_modules.py             # E2E semantic test harness (syntax, headers, exclusions)
├── chapters/
│   ├── physics/
│   │   ├── experimental_physics_unit_20.tex (.pdf) # Existing lab unit
│   │   ├── mechanics_master_theory.tex (.pdf)       # M1 Deliverable (Units 1-4)
│   │   ├── rotational_gravitation_fluids_theory.tex (.pdf) # M1 Deliverable (Units 5-7)
│   │   ├── thermal_physics_oscillations_theory.tex (.pdf)  # M2 Deliverable (Units 7-10)
│   │   ├── electrodynamics_master_theory.tex (.pdf)        # M2 Deliverable (Units 11-15)
│   │   └── optics_modern_physics_theory.tex (.pdf)         # M2 Deliverable (Units 16-19)
│   └── chemistry/
│       ├── practical_chemistry_lab_manual.tex (.pdf)       # Existing lab manual
│       ├── organic_reaction_mechanisms_handbook.tex        # Existing mechanisms handbook
│       ├── physical_chemistry_master_theory.tex (.pdf)     # M3 Deliverable (Units 1-8)
│       ├── inorganic_chemistry_master_compendium.tex (.pdf)# M3 Deliverable (Units 9-12)
│       └── organic_chemistry_master_theory.tex (.pdf)      # M4 Deliverable (Units 13-19)
├── README.md                            # Global syllabus & deliverable index
├── PROJECT.md                           # Master architectural blueprint
└── TEST_READY.md                        # E2E Test Suite readiness attestation
```

---

## Feature Inventory
| # | Feature Code | Feature Description | Milestone | Source |
|---|---|---|---|---|
| 1 | F-E2E-TEST | Comprehensive E2E test harness (`validate_modules.py`) verifying syntax, braces, headers, boxes, and deleted topics | M0 (Done) | Survey 3 & Request R4 |
| 2 | F-PHY-MECH | Mechanics Master Theory: 1D/2D Kinematics, Newton's Laws, Friction, Circular Motion, WEP, Momentum & Collisions | M1 (Done) | Survey 1 & Request R1 |
| 3 | F-PHY-ROT-GRAV | Rotational Dynamics, Gravitation & Fluids: Rigid Body, MOI proofs, Rolling on inclines, Kepler, Fluids | M1 (Done) | Survey 1 & Request R1 |
| 4 | F-PHY-THERM-OSC | Thermal Physics & Oscillations: First & Second Laws (no Carnot), KTG derivations, SHM, Waves | M2 (Done) | Survey 1 & Request R1 |
| 5 | F-PHY-ELECTRO | Electrodynamics Master Theory: Electrostatics, Gauss, Dielectrics, Current networks, Biot-Savart, AC | M2 (Done) | Survey 1 & Request R1 |
| 6 | F-PHY-OPT-MOD | Optics & Modern Physics: Lens-maker, Prism deviation, Wave optics, Photoelectric, Bohr atom, Semiconductors | M2 (Done) | Survey 1 & Request R1 |
| 7 | F-CHM-PHYSICAL | Physical Chemistry Master Theory: Mole concept, Wave mechanics, Thermodynamics, Equilibrium, Solutions, Kinetics | M3 (Done) | Survey 2 & Request R2 |
| 8 | F-CHM-INORGANIC | Inorganic Chemistry Compendium: Periodic trends, VSEPR, MO diagrams, Coordination, p-block, d/f-block | M3 (Done) | Survey 2 & Request R2 |
| 9 | F-CHM-ORGANIC | Organic Chemistry Master Theory: Electronic effects, intermediates, full reaction pathways, Biomolecules | M4 (Done) | Survey 2 & Request R2 |
| 10 | F-STYLE-CALLOUTS | Full implementation of `styles/neet_book.sty` with 5 semantic callouts for 6" x 9" trade paperback | All Modules | Survey 3 & Request R3 |
| 11 | F-AUTH-ATTRIB | Author attribution `Satya Prakash`, email `spdedsec@hotmail.com`, front matter, verso/recto headers | All Modules | Survey 3 & Request R3 |
| 12 | F-NMC-EXCLUSION | Strict exclusion of deleted NMC topics | All Modules | Surveys 1, 2 & Request R3 |
| 13 | F-COMPILATION | Error-free compilation of all 3 master books into publication-grade `.pdf` using Tectonic | All Milestones | Request R4 |
| 14 | F-BOX-PHYSICS | Refactor all boxed display equations, annotations, and tables in `books/physics_master_book.tex` to $\le 310$ pt usable width | M-PHYS | Request R1 (2026-10-16) |
| 15 | F-BOX-CHEMISTRY | Refactor all 216 overwide equations, reaction mechanisms, and tables in `books/chemistry_master_book.tex` to $\le 310$ pt usable width | M-CHEM | Request R2 (2026-10-16) |
| 16 | F-BOX-BIOLOGY | Refactor all 17 overwide elements in `books/biology_master_book.tex` (TikZ, tables, math strings) to $\le 310$ pt usable width | M-BIO | Request R4 & Acceptance Criteria |
| 17 | F-KDP-STRESS-TEST | Pass `python3 scripts/verify_books_kdp.py` with verdict APPROVE and total page count > 400 pages | M-FINAL | Request R4 & Acceptance Criteria |
| 18 | F-FORENSIC-AUDIT | Independent forensic integrity audit verifying zero cheating, zero facades, zero syllabus stripping | M-FINAL | Request R3 & Integrity Forensics |

---

## Milestones
| # | Name | Scope & Deliverables | Dependencies | Status |
|---|---|---|---|---|
| M0 | Survey & Scope Audit | Live audit of all 3 master books; catalog all overfull lines $\ge 10.0$ pt, verify KDP baseline | None | DONE (`survey_physics.md`, `survey_chemistry.md`, `survey_biology_kdp.md`) |
| M-PHYS | Physics 6" x 9" Margin Compliance | Refactor all overwide equations, annotations, and tables in `books/physics_master_book.tex` so `audit_book.py physics_master_book 10.0` reports 0 overfull instances. | M0 | DONE |
| M-CHEM | Chemistry 6" x 9" Margin Compliance | Refactor all overwide equations, mechanisms, and tables in `books/chemistry_master_book.tex` so `audit_book.py chemistry_master_book 10.0` reports 0 overfull instances. | M0 | DONE |
| M-BIO | Biology 6" x 9" Margin Compliance | Refactor all overwide lines in `books/biology_master_book.tex` so `audit_book.py biology_master_book 10.0` reports 0 overfull instances. | M0 | DONE |
| M-FINAL | Automated Verification & KDP Gate Validation | Run full audit across all 3 books (all report 0 overfull $\ge 10.0$ pt), pass `verify_books_kdp.py` (verdict APPROVE, > 400 pages), pass Forensic Integrity Audit. | M-PHYS, M-CHEM, M-BIO | DONE |

---

## Code Layout & Write Boundaries
- `books/physics_master_book.tex` — Exclusively owned by Worker Physics (`worker_physics_refactor`).
- `books/chemistry_master_book.tex` — Exclusively owned by Worker Chemistry (`worker_chemistry_refactor`).
- `books/biology_master_book.tex` — Exclusively owned by Worker Biology (`worker_biology_refactor`).
- Concurrent workers MUST NOT write outside their assigned manuscript file.
- All agent metadata and reports are stored in `.agents/teamwork/<agent_id>/`.

---

## Interface Contracts

### 1. LaTeX Package & Preamble Contract
Every `.tex` module must adhere to:
```latex
\documentclass[10pt,a4paper]{article}
\usepackage{../../styles/neet_style}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small \textbf{NEET UG 2027: <Subject / Module Title>}}
\fancyhead[R]{\small Satya Prakash}
\fancyfoot[L]{\small \textbf{NEET UG 2027 Prep Series}}
\fancyfoot[C]{\thepage}
\fancyfoot[R]{\small \textbf{<Discipline> Chapter Notes}}
```

### 2. Front Banner Contract
Every `.tex` module must begin immediately following `\begin{document}` with:
```latex
\begin{center}
  {\Huge \textbf{NEET UG 2027: Master Chapter Theory}}\\[6pt]
  {\Large \textbf{<Thematic Unit Title: In-Depth Derivations \& High-Yield Archetypes>}}\\[4pt]
  {\small \textbf{Prepared, Compiled \& Authored by Satya Prakash} $\cdot$ Strictly Calibrated to Revised NMC Syllabus}
  \vspace{4pt}
  \hrule height 1.5pt
\end{center}
```

### 3. Semantic Callout Usage Contract
Each module must contain multiple, substantive instances of:
- `\begin{conceptbox}[Title] ... \end{conceptbox}`
- `\begin{formulabox}[Title] ... \end{formulabox}`
- `\begin{usecasebox}[Title] ... \end{usecasebox}`
- `\begin{trapbox}[Title] ... \end{trapbox}`
- `\begin{ncertbox}[Title] ... \end{ncertbox}`

### 4. Zero-Tolerance NMC Exclusion Contract
No module may contain positive theoretical formulations of:
- Physics: Carnot engine / refrigerator, Doppler effect, Potentiometer, Cyclotron, Radioactivity ($\alpha, \beta, \gamma$ decays), Transistors, Van de Graaff, Earth's magnetic elements, Resolving power of microscope/telescope, Light polarization.
- Chemistry: Solid state, States of matter (gas/liquid macroscopic unit), Surface chemistry, Hydrogen, s-block elements, Metallurgy, Polymers, Chemistry in everyday life.
Any mention of these must appear solely within a `trapbox` alerting students to their deletion from the NEET UG syllabus.

### 5. Verification Gate Contract
1. `python3 scripts/validate_latex.py <file.tex>` must exit with code 0.
2. `python3 scripts/validate_modules.py <file.tex>` must exit with code 0.
3. `/home/spdedsec/.local/bin/tectonic <file.tex>` must produce a non-empty `.pdf` file.
