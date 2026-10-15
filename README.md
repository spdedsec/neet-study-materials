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

## 2. NEET UG Master Textbooks

The repository features three comprehensive, unabridged master textbook volumes engineered for professional print-on-demand publication (Paperback and Hardcover) and high-intensity self-study, located in the dedicated [`books/`](books/) directory. Authored by **Satya Prakash**, each volume features an academic two-sided book layout, complete publishing front matter (Half-Title, Title page, Copyright with editorial contact `spdedsec@hotmail.com`, Dedication, Acknowledgements, Author's Preface, Syllabus Blueprint, and auto-generated Table of Contents), discrete running headers, clean chapter openings with zero repetitive banners, and personal conversational mentor notes on learning psychology, memory consolidation, knowing when to stop, and error analysis.

### Master Book Series Overview

| Volume Title | Scope & Curriculum Architecture | LaTeX Manuscript | Compiled PDF | Verified Metrics |
| :--- | :--- | :--- | :--- | :---: |
| **Volume 1: NEET UG Physics Master Book** | Parts I–VI + Appendix: Mechanics, Rotational Dynamics, Gravitation, Fluids, Heat, Thermodynamics, Waves, Electrodynamics, Optics, Modern Physics, all 18 NMC Lab Practicals & High-Yield Formulas | [`books/physics_master_book.tex`](books/physics_master_book.tex) | [`books/physics_master_book.pdf`](books/physics_master_book.pdf) | **147 Pages** (851 KB) |
| **Volume 2: NEET UG Chemistry Master Book** | Parts I–VI + Appendix: Physical Chemistry Foundations, Advanced Solutions/Electro/Kinetics, Inorganic Bonding/CFT, Organic Theory, Reaction Mechanisms Handbook, Qualitative Lab Manual & Formulas | [`books/chemistry_master_book.tex`](books/chemistry_master_book.tex) | [`books/chemistry_master_book.pdf`](books/chemistry_master_book.pdf) | **171 Pages** (997 KB) |
| **Volume 3: NEET UG Biology Master Book** | Parts I–VII + Appendix: Cell Biology, Structural Diversity, 7 NMC Plant Families, Comparative Anatomy (Frog/Cockroach), Plant & Human Physiology, Reproduction, Genetics, Ecology & Quantitative Diagnostics | [`books/biology_master_book.tex`](books/biology_master_book.tex) | [`books/biology_master_book.pdf`](books/biology_master_book.pdf) | **103 Pages** (510 KB) |

---

### Detailed Volume Architectural Specifications

#### Volume 1: NEET UG Physics Master Book (147 Pages)
- **LaTeX Source:** [`books/physics_master_book.tex`](books/physics_master_book.tex) | **Compiled PDF:** [`books/physics_master_book.pdf`](books/physics_master_book.pdf)
- **Curriculum Architecture (Parts I–VI + Appendix):**
  - **Part I: Classical Mechanics & Dynamics:** Kinematics ($1\text{D}/2\text{D}$ calculus, projectile trajectories, relative velocity), Newton's Laws with constrained pulley dynamics, static and kinetic friction, circular motion banking, Work-Energy Theorem, variable mass rocket systems, and 1D/2D oblique collisions.
  - **Part II: Rotational Mechanics, Gravitation & Continuum Mechanics:** Centre of mass integrals, parallel and perpendicular axis theorems, moment of inertia derivations, rolling without slipping dynamics on inclines, Kepler's three planetary laws, gravitational potential integration, Hooke's elasticity, Pascal's principle, surface tension capillary rise, Bernoulli's theorem, and Stokes' law.
  - **Part III: Thermal Physics, Thermodynamics & Waves:** Thermal expansion, calorimetry, Stefan-Boltzmann and Wien's displacement laws, First Law of Thermodynamics ($dQ = dU + dW$), Mayer's relation ($C_p - C_v = R$), Second Law (Kelvin-Planck and Clausius formulations; *Carnot engine strictly excluded*), Kinetic Theory of Gases molecular derivations ($P = \frac{1}{3}\rho v_{rms}^2$), degrees of freedom, SHM phasor analysis, coupled oscillations, and standing waves in strings/pipes (*Doppler effect strictly excluded*).
  - **Part IV: Electrodynamics & Magnetism:** Coulomb's law in vector form, Gauss's law boundary applications, capacitor dielectrics and electrostatic energy density, drift velocity, microscopic Ohm's law, Kirchhoff's loop rules (*potentiometer strictly excluded*), Biot-Savart and Ampere's circuital laws (*cyclotron strictly excluded*), Faraday-Lenz EMI, series LCR AC resonance ($Q$-factor), and Maxwell's displacement current.
  - **Part V: Optics & Modern Physics:** Lens-maker's formula, prism minimum deviation ($A$-$\delta_m$), Young's double slit interference fringe width ($\beta = \lambda D/d$), single slit diffraction, Einstein photoelectric equation, de Broglie matter waves, Bohr hydrogen atom postulates and Rydberg formula, nuclear mass defect and binding energy curve (*radioactivity strictly excluded*), and semiconductor p-n junction diode forward/reverse characteristics (*transistors strictly excluded*).
  - **Part VI: Experimental Physics & Laboratory Skills:** Complete experimental protocols, apparatus schematics, error analysis, and observation tables for all **18 NMC prescribed practicals** (Vernier calipers, screw gauge, simple pendulum, downward force on incline, parallelogram law, Searle's apparatus, capillary rise, terminal velocity, cooling curve, resonance tube speed of sound, convex/concave lens focal length, prism deviation, meter bridge, and p-n diode characteristics).
  - **Appendix: High-Yield Physics Formula & Equation Compendium:** Comprehensive formula matrices and dimension tables covering mechanics, thermal physics, electromagnetism, optics, and modern physics.
- **Syllabus Exclusions:** 100% strictly aligned with the revised NMC syllabus; zero deleted topics presented as active curriculum.

#### Volume 2: NEET UG Chemistry Master Book (171 Pages)
- **LaTeX Source:** [`books/chemistry_master_book.tex`](books/chemistry_master_book.tex) | **Compiled PDF:** [`books/chemistry_master_book.pdf`](books/chemistry_master_book.pdf)
- **Curriculum Architecture (Parts I–VI + Appendix):**
  - **Part I: Physical Chemistry Foundations:** Mole concept, stoichiometric balancing, atomic structure and quantum mechanics (de Broglie hypothesis, Heisenberg uncertainty principle, radial wavefunctions, quantum numbers), Chemical Thermodynamics derivations (First and Second Laws, Hess's law, Gibbs free energy $\Delta G = \Delta H - T\Delta S$), and Chemical & Ionic Equilibrium (Le Chatelier's principle, Henderson-Hasselbalch buffer calculations, salt hydrolysis, and solubility product $K_{sp}$).
  - **Part II: Advanced Physical Chemistry:** Solutions and Colligative Properties (Raoult's law thermodynamics, boiling point elevation, freezing point depression, osmotic pressure, van 't Hoff factor $i$), Electrochemistry (Nernst equation derivation, standard electrode potentials, Kohlrausch's law of independent migration of ions), and Chemical Kinetics (integrated rate equations for 0th and 1st order reactions, pseudo-first-order kinetics, Arrhenius equation and collision theory).
  - **Part III: Inorganic Chemistry & Coordination Compounds:** Periodic trends and electronic anomalies (lanthanoid contraction, ionization energy variations), Chemical Bonding (Lewis structures, VSEPR geometries with lone-pair repulsions, Hybridization from $sp$ to $sp^3d^2$, Molecular Orbital Energy Level diagrams for $B_2, C_2, N_2, O_2, O_2^+, O_2^-$), Coordination Chemistry (Werner's coordination theory, Crystal Field Theory splitting diagrams for octahedral $\Delta_o$ and tetrahedral $\Delta_t$ complexes, CFSE calculations, high-spin/low-spin states, Jahn-Teller distortion basics, optical and geometrical isomerism), and comparative $p$-block (Groups 13–18) and $d$-/$f$-block elements (*extractive metallurgy strictly excluded*).
  - **Part IV: Organic Chemistry: Principles, Pathways & Biomolecules:** Electronic effects (inductive, resonance, hyperconjugation, Hückel $4n+2$ aromaticity rule), Reactive intermediates (carbocations, carbanions, carbon free radicals, carbenes), Hydrocarbons, Haloalkanes and Haloarenes, Oxygen and Nitrogen functional groups (alcohols, phenols, ethers, aldehydes, ketones, carboxylic acids, amines, diazonium salts), and Biomolecules (monosaccharides, peptide bonds, protein secondary/tertiary structures, DNA/RNA double helix).
  - **Part V: Organic Reaction Mechanisms Handbook:** Step-by-step arrow-pushing mechanisms across all major reaction classes: Electrophilic Aromatic Substitution (chlorination, nitration, sulfonation, Friedel-Crafts alkylation/acylation), Nucleophilic Aliphatic Substitution ($S_N1$ and $S_N2$ stereochemical inversions), Elimination reactions ($E1$ and $E2$ Saytzeff vs Hofmann regioselectivity), Aldol condensation, Cannizzaro disproportionation, Decarboxylation pathways, Kolbe-Schmitt reaction, Reimer-Tiemann formylation, and Diazotization with Sandmeyer substitution.
  - **Part VI: Practical Chemistry & Qualitative Analysis Lab Manual:** Systematic Anion analysis (Class I dilute $\mathrm{H_2SO_4}$, Class II conc $\mathrm{H_2SO_4}$, Class III precipitation tests), Systematic Cation Group Analysis (Groups 0 through VI separated by $K_{sp}$ thresholds and common-ion effect), confirmatory tests, and volumetric quantitative redox titrations ($\mathrm{KMnO_4}$ vs oxalic acid and Mohr's salt).
  - **Appendix: Comprehensive Chemistry Formula, Named Reaction & Reagent Matrices:** Complete reference matrices for thermodynamics, kinetics, electrochemistry, named organic transformations, and synthetic reagent profiles.
- **Syllabus Exclusions:** 100% strictly aligned with the revised NMC syllabus; zero deleted topics (Solid state, States of matter, Hydrogen, s-block, Metallurgy, Surface chemistry, Polymers, and Chemistry in everyday life strictly excluded).

#### Volume 3: NEET UG Biology Master Book (103 Pages)
- **LaTeX Source:** [`books/biology_master_book.tex`](books/biology_master_book.tex) | **Compiled PDF:** [`books/biology_master_book.pdf`](books/biology_master_book.pdf)
- **Curriculum Architecture (Parts I–VII + Appendix):**
  - **Part I: Cell Biology, Biomolecules & Cell Division:** Cell theory, prokaryotic vs eukaryotic ultrastructure, endomembrane system, enzyme kinetics (Michaelis-Menten kinetics, $K_m$, competitive and non-competitive enzyme inhibition), Cell cycle phases ($G_1, S, G_2, M$), mitotic stages, and meiotic recombination (pachytene crossing over, synaptonemal complex).
  - **Part II: Structural Organisation & Diversity:** Plant morphology (root, stem, leaf modifications, inflorescence, flower anatomy), floral formulas, floral diagrams, and systematic diagnostic keys for **all 7 NMC prescribed plant families** (Fabaceae, Solanaceae, Liliaceae, Brassicaceae, Poaceae, Malvaceae, and Asteraceae), Animal Kingdom taxonomic hierarchy, and detailed comparative morphology and organ-system anatomy of the Frog (*Rana tigrina*) and Cockroach (*Periplaneta americana*).
  - **Part III: Plant Physiology:** Photosynthesis in higher plants (photochemical light reactions, Z-scheme, photophosphorylation, Calvin $C_3$ cycle, Hatch-Slack $C_4$ pathway, CAM pathway, photorespiration), Cellular respiration in plants (glycolysis, oxidative decarboxylation, Krebs TCA cycle, Electron Transport System, chemiosmotic ATP synthesis, respiratory quotients), and Plant Growth Regulators (auxins, gibberellins, cytokinins, ethylene, abscisic acid).
  - **Part IV: Human Physiology:** Complete physiological systems: Breathing and exchange of gases ($\mathrm{O_2}$-$\mathrm{Hb}$ dissociation curve, Bohr effect), Body fluids and circulation (cardiac cycle, ECG waves, double circulation, blood pressure regulation), Excretory products and elimination (nephron function, counter-current multiplier, RAAS feedback loop), Locomotion and movement (sliding filament theory of muscle contraction, human skeletal system), Neural control and coordination (action potential generation and saltatory conduction, reflex arc), and Chemical coordination and integration (endocrine axes, hormone-receptor interactions).
  - **Part V: Reproduction & Reproductive Health:** Sexual reproduction in flowering plants (microsporogenesis, megasporogenesis, pollen-pistil interaction, double fertilization, endosperm development), Human reproduction (male and female reproductive systems, spermatogenesis, oogenesis, hormonal menstrual cycle regulation, fertilization, cleavage, implantation, placenta formation, parturition, lactation), and Reproductive Health (contraceptive methodologies, sexually transmitted infections, and Assisted Reproductive Technologies [IVF, ET, ZIFT, GIFT, ICSI, IUI]).
  - **Part VI: Genetics & Molecular Biology:** Principles of Inheritance and Variation (Mendelian ratios, incomplete dominance, codominance, multiple alleles, chromosomal theory of inheritance, sex linkage, pedigree analysis, chromosomal and gene disorders), Molecular Basis of Inheritance (DNA structure, double helix topology, packaging in nucleosomes, Meselson-Stahl experiment, DNA replication fork, transcription, genetic code universality and degeneracy, translation, Lac operon prokaryotic regulation, Human Genome Project, and DNA fingerprinting).
  - **Part VII: Biotechnology, Human Health & Ecology:** Biotechnology Principles & Processes (restriction endonucleases, plasmid vectors, agarose gel electrophoresis, PCR thermal cycling, recombinant DNA technology, stirred-tank bioreactors, downstream processing), Biotechnology Applications in agriculture and medicine ($Bt$ crops, RNA interference, recombinant human insulin, gene therapy, transgenic animals), Human Health & Disease (pathogens, life cycle of *Plasmodium*, innate and acquired immunity, humoral and cell-mediated responses, antibodies, AIDS pathogenesis, cancer biology), Evolution (evidence, Lamarckism, Darwinian natural selection, Modern Synthetic Theory, Hardy-Weinberg equilibrium, adaptive radiation), and Ecology (organisms and populations, population growth models, ecosystem trophic structures, ecological pyramids, nutrient cycling, biodiversity gradients, and in-situ/ex-situ conservation strategies).
  - **Appendix: High-Yield Quantitative Biology & Master Diagnostic Matrices:** Chapter 16 high-yield compendium containing numerical genetic ratios, physiological reference ranges, taxonomic classification matrices, and comparative floral formula charts.
- **Syllabus Inclusions & Compliance:** Fully integrated with the rationalized NMC biology curriculum, highlighting all newly emphasized plant families and practical organismal dissections.

---

### Publication-Grade Master Book Typesetting Architecture & Design System

The master book series is built on a custom, professional book publishing framework defined in [`styles/neet_book.sty`](styles/neet_book.sty) (architectural specification: `styles/neet_book_style.sty`). Designed specifically for professional two-sided print-on-demand requirements, this system enforces publication-grade academic standards across all three volumes:

1. **Two-Sided Academic Book Layout & Geometry:**
   - Document class: `\documentclass[10pt,twoside,openright]{book}`.
   - Geometry parameters via `geometry`:
     ```latex
     \RequirePackage[
       a4paper,
       top=2.2cm,
       bottom=2.2cm,
       inner=2.4cm,
       outer=2.0cm,
       headheight=24pt,
       headsep=14pt,
       footskip=16pt,
       twoside,
       bindingoffset=4mm
     ]{geometry}
     ```
   - Total inner gutter of 2.8 cm ensures comfortable readability when bound in paperback or hardcover without spine-pinch or equation clipping.
   - Even (verso) and odd (recto) pages mirror margins and headers correctly, adhering to trade and academic publishing guidelines.

2. **Standard Academic Publishing Front Matter:**
   Each master book incorporates a complete, standard publishing front matter sequence structured with `\frontmatter`:
   - **Half-Title Page:** Clean, minimalist presentation of the book title and master reference series designation.
   - **Full Title Page:** Complete title, subtitle (*"Complete Master Theory, Formulas & Experimental Compendium strictly aligned with NEET UG 2027 NMC Syllabus"*), author declaration (*Authored by Satya Prakash*), syllabus calibration statement, and examination target.
   - **Professional Copyright Page:** Copyright declaration (All Rights Reserved © 2026–2027 Satya Prakash), author contact and editorial feedback email (`spdedsec@hotmail.com`), repository errata link, First Edition October 2026 notice, publishing imprint details, ISBN-13 placeholders for Paperback and Hardcover editions, printing location notices, and an exhaustive medical entrance examination academic and legal disclaimer.
   - **Dedication Page:** Dignified, personal tribute to parents, mentors, and aspirants preparing in the quiet hours of the night.
   - **Acknowledgements:** Sincere recognition of family, physics/chemistry/biology educators, student peer study circles, and the open-source $\mathrm{\LaTeX}$ and Tectonic engineering communities.
   - **Author's Preface:** Scholarly, pedagogical orientation to the NEET UG rationalized curriculum, analytical first-principles thinking, learning psychology, active recall, and error log analysis (strictly free of promotional filler, AI buzzwords, or ungrounded claims).
   - **Syllabus Blueprint & NMC Rationalization Guide:** Examination architecture, question counts (45 compulsory per subject, 180 total), mark allocations, time pacing budgets, and an explicit breakdown of deleted NMC topics to prevent wasted study effort.
   - **Table of Contents (`\tableofcontents`):** Auto-generated two-level TOC (`tocdepth=2`, `secnumdepth=2`) featuring styled dot leaders, distinct Part division banners, and exact page references.

3. **Clean Chapter Openings (Zero Banner Duplication):**
   - In contrast to modular single-chapter notes, the master book series completely eliminates repeated front banners and author boxes at the start of individual chapters.
   - Chapter titles are typeset cleanly using `titlesec`:
     ```latex
     \titleformat{\chapter}[display]
       {\normalfont\huge\bfseries\color{primarydark}}
       {\Large\bfseries\color{accentblue}\chaptertitlename\ \thechapter}
       {6pt}
       {\Huge}
       [{\color{accentblue}\vspace{6pt}\titlerule[1.5pt]}]
     ```
   - Each chapter opens cleanly on a new recto (odd) page (`openright`), followed immediately by core theoretical exposition and derivations.

4. **Running Headers & Footers (`fancyhdr`):**
   - **Verso (Even / Left Pages):**
     - Header: Outer bold page number (`\fancyhead[LE]`) and Master Reference Series title (`\fancyhead[RE]`).
     - Footer: Author attribution and correspondence (`Authored by Satya Prakash · spdedsec@hotmail.com`).
   - **Recto (Odd / Right Pages):**
     - Header: Current chapter/section title (`\fancyhead[LO]`) and outer bold page number (`\fancyhead[RO]`).
     - Footer: Series edition identifier (`Master Reference Edition · Strictly NMC Calibrated`).
   - **Blank Page Suppression:** Patched `\cleardoublepage` ensures that blank transition pages generated by `openright` completely suppress running headers and footers (`\thispagestyle{empty}`).
   - **Chapter Opening Pages:** Uses `\fancypagestyle{plain}` to suppress top running headers while retaining a clean centered page number in the footer.

5. **Frontmatter and Mainmatter Paging Strategy:**
   - `\frontmatter`: Numbered in lowercase Roman numerals (`i`, `ii`, `iii`, ...) for half-title, copyright, preface, and table of contents.
   - `\mainmatter`: Page numbering resets to Arabic numeral `1` starting on the recto page of Part I, maintaining clean continuity throughout all core chapters, practicals, and appendixes.

6. **Semantic Callout Box Environments (`tcolorbox`):**
   The book package preserves full compatibility with all semantic learning environments, styled with professional publishing palettes:
   - `\begin{conceptbox}[Title]` — Theoretical foundations, fundamental scientific postulates, and structural mechanisms (Deep Navy: `#0F2240`).
   - `\begin{formulabox}[Title]` — Governing mathematical equations, limits, variables, and SI units (Formula Blue: `#1746A2`).
   - `\begin{usecasebox}[Title]` — Real-world application regimes, valid boundary conditions, and calculation shortcuts (Forest Green: `#146C43`).
   - `\begin{trapbox}[Title]` — NEET examination traps, historical trick questions, subtle distinction errors, and sign pitfalls (Crimson Red: `#BA181B`).
   - `\begin{ncertbox}[Title]` — Direct verbatim NCERT lines, critical data tables, and official diagram cross-references (NCERT Amber: `#B45309`).
   - `\begin{mentorbox}[Title]` — Personal advice, exam mindset, sleep consolidation, and active recall strategies from Satya Prakash (Royal Purple: `#6D28D9`).
   - `\begin{studytipbox}[Title]` — High-yield tactical shortcuts and rapid problem-solving heuristics (Mint Teal: `#0D9488`).

---

## 3. Physics Master Theory & Experimental Practicals Suite

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

## 4. Chemistry Master Theory, Reaction Mechanisms & Lab Manual Suite

Comprehensive master volumes covering all 20 units of the NEET UG 2027 Chemistry syllabus, encompassing Physical Chemistry mathematical formulations, Inorganic structural and coordination models, Organic electronic effects and reaction pathways, and Practical Qualitative & Quantitative Lab skills.

| Thematic Volume | NMC Units & Scope | LaTeX Source | Compiled PDF | Key Coverage & High-Yield Reaction Pathways |
| :--- | :--- | :--- | :--- | :--- |
| **Physical Chemistry Master Theory** | Units 1--8: Mole Concept, Atomic Structure, Thermodynamics, Equilibrium, Solutions, Electrochemistry, Kinetics | [`chapters/chemistry/physical_chemistry_master_theory.tex`](chapters/chemistry/physical_chemistry_master_theory.tex) | [`chapters/chemistry/physical_chemistry_master_theory.pdf`](chapters/chemistry/physical_chemistry_master_theory.pdf) | Stoichiometric limits, empirical/molecular formula, de Broglie duality, Heisenberg uncertainty, radial wavefunctions, First & Second Laws of Thermodynamics, Hess's law, Gibbs free energy ($\Delta G = \Delta H - T\Delta S$), Le Chatelier's principle, Henderson-Hasselbalch buffer calculations, salt hydrolysis & $K_{sp}$, Raoult's law vapor pressure depression, Nernst equation derivation, Kohlrausch's law, and Arrhenius activation energy. |
| **Inorganic Chemistry Master Compendium** | Units 9--12: Periodic Trends, Chemical Bonding, $d$-/$f$-Block, Coordination Chemistry | [`chapters/chemistry/inorganic_chemistry_master_compendium.tex`](chapters/chemistry/inorganic_chemistry_master_compendium.tex) | [`chapters/chemistry/inorganic_chemistry_master_compendium.pdf`](chapters/chemistry/inorganic_chemistry_master_compendium.pdf) | Periodic anomalies (lanthanoid contraction, ionization energy dips), Lewis structures, VSEPR geometries with lone-pair repulsion, Hybridization ($sp$ to $sp^3d^2$), MO diagrams ($B_2, C_2, N_2, O_2, O_2^+, O_2^-$), Crystal Field Theory splitting ($\Delta_o, \Delta_t$), CFSE calculations, Jahn-Teller distortions, optical/geometrical isomerism, and comparative $p$-block (Gr 13--18) and $d$-/$f$-block metallurgy-free chemistry. |
| **Organic Chemistry Master Theory** | Units 13--19: GOC, Hydrocarbons, Haloalkanes, Oxygen & Nitrogen Functions, Biomolecules | [`chapters/chemistry/organic_chemistry_master_theory.tex`](chapters/chemistry/organic_chemistry_master_theory.tex) | [`chapters/chemistry/organic_chemistry_master_theory.pdf`](chapters/chemistry/organic_chemistry_master_theory.pdf) | Electronic effects (inductive, resonance, hyperconjugation, Hückel $4n+2$ aromaticity), reactive intermediates (carbocations, carbanions, free radicals, carbenes), detailed mechanistic pathways for EAS, $S_N1/S_N2$, $E1/E2$, Markownikoff addition, Aldol condensation, Cannizzaro, Sandmeyer, Gabriel phthalimide, and biomolecules (monosaccharides, peptide bonds, DNA/RNA double helix). |
| **Organic Reaction Mechanisms Master Handbook** | Advanced Mechanistic Handbook across all Reaction Classes | [`chapters/chemistry/organic_reaction_mechanisms_handbook.tex`](chapters/chemistry/organic_reaction_mechanisms_handbook.tex) | [`chapters/chemistry/organic_reaction_mechanisms_handbook.pdf`](chapters/chemistry/organic_reaction_mechanisms_handbook.pdf) | Step-by-step arrow-pushing mechanisms: Electrophilic Aromatic Substitution (chlorination, nitration, sulfonation, Friedel-Crafts), nucleophilic substitution stereochemistry, alcohol dehydration pathways, nucleophilic carbonyl additions, Fischer esterification, HVZ reaction, Kolbe-Schmitt, Reimer-Tiemann, and complete decarboxylation pathways. |
| **Practical Chemistry Lab Manual** | Practical Qualitative Salt Analysis & Volumetric Redox Titrations | [`chapters/chemistry/practical_chemistry_lab_manual.tex`](chapters/chemistry/practical_chemistry_lab_manual.tex) | [`chapters/chemistry/practical_chemistry_lab_manual.pdf`](chapters/chemistry/practical_chemistry_lab_manual.pdf) | Systematic Anion analysis (Class I dilute $\mathrm{H_2SO_4}$, Class II conc $\mathrm{H_2SO_4}$, Class III precipitation), Cation Groups 0 through VI based on $K_{sp}$ and common-ion effect, confirmatory tests, and volumetric quantitative redox titrations ($\mathrm{KMnO_4}$ vs oxalic acid and Mohr's salt). |

---

## 5. End-to-End (E2E) Testing, Quality Verification & Syllabus Compliance Track

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

## 6. Foundational Formula Handbooks & Biology Master Notes

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

## 7. Styling & LaTeX Environment Framework

All documents in this repository import [`styles/neet_style.sty`](styles/neet_style.sty) or [`styles/neet_book.sty`](styles/neet_book.sty) and render using custom breakable `tcolorbox` semantic callout environments:

- `\begin{conceptbox}[Title]` -- Fundamental scientific laws, underlying postulates, mechanisms, and structural pathways.
- `\begin{formulabox}[Title]` -- High-yield governing equations, vector forms, dimensional analysis, and SI units.
- `\begin{usecasebox}[Title]` -- Boundary conditions, domains of validity, approximations, and practical calculation shortcuts.
- `\begin{trapbox}[Title]` -- NEET exam traps, historical trick questions, subtle distinction errors, and sign convention traps.
- `\begin{ncertbox}[Title]` -- Direct NCERT line extractions, critical benchmark data, and official diagram cross-references.
- `\begin{mentorbox}[Title]` -- Personal wisdom, study strategy, memory consolidation, and psychological endurance notes from Satya Prakash.
- `\begin{studytipbox}[Title]` -- High-yield tactical shortcuts and examination problem-solving techniques.

---

## 8. Local Build & Verification Guide

### 1. Run Automated E2E Quality Verification
To run the automated 7-gate verification engine on the Master Theory Suite:
```bash
# Fast lint & syntax verification (Gates 1-6 across all modules)
python3 scripts/validate_modules.py --all --skip-compile

# Full 7-Gate verification including live Tectonic PDF compilation
python3 scripts/validate_modules.py chapters/physics/mechanics_master_theory.tex

# Validate Master Textbook syntax & environment nesting
python3 scripts/validate_latex.py books/physics_master_book.tex
python3 scripts/validate_latex.py books/chemistry_master_book.tex
python3 scripts/validate_latex.py books/biology_master_book.tex
```

### 2. Compile LaTeX Modules & Master Books via Tectonic
Any LaTeX module or master textbook can be individually compiled using the high-performance modern TeX engine:
```bash
# Compile Master Theory Chapters
tectonic chapters/physics/mechanics_master_theory.tex
tectonic chapters/chemistry/physical_chemistry_master_theory.tex
tectonic chapters/chemistry/organic_reaction_mechanisms_handbook.tex

# Compile Complete Master Textbooks
tectonic books/physics_master_book.tex
tectonic books/chemistry_master_book.tex
tectonic books/biology_master_book.tex
```

### 3. Batch Compilation of Entire Repository
To batch-compile all modules across the repository:
```bash
./scripts/compile_all.sh
```
