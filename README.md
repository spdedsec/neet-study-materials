# NEET UG 2027 Study Materials Repository
**Prepared by Satya Prakash**

---

## 1. Project Objective & Standards
This repository contains a modular, publication-grade LaTeX suite specifically engineered for **NEET UG 2027**. 

### Editorial Standard & Attribution
- **Zero AI Bloat:** No filler phrases ("the ultimate", "the best", "one and only"), no narrative padding. Pure high-density technical notes.
- **Strict NMC Alignment:** Strictly calibrated to the revised National Medical Commission (NMC) syllabus and rationalized NCERT textbooks. Dropped chapters are formally marked and excluded from core prep.
- **Rigorous Formula Architecture:** Every formula includes variables, SI units, dimensional formula, conditions of validity, vector forms, edge cases, and high-yield traps.
- **Corner Attribution:** Front page carries `Prepared, Compiled & Authored by Satya Prakash`. Interior pages carry `Satya Prakash` in the upper-right corner header only.
- **Remote GitHub Repository:** [https://github.com/spdedsec/neet-study-materials](https://github.com/spdedsec/neet-study-materials)

---

## 2. Directory Structure

```text
neet-study-materials/
├── styles/
│   └── neet_style.sty               # Central styling, custom callout boxes, fancyhdr, colors
├── syllabus/
│   └── neet_2027_master_syllabus.tex# Exhaustive, granular 50-unit syllabus & exclusion map
├── formulas/                        # Pure formula handbooks (boxed, use cases, traps)
│   ├── physics/                     # Mechanics, Electrodynamics, Optics, Modern Physics, Thermal
│   └── chemistry/                   # Physical Chemistry, Inorganic Trends, Organic Reaction Sheets
├── chapters/                        # Comprehensive chapter notes (Theory, Formulas, NCERT Traps)
│   ├── physics/
│   ├── chemistry/
│   ├── botany/
│   └── zoology/
├── scripts/                         # Build, lint, and compilation automation scripts
│   └── compile_all.sh
└── README.md
```

---

## 3. Custom LaTeX Environments

| Environment | Purpose | Primary Color Accent |
| :--- | :--- | :--- |
| `\begin{formulabox}[Title]` | Mathematical governing equations, vector forms, units | Royal Navy Blue (`formulablue`) |
| `\begin{usecasebox}[Title]` | Assumptions, valid domains, boundary limits, shortcuts | Forest Green (`usecasegreen`) |
| `\begin{trapbox}[Title]` | Exam pitfalls, sign errors, exceptions, A/R traps | Crimson Red (`traprange`) |
| `\begin{ncertbox}[Title]` | Direct NCERT lines, crucial figures, tabular data | Amber Gold (`ncertgold`) |
| `\begin{conceptbox}[Title]`| Core laws, fundamental postulates, definitions | Slate Navy (`primarydark`) |

---

## 4. Execution Workflow

1. **Phase 1: Master Syllabus Blueprint** (`syllabus/neet_2027_master_syllabus.tex`)
   - Granular breakdown of 20 Physics units, 20 Chemistry units, and 10 Biology units.
   - Distinct classification: `[CORE]`, `[PRACTICAL / EXPERIMENTAL]`, `[EXCLUDED / NMC DELETED]`.
2. **Phase 2: Formula & Equation Handbooks** (`formulas/`)
   - Comprehensive formula sheets for all calculation-intensive units.
   - Inclusion of variations, standard limits, dimensional checks.
3. **Phase 3: High-Yield Chapter Notes** (`chapters/`)
   - Unit-by-unit comprehensive modules.
   - Core concepts, reaction mechanisms, physiological processes, boxed equations, and NCERT line extractions.
