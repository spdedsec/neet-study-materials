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
| 1 | F-E2E-TEST | Comprehensive E2E test harness (`validate_modules.py`) verifying syntax, braces, headers, boxes, and deleted topics | M0 (Test Track) | Survey 3 & Request R4 |
| 2 | F-PHY-MECH | Mechanics Master Theory: 1D/2D Kinematics, Newton's Laws, Friction, Circular Motion, WEP, Momentum & Collisions | M1 | Survey 1 & Request R1 |
| 3 | F-PHY-ROT-GRAV | Rotational Dynamics, Gravitation & Fluids: Rigid Body, MOI proofs, Rolling on inclines, Kepler, Fluids (Bernoulli, Poiseuille, Stokes) | M1 | Survey 1 & Request R1 |
| 4 | F-PHY-THERM-OSC | Thermal Physics & Oscillations: First & Second Laws (no Carnot), KTG derivations, SHM phase diagrams, Wave kinematics (no Doppler) | M2 | Survey 1 & Request R1 |
| 5 | F-PHY-ELECTRO | Electrodynamics Master Theory: Electrostatics, Gauss boundary, Dielectrics, Current networks (no Potentiometer/Cyclotron), Biot-Savart, Ampere, AC resonance | M2 | Survey 1 & Request R1 |
| 6 | F-PHY-OPT-MOD | Optics & Modern Physics: Lens-maker, Prism deviation, Wave optics (Fresnel/Fraunhofer, YDSE), Photoelectric, Bohr atom, Mass defect (no Radioactivity/Transistors) | M2 | Survey 1 & Request R1 |
| 7 | F-CHM-PHYSICAL | Physical Chemistry Master Theory: Mole concept, Wave mechanics, Thermodynamics & Thermochemistry, Equilibrium (Buffer, Ksp), Solutions, Electrochemistry, Kinetics | M3 | Survey 2 & Request R2 |
| 8 | F-CHM-INORGANIC | Inorganic Chemistry Compendium: Periodic trends, VSEPR geometries, MO diagrams (B2-O2-), Coordination (CFT splitting, CFSE, Jahn-Teller), p-block, d/f-block | M3 | Survey 2 & Request R2 |
| 9 | F-CHM-ORGANIC | Organic Chemistry Master Theory: Electronic effects, intermediates, full reaction pathways (EAS, SN1/SN2, E1/E2, Aldol, Cannizzaro), Biomolecules (Carbs, Proteins, Nucleic) | M4 | Survey 2 & Request R2 |
| 10 | F-STYLE-CALLOUTS | Full implementation of `styles/neet_style.sty` with 5 semantic callouts: `conceptbox`, `formulabox`, `usecasebox`, `trapbox`, `ncertbox` | All Modules | Survey 3 & Request R3 |
| 11 | F-AUTH-ATTRIB | Front banner attribution `Prepared, Compiled \& Authored by Satya Prakash` & upper-right running header `Satya Prakash` | All Modules | Survey 3 & Request R3 |
| 12 | F-NMC-EXCLUSION | Strict exclusion of deleted NMC topics (Carnot, Doppler, Potentiometer, Cyclotron, Transistors, Radioactivity; Solid state, Hydrogen, s-block, Metallurgy, Surface chem, Polymers) | All Modules | Surveys 1, 2 & Request R3 |
| 13 | F-COMPILATION | Error-free compilation of all 8 `.tex` modules into publication-grade `.pdf` using `/home/spdedsec/.local/bin/tectonic` | M5 | Survey 3 & Request R4 |
| 14 | F-README-SYNC | Complete indexing of all newly generated LaTeX sources and compiled PDFs with verified markdown links | M5 | Request R4 |
| 15 | F-GIT-PUSH | Commit all new `.tex` sources, `.pdf` files, and documentation, and push to GitHub `origin main` | M5 | Request R4 |

---

## Milestones
| # | Name | Scope & Deliverables | Dependencies | Status |
|---|---|---|---|---|
| M0 | E2E Testing & Quality Track | Create automated test harness `scripts/validate_modules.py` covering syntax, brace matching, header verification, attribution checks, and deleted topic regex scanner. Publish `TEST_READY.md`. | None | IN_PROGRESS (`5dc5320c-6214-456b-a91e-b4347965a902`) |
| M1 | Physics Core Mechanics & Dynamics | Author `chapters/physics/mechanics_master_theory.tex` and `chapters/physics/rotational_gravitation_fluids_theory.tex` with complete step-by-step derivations and problem archetypes. Compile to PDF. | M0 | IN_PROGRESS (`e16eddce-07e9-4bd5-9b55-a6d17bbd26cc`) |
| M2 | Physics Fields, Waves & Modern Physics | Author `chapters/physics/thermal_physics_oscillations_theory.tex`, `chapters/physics/electrodynamics_master_theory.tex`, and `chapters/physics/optics_modern_physics_theory.tex`. Compile to PDF. | M0 | IN_PROGRESS (`09f3b1a2-05f5-46cc-a7e6-49bf15a8796b`) |
| M3 | Physical & Inorganic Chemistry Compendium | Author `chapters/chemistry/physical_chemistry_master_theory.tex` and `chapters/chemistry/inorganic_chemistry_master_compendium.tex` with complete derivations, VSEPR geometries, MO diagrams, and CFT splitting. Compile to PDF. | M0 | IN_PROGRESS (`af252f5c-91b2-4a81-904c-0e642c8c1d07`) |
| M4 | Organic Chemistry Master Theory & Synthesis | Author `chapters/chemistry/organic_chemistry_master_theory.tex` (GOC, reaction intermediates, all named mechanisms, aliphatic/aromatic conversions, and biomolecules). Compile to PDF. | M0 | IN_PROGRESS (`1067bcf7-e4ff-4ef4-af3a-093ad92bd030`) |
| M5 | Final E2E Verification, README Index & Git Push | Run full E2E test suite (100% pass across all 8 modules), update `README.md`, commit and push to remote repository `origin main`. | M1, M2, M3, M4 | PLANNED |

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
