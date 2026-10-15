# NEET UG 2027 Study Materials Repository
**Prepared, Compiled & Authored by Satya Prakash**

---

## 1. Project Overview & Architectural Standards

This repository hosts the complete, publication-grade study materials suite engineered specifically for **NEET UG 2027**. Every theoretical module, derivation, and archetype has been authored with dense academic rigor, step-by-step mathematical proofs, complete reaction mechanisms, and strict calibration to the rationalized National Medical Commission (NMC) syllabus.

- **Remote GitHub Repository:** [https://github.com/spdedsec/neet-study-materials](https://github.com/spdedsec/neet-study-materials)
- **Target Exam:** NEET UG 2027 (National Eligibility cum Entrance Test - Undergraduate)
- **Syllabus Calibration:** 100% aligned with the revised NMC syllabus and rationalized NCERT textbooks.
- **Editorial & Attribution Policy:** Front/title banners carry `Prepared, Compiled & Authored by Satya Prakash`. Interior pages feature running headers with `Satya Prakash`. Zero marketing hype, filler text, or unverified claims.
- **Verification & Quality Gate:** Backed by an automated, opaque-box 7-gate test harness (`scripts/validate_modules.py`), full Tectonic compilation checks, and comprehensive audit specifications (`TEST_INFRA.md`, `TEST_READY.md`).

---

## 2. Physics Master Theory & Experimental Practicals Suite

Comprehensive thematic master volumes covering all 20 units of the NEET UG 2027 Physics syllabus, featuring complete mathematical derivations, vector calculus, coordinate transformations, and worked problem archetypes.

| Thematic Volume | NMC Units & Scope | LaTeX Source | Compiled PDF | Key Coverage & High-Yield Derivations |
| :--- | :--- | :--- | :--- | :--- |
| **Mechanics Master Theory** | Units 1--4: Kinematics, Laws of Motion, Work-Energy-Power | [`chapters/physics/mechanics_master_theory.tex`](chapters/physics/mechanics_master_theory.tex) | [`chapters/physics/mechanics_master_theory.pdf`](chapters/physics/mechanics_master_theory.pdf) | Dimensional calculus, error propagation, 1D/2D kinematics, projectile trajectory calculus, relative velocity, Newton's laws with constrained pulleys, friction dynamics, conical pendulum banking, work-energy theorem, variable mass systems, and 1D/2D oblique collisions. |
| **Rotational Dynamics, Gravitation & Fluids Theory** | Units 5--7: Rotational Motion, Gravitation, Solids & Fluids | [`chapters/physics/rotational_gravitation_fluids_theory.tex`](chapters/physics/rotational_gravitation_fluids_theory.tex) | [`chapters/physics/rotational_gravitation_fluids_theory.pdf`](chapters/physics/rotational_gravitation_fluids_theory.pdf) | Centre of mass integral formulations, parallel/perpendicular axis theorems, pure rolling without slipping on inclines, Kepler's three laws, gravitational field & potential integration, Hooke's law, Pascal's principle, surface tension capillary rise, Bernoulli's equation, and Stokes' law. |
| **Thermal Physics & Oscillations Theory** | Units 7--10: Thermal Physics, Thermodynamics, KTG, Oscillations & Waves | [`chapters/physics/thermal_physics_oscillations_theory.tex`](chapters/physics/thermal_physics_oscillations_theory.tex) | [`chapters/physics/thermal_physics_oscillations_theory.pdf`](chapters/physics/thermal_physics_oscillations_theory.pdf) | Thermal expansion, calorimetry, Stefan-Boltzmann & Wien's laws, First Law ($dQ=dU+dW$), Mayer's relation ($C_p-C_v=R$), Second Law (Kelvin-Planck/Clausius; *Carnot excluded*), KTG pressure derivation ($P=\frac{1}{3}\rho v_{rms}^2$), degrees of freedom, SHM phasor analysis, coupled springs, and standing waves in strings/pipes (*Doppler excluded*). |
| **Electrodynamics Master Theory** | Units 11--15: Electrostatics, Current, Magnetism, EMI, AC & EM Waves | [`chapters/physics/electrodynamics_master_theory.tex`](chapters/physics/electrodynamics_master_theory.tex) | [`chapters/physics/electrodynamics_master_theory.pdf`](chapters/physics/electrodynamics_master_theory.pdf) | Coulomb's law in vector form, Gauss's law boundary applications, capacitor dielectrics & energy density, drift velocity & Ohm's microscopic law, Kirchhoff's loop laws (*potentiometer excluded*), Biot-Savart & Ampere's law (*cyclotron excluded*), Faraday-Lenz EMI, LCR series AC resonance ($Q$-factor), and Maxwell's displacement current. |
| **Optics & Modern Physics Theory** | Units 16--19: Ray Optics, Wave Optics, Dual Nature, Atoms, Nuclei, Semiconductors | [`chapters/physics/optics_modern_physics_theory.tex`](chapters/physics/optics_modern_physics_theory.tex) | [`chapters/physics/optics_modern_physics_theory.pdf`](chapters/physics/optics_modern_physics_theory.pdf) | Lens-maker's formula, prism minimum deviation ($A$-$\delta_m$), Young's double slit interference fringe width ($\beta=\lambda D/d$), single slit diffraction, Einstein photoelectric equation, de Broglie wavelength, Bohr hydrogen atom postulates & Rydberg formula, nuclear binding energy curve (*radioactivity excluded*), and p-n junction forward/reverse diode characteristics (*transistors excluded*). |
| **Experimental Physics Unit 20 Handbook** | Unit 20: 18 Prescribed Experimental Lab Skills | [`chapters/physics/experimental_physics_unit_20.tex`](chapters/physics/experimental_physics_unit_20.tex) | [`chapters/physics/experimental_physics_unit_20.pdf`](chapters/physics/experimental_physics_unit_20.pdf) | Complete protocols for all 18 NMC practicals: Vernier calipers, screw gauge, simple pendulum, downward force on incline, parallelogram law, Searle's apparatus, capillary rise, terminal velocity (Stokes), cooling curve, speed of sound (resonance tube), focal length of convex/concave lenses, prism deviation, diode V-I characteristics, and Zener reverse breakdown. |

---

## 3. Chemistry Master Theory, Reaction Mechanisms & Lab Manual Suite

Comprehensive master volumes covering all 20 units of the NEET UG 2027 Chemistry syllabus, encompassing Physical Chemistry mathematical formulations, Inorganic structural and coordination models, Organic electronic effects and reaction pathways, and Practical Qualitative & Quantitative Lab skills.

| Thematic Volume | NMC Units & Scope | LaTeX Source | Compiled PDF | Key Coverage & High-Yield Reaction Pathways |
| :--- | :--- | :--- | :--- | :--- |
| **Physical Chemistry Master Theory** | Units 1--8: Mole Concept, Atomic Structure, Thermodynamics, Equilibrium, Solutions, Electrochemistry, Kinetics | [`chapters/chemistry/physical_chemistry_master_theory.tex`](chapters/chemistry/physical_chemistry_master_theory.tex) | [`chapters/chemistry/physical_chemistry_master_theory.pdf`](chapters/chemistry/physical_chemistry_master_theory.pdf) | Stoichiometric limits, empirical/molecular formula, de Broglie duality, Heisenberg uncertainty, radial wavefunctions, First & Second Laws of Thermodynamics, Hess's law, Gibbs free energy ($\Delta G = \Delta H - T\Delta S$), Le Chatelier's principle, Henderson-Hasselbalch buffer calculations, salt hydrolysis & $K_{sp}$, Raoult's law vapor pressure depression, Nernst equation derivation, Kohlrausch's law, and Arrhenius activation energy. |
| **Inorganic Chemistry Master Compendium** | Units 9--12: Periodic Trends, Chemical Bonding, $d$-/$f$-Block, Coordination Chemistry | [`chapters/chemistry/inorganic_chemistry_master_compendium.tex`](chapters/chemistry/inorganic_chemistry_master_compendium.tex) | [`chapters/chemistry/inorganic_chemistry_master_compendium.pdf`](chapters/chemistry/inorganic_chemistry_master_compendium.pdf) | Periodic anomalies (lanthanoid contraction, ionization energy dips), Lewis structures, VSEPR geometries with lone-pair repulsion, Hybridization ($sp$ to $sp^3d^2$), MO diagrams ($B_2, C_2, N_2, O_2, O_2^+, O_2^-$), Crystal Field Theory splitting ($\Delta_o, \Delta_t$), CFSE calculations, Jahn-Teller distortions, optical/geometrical isomerism, and comparative $p$-block (Gr 13--18) and $d$-/$f$-block metallurgy-free chemistry. |
| **Organic Chemistry Master Theory** | Units 13--19: GOC, Hydrocarbons, Haloalkanes, Oxygen & Nitrogen Functions, Biomolecules | [`chapters/chemistry/organic_chemistry_master_theory.tex`](chapters/chemistry/organic_chemistry_master_theory.tex) | [`chapters/chemistry/organic_chemistry_master_theory.pdf`](chapters/chemistry/organic_chemistry_master_theory.pdf) | Electronic effects (inductive, resonance, hyperconjugation, Hückel $4n+2$ aromaticity), reactive intermediates (carbocations, carbanions, free radicals, carbenes), detailed mechanistic pathways for EAS, $S_N1/S_N2$, $E1/E2$, Markownikoff addition, Aldol condensation, Cannizzaro, Sandmeyer, Gabriel phthalimide, and biomolecules (monosaccharides, peptide bonds, DNA/RNA double helix). |
| **Organic Reaction Mechanisms Master Handbook** | Advanced Mechanistic Handbook across all Reaction Classes | [`chapters/chemistry/organic_reaction_mechanisms_handbook.tex`](chapters/chemistry/organic_reaction_mechanisms_handbook.tex) | [`chapters/chemistry/organic_reaction_mechanisms_handbook.pdf`](chapters/chemistry/organic_reaction_mechanisms_handbook.pdf) | Step-by-step arrow-pushing mechanisms: Electrophilic Aromatic Substitution (chlorination, nitration, sulfonation, Friedel-Crafts), nucleophilic substitution stereochemistry, alcohol dehydration pathways, nucleophilic carbonyl additions, Fischer esterification, HVZ reaction, Kolbe-Schmitt, Reimer-Tiemann, and complete decarboxylation pathways. |
| **Practical Chemistry Lab Manual** | Practical Qualitative Salt Analysis & Volumetric Redox Titrations | [`chapters/chemistry/practical_chemistry_lab_manual.tex`](chapters/chemistry/practical_chemistry_lab_manual.tex) | [`chapters/chemistry/practical_chemistry_lab_manual.pdf`](chapters/chemistry/practical_chemistry_lab_manual.pdf) | Systematic Anion analysis (Class I dilute $\mathrm{H_2SO_4}$, Class II conc $\mathrm{H_2SO_4}$, Class III precipitation), Cation Groups 0 through VI based on $K_{sp}$ and common-ion effect, confirmatory tests, and volumetric quantitative redox titrations ($\mathrm{KMnO_4}$ vs oxalic acid and Mohr's salt). |

---

## 4. End-to-End (E2E) Testing, Quality Verification & Syllabus Compliance Track

The repository enforces strict opaque-box software engineering standards for all LaTeX documents. Every single master module must pass a deterministic 7-gate verification engine prior to publication.

- **Master Test Harness:** [`scripts/validate_modules.py`](scripts/validate_modules.py)
- **Test Infrastructure Specification:** [`TEST_INFRA.md`](TEST_INFRA.md)
- **Readiness Attestation & Verification Audit:** [`TEST_READY.md`](TEST_READY.md)
- **Master Project Architectural Blueprint:** [`PROJECT.md`](PROJECT.md)

### The 7 Quality Gates

| Gate # | Gate Name | Verification Criteria | Status |
| :---: | :--- | :--- | :---: |
| **Gate 1** | Syntax & Environment Stack | LIFO nesting order across all `\begin{...}` and `\end{...}` pairs. Zero unclosed environments. | **100% PASS** |
| **Gate 2** | Non-Comment Curly Brace Parity | Exact match between opening `{` and closing `}` braces on non-comment lines. Escaped braces handled. | **100% PASS** |
| **Gate 3** | Front Banner Editorial Attribution | Mandatory presence of `Prepared, Compiled \& Authored by Satya Prakash` in title banner. | **100% PASS** |
| **Gate 4** | Running Header Attribution | Balanced-argument verification of `Satya Prakash` in `\fancyhead[R]` on all interior pages. | **100% PASS** |
| **Gate 5** | Semantic Callout Presence | Mandatory inclusion of all 5 custom semantic callouts (`conceptbox`, `formulabox`, `usecasebox`, `trapbox`, `ncertbox`). | **100% PASS** |
| **Gate 6** | Zero-Tolerance Deleted Syllabus Scanner | Rejects any positive presentation of deleted NMC topics (e.g., Carnot engine, Doppler effect, Potentiometer, Cyclotron, Transistors, Radioactivity; Solid state, Hydrogen, s-block, Metallurgy, Surface chemistry, Polymers). | **100% PASS** |
| **Gate 7** | Tectonic PDF Compilation Gate | Compiles source via `/home/spdedsec/.local/bin/tectonic` into a non-empty, publication-quality A4 PDF. | **100% PASS** |

---

## 5. Foundational Formula Handbooks & Biology Master Notes

In addition to the in-depth Master Theory Suite, the repository maintains high-yield quick revision formula handbooks and comprehensive Biology master notes covering Botany and Zoology.

| Category | Module Title | LaTeX Source | Compiled PDF | Key Highlights |
| :--- | :--- | :--- | :--- | :--- |
| **Syllabus** | Master Syllabus Blueprint | [`syllabus/neet_2027_master_syllabus.tex`](syllabus/neet_2027_master_syllabus.tex) | [`syllabus/neet_2027_master_syllabus.pdf`](syllabus/neet_2027_master_syllabus.pdf) | Exhaustive 50-unit breakdown (20 Physics, 20 Chemistry, 10 Biology), NMC deleted topics map, chapter weightage |
| **Physics Formulas** | Mechanics Core | [`formulas/physics/mechanics_core_formulas.tex`](formulas/physics/mechanics_core_formulas.tex) | [`formulas/physics/mechanics_core_formulas.pdf`](formulas/physics/mechanics_core_formulas.pdf) | Kinematics ($1\text{D}/2\text{D}$), Newton's Laws, Friction, Circular Motion, Work-Energy-Power, Collisions |
| **Physics Formulas** | Rotational, Gravitation, Thermal & Waves | [`formulas/physics/rotational_gravitation_thermal_shm_formulas.tex`](formulas/physics/rotational_gravitation_thermal_shm_formulas.tex) | [`formulas/physics/rotational_gravitation_thermal_shm_formulas.pdf`](formulas/physics/rotational_gravitation_thermal_shm_formulas.pdf) | Moment of Inertia, Rolling, Kepler's Laws, Fluid Dynamics, Thermodynamics, KTG, SHM, Doppler-excluded waves |
| **Physics Formulas** | Electrodynamics Core | [`formulas/physics/electrodynamics_core_formulas.tex`](formulas/physics/electrodynamics_core_formulas.tex) | [`formulas/physics/electrodynamics_core_formulas.pdf`](formulas/physics/electrodynamics_core_formulas.pdf) | Coulomb's law, Gauss's law, Dielectrics, Current electricity, Biot-Savart, Ampere's law, EMI, AC circuits, EM Waves |
| **Physics Formulas** | Optics & Modern Physics | [`formulas/physics/optics_modern_physics_formulas.tex`](formulas/physics/optics_modern_physics_formulas.tex) | [`formulas/physics/optics_modern_physics_formulas.pdf`](formulas/physics/optics_modern_physics_formulas.pdf) | Lens-Maker formula, Prism, Wave Optics (YDSE), Photoelectric effect, Bohr atom, Nuclear mass defect, Semiconductors |
| **Chemistry Formulas** | Physical Chemistry Core (Class 11) | [`formulas/chemistry/physical_chemistry_core_formulas.tex`](formulas/chemistry/physical_chemistry_core_formulas.tex) | [`formulas/chemistry/physical_chemistry_core_formulas.pdf`](formulas/chemistry/physical_chemistry_core_formulas.pdf) | Mole concept, Stoichiometry, Quantum numbers, Enthalpy/Entropy/Gibbs, $K_p/K_c$, Henderson-Hasselbalch, Solubility $K_{sp}$ |
| **Chemistry Formulas** | Solutions, Electrochemistry & Kinetics (Class 12) | [`formulas/chemistry/solutions_electrochemistry_kinetics_formulas.tex`](formulas/chemistry/solutions_electrochemistry_kinetics_formulas.tex) | [`formulas/chemistry/solutions_electrochemistry_kinetics_formulas.pdf`](formulas/chemistry/solutions_electrochemistry_kinetics_formulas.pdf) | Raoult's law, Colligative properties, van 't Hoff factor, Nernst equation, Kohlrausch's law, Integrated rate laws, Arrhenius equation |
| **Inorganic Chemistry** | Inorganic Chemistry Compendium | [`formulas/chemistry/inorganic_chemistry_compendium.tex`](formulas/chemistry/inorganic_chemistry_compendium.tex) | [`formulas/chemistry/inorganic_chemistry_compendium.pdf`](formulas/chemistry/inorganic_chemistry_compendium.pdf) | Periodic anomalies, VSEPR & hybridization geometries, Crystal Field Splitting ($\Delta_o, \Delta_t$), Isomerism, $d$-/$f$-block |
| **Organic Chemistry** | Named Reactions & Distinction Tests | [`formulas/chemistry/organic_chemistry_reactions.tex`](formulas/chemistry/organic_chemistry_reactions.tex) | [`formulas/chemistry/organic_chemistry_reactions.pdf`](formulas/chemistry/organic_chemistry_reactions.pdf) | GOC stability series, Hydrocarbon mechanisms, Aldol/Cannizzaro, Gabriel Phthalimide, Functional group test matrix |
| **Botany Notes** | Genetics & Molecular Basis | [`chapters/botany/genetics_and_molecular_basis.tex`](chapters/botany/genetics_and_molecular_basis.tex) | [`chapters/botany/genetics_and_molecular_basis.pdf`](chapters/botany/genetics_and_molecular_basis.pdf) | Mendelian genetics, Pedigree analysis, DNA replication, Transcription, Genetic code, Lac operon, HGP, DNA fingerprinting |
| **Botany Notes** | Plant Physiology Master Notes | [`chapters/botany/plant_physiology_master_notes.tex`](chapters/botany/plant_physiology_master_notes.tex) | [`chapters/botany/plant_physiology_master_notes.pdf`](chapters/botany/plant_physiology_master_notes.pdf) | Light reactions (Z-scheme), Calvin $C_3$ cycle, Hatch-Slack $C_4$ pathway, Photorespiration, Glycolysis, TCA cycle, ETS, PGRs |
| **Botany Notes** | Reproduction & Biotechnology | [`chapters/botany/reproduction_and_biotechnology.tex`](chapters/botany/reproduction_and_biotechnology.tex) | [`chapters/botany/reproduction_and_biotechnology.pdf`](chapters/botany/reproduction_and_biotechnology.pdf) | Micro/megasporogenesis, Double fertilization, Spermatogenesis/Oogenesis, Menstrual cycle, Contraceptives, r-DNA, PCR, Bt cotton |
| **Botany Notes** | Ecology & 7 NMC Plant Families | [`chapters/botany/ecology_diversity_and_families.tex`](chapters/botany/ecology_diversity_and_families.tex) | [`chapters/botany/ecology_diversity_and_families.pdf`](chapters/botany/ecology_diversity_and_families.pdf) | Population interactions, Trophic pyramids, Biodiversity latitudinal gradient, Floral formulas for Malvaceae, Compositae, Gramineae |
| **Zoology Notes** | Human Physiology Master Notes | [`chapters/zoology/human_physiology_master_notes.tex`](chapters/zoology/human_physiology_master_notes.tex) | [`chapters/zoology/human_physiology_master_notes.pdf`](chapters/zoology/human_physiology_master_notes.pdf) | Gas transport ($\mathrm{O_2-Hb}$ curve), Cardiac cycle & ECG, Counter-current mechanism & RAAS, Sliding filament theory, Nerve impulse |
| **Zoology Notes** | Cell Diversity & Animal Morphology | [`chapters/zoology/cell_diversity_and_animal_morphology.tex`](chapters/zoology/cell_diversity_and_animal_morphology.tex) | [`chapters/zoology/cell_diversity_and_animal_morphology.pdf`](chapters/zoology/cell_diversity_and_animal_morphology.pdf) | Endomembrane system, Enzyme kinetics ($K_m$, competitive/non-competitive inhibition), Meiosis phases, Cockroach & Frog morphology |
| **Zoology Notes** | Human Health, Immunology & Evolution | [`chapters/zoology/human_health_disease_and_evolution.tex`](chapters/zoology/human_health_disease_and_evolution.tex) | [`chapters/zoology/human_health_disease_and_evolution.pdf`](chapters/zoology/human_health_disease_and_evolution.pdf) | Innate & Acquired immunity, B/T-cells, Antibodies, AIDS/HIV, Cancer, Drugs/Alcohol abuse, Darwinian evolution, Hardy-Weinberg |

---

## 6. Styling & LaTeX Environment Framework

All documents in this repository import [`styles/neet_style.sty`](styles/neet_style.sty) and render using five breakable `tcolorbox` semantic callout environments:

- `\begin{conceptbox}[Title]` -- Fundamental scientific laws, underlying postulates, mechanisms, and structural pathways.
- `\begin{formulabox}[Title]` -- High-yield governing equations, vector forms, dimensional analysis, and SI units.
- `\begin{usecasebox}[Title]` -- Boundary conditions, domains of validity, approximations, and practical calculation shortcuts.
- `\begin{trapbox}[Title]` -- NEET exam traps, historical trick questions, subtle distinction errors, and sign convention traps.
- `\begin{ncertbox}[Title]` -- Direct NCERT line extractions, critical benchmark data, and official diagram cross-references.

---

## 7. Local Build & Verification Guide

### 1. Run Automated E2E Quality Verification
To run the automated 7-gate verification engine on the Master Theory Suite:
```bash
# Fast lint & syntax verification (Gates 1-6 across all modules)
python3 scripts/validate_modules.py --all --skip-compile

# Full 7-Gate verification including live Tectonic PDF compilation
python3 scripts/validate_modules.py chapters/physics/mechanics_master_theory.tex
```

### 2. Compile LaTeX Modules via Tectonic
Any LaTeX module can be individually compiled using the high-performance modern TeX engine:
```bash
tectonic chapters/physics/mechanics_master_theory.tex
tectonic chapters/chemistry/physical_chemistry_master_theory.tex
tectonic chapters/chemistry/organic_reaction_mechanisms_handbook.tex
```

### 3. Batch Compilation of Entire Repository
To batch-compile all modules across the repository:
```bash
./scripts/compile_all.sh
```
