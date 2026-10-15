#!/usr/bin/env python3
"""
scripts/build_books.py - Master Book Generation & Compilation Automation Suite
Strictly calibrated for comprehensive print-on-demand publishing standards.
Author: Satya Prakash <spdedsec@hotmail.com>
Repository: https://github.com/spdedsec/neet-study-materials
Target: NEET UG 2027 Examination Cycle
"""

import os
import re
import sys
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
BOOKS_DIR = ROOT_DIR / "books"
COMPILER = "/home/spdedsec/.local/bin/tectonic"


def extract_body(rel_path: str) -> str:
    """Extract academic body from a chapter or formula .tex file.
    Strips document preamble, packages, pagestyle, and title banners.
    Returns clean LaTeX content starting from the first \\section to \\end{document}.
    """
    full_path = ROOT_DIR / rel_path
    if not full_path.exists():
        raise FileNotFoundError(f"File not found: {full_path}")

    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    sec_idx = content.find(r"\section")
    if sec_idx == -1:
        raise ValueError(f"No \\section found in {rel_path}")

    end_idx = content.rfind(r"\end{document}")
    if end_idx == -1:
        body = content[sec_idx:]
    else:
        body = content[sec_idx:end_idx]

    return body.strip()


def build_physics_book() -> str:
    """Assemble the complete manuscript for Physics Master Textbook."""
    
    # Extract source chapters
    b_mechanics = extract_body("chapters/physics/mechanics_master_theory.tex")
    b_rot_grav = extract_body("chapters/physics/rotational_gravitation_fluids_theory.tex")
    b_thermal = extract_body("chapters/physics/thermal_physics_oscillations_theory.tex")
    b_electro = extract_body("chapters/physics/electrodynamics_master_theory.tex")
    b_optics_mod = extract_body("chapters/physics/optics_modern_physics_theory.tex")
    b_unit20 = extract_body("chapters/physics/experimental_physics_unit_20.tex")
    
    # Extract formula modules
    f_mech = extract_body("formulas/physics/mechanics_core_formulas.tex")
    f_rot_therm = extract_body("formulas/physics/rotational_gravitation_thermal_shm_formulas.tex")
    f_electro = extract_body("formulas/physics/electrodynamics_core_formulas.tex")
    f_optics = extract_body("formulas/physics/optics_modern_physics_formulas.tex")

    tex = r"""\documentclass[10pt,twoside,openright]{book}
\usepackage{../styles/neet_book}

\begin{document}

% =========================================================================
% FRONT MATTER
% =========================================================================
\frontmatter

% --- Half-Title Page ---
\thispagestyle{empty}
\vspace*{4cm}
\begin{center}
  {\Huge\bfseries\color{primarydark} NEET UG PHYSICS}\\[0.6cm]
  {\Large\bfseries\color{accentblue} MASTER TEXTBOOK}\\[1.5cm]
  {\normalsize\color{gray} NEET UG 2027 Master Reference Series $\cdot$ Authoritative KDP Edition}
\end{center}
\cleardoublepage

% --- Full Title Page ---
\thispagestyle{empty}
\vspace*{2cm}
\begin{center}
  {\Huge\bfseries\color{primarydark} NEET UG PHYSICS}\\[0.4cm]
  {\LARGE\bfseries\color{primarydark} MASTER TEXTBOOK}\\[0.8cm]
  {\Large\bfseries\color{accentblue} Mechanics, Thermodynamics, Electrodynamics, Optics,}\\[0.2cm]
  {\Large\bfseries\color{accentblue} Modern Physics, Experimental Skills \& High-Yield Formulas}\\[2cm]
  
  {\large\textbf{Authored by}}\\[0.3cm]
  {\LARGE\bfseries\color{primarydark} Satya Prakash}\\[1.5cm]

  {\normalsize\textbf{Strictly Calibrated to the Revised NMC Syllabus \& Rationalized NCERT Textbooks}}\\[0.3cm]
  {\small Target Examination: National Eligibility cum Entrance Test (NEET UG 2027)}\\[2.5cm]

  {\footnotesize Published for Independent Medical Aspirants, Educators \& Academic Study Circles}\\[0.2cm]
  {\footnotesize Print-on-Demand $\cdot$ Amazon KDP Distribution}
\end{center}
\cleardoublepage

% --- Professional Copyright Page ---
\thispagestyle{empty}
\vspace*{\fill}
\begin{flushleft}
{\small
\textbf{NEET UG PHYSICS MASTER TEXTBOOK}\\[2pt]
\textit{Comprehensive Theory, Rigorous Derivations, Experimental Skills \& Formula Compendium}\\[8pt]
\textbf{Author:} Satya Prakash\\
\textbf{Editorial Correspondence \& Academic Feedback:} \href{mailto:spdedsec@hotmail.com}{spdedsec@hotmail.com}\\
\textbf{Source Repository \& Official Errata:} \url{https://github.com/spdedsec/neet-study-materials}\\[10pt]

\copyright\ 2026--2027 Satya Prakash. All rights reserved.\\[8pt]

\textbf{First Edition:} October 2026\\
\textbf{Publishing Imprint:} Independent Academic Publishing / Amazon Kindle Direct Publishing (KDP)\\
\textbf{Target Cycle:} NEET UG 2027 (Undergraduate Medical Admissions Entrance Examination)\\
\textbf{ISBN-13 (Paperback):} 979-8-XXXXXXXXX (Placeholder for KDP Assigned ISBN)\\
\textbf{ISBN-13 (Hardcover):} 979-8-XXXXXXXXX (Placeholder for KDP Assigned ISBN)\\[10pt]

\textbf{All Rights Reserved.} No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any form or by any means---electronic, mechanical, photocopying, recording, scanning, or otherwise---without the prior written permission of the author, except for brief quotations embodied in critical reviews or scholarly analysis as permitted under copyright law.\\[8pt]

\textbf{Academic \& Legal Disclaimer:} This textbook is an independent preparation manual authored by Satya Prakash to assist candidates preparing for the National Eligibility cum Entrance Test (NEET UG). While every effort has been made to verify scientific accuracy and strict concordance with the National Medical Commission (NMC) curriculum and rationalized NCERT textbooks, the author and publisher make no official claims of affiliation with or endorsement by the National Testing Agency (NTA), the National Medical Commission (NMC), or the Ministry of Education, Government of India. The author disclaims any liability for errors or omissions.\\[8pt]

\textbf{Typesetting \& Typography:} Typeset in \LaTeXe\ with the Tectonic XeTeX engine using Latin Modern typefaces. Mathematical typesetting follows ISO 80000-2 standards. Produced and printed via Amazon Kindle Direct Publishing (KDP).\\[4pt]
Printed in the United States of America / United Kingdom / India.
}
\end{flushleft}
\cleardoublepage

% --- Dedication Page ---
\thispagestyle{empty}
\vspace*{5cm}
\begin{center}
  \itshape\large
  To my parents, whose quiet sacrifices and endless belief built the foundation of my life;\\
  \vspace{1.2cm}
  To the teachers and mentors who showed me that physics is not a collection of arbitrary formulas,\\
  but the poetry of how nature actually works;\\
  \vspace{1.2cm}
  And to you, the medical aspirant reading this in the quiet hours of the night---\\
  may every solved problem and mastered derivation bring you one step closer\\
  to the stethoscope, the white coat, and a lifetime of healing.
\end{center}
\cleardoublepage

% --- Acknowledgements ---
\chapter*{Acknowledgements}
\addcontentsline{toc}{chapter}{Acknowledgements}

Creating a complete, mathematically uncompromising textbook calibrated to a competitive examination as fiercely contested as NEET UG is never a solitary effort. I owe an immense debt of gratitude to several people and institutions whose influence echoes through these chapters.

First and foremost, I thank my family for their patience, understanding, and unwavering encouragement during the countless late nights and weekends spent drafting, proofreading, and verifying derivations.

I express deep gratitude to the mentors and physics educators whose classroom discussions shaped my conviction that physics must be taught from fundamental principles rather than mechanical memorization. Their insistence on clear vector diagrams, rigorous free-body analysis, and boundary condition checks inspired the structure of every chapter in this book.

I am especially grateful to the students and peer study groups whose probing questions, skepticism, and frequent exam mistakes illuminated the exact cognitive hurdles aspirants face. The "NEET Trap" boxes in this book were born directly from real student doubts and mock exam error logs.

Finally, I acknowledge the vibrant open-source scientific typesetting community, specifically the developers of the \LaTeXe\ ecosystem and the Tectonic compiler, which made it possible to produce a publication of this typographical caliber.

\vspace{1cm}
\begin{flushright}
  \textbf{Satya Prakash}\\
  \textit{October 2026}
\end{flushright}
\cleardoublepage

% --- Author's Preface ---
\chapter*{Author's Preface: Straight Talk Before We Begin}
\addcontentsline{toc}{chapter}{Author's Preface: Straight Talk Before We Begin}

Let's be completely frank with each other. If you are preparing for NEET UG, you already know that physics is where ranks are decided. Biology gives you the foundation, Chemistry keeps you in the game, but Physics is what separates a student struggling for a cutoff from one who walks into a top government medical college.

Yet for most aspirants, physics feels like a daily war. You sit down with coaching modules running over 800 pages, and half the material is either filled with fluff or contains obsolete topics that the National Medical Commission (NMC) eliminated years ago. You waste precious study hours memorizing Carnot refrigerator formulas, potentiometer wire balancing equations, and Earth magnetism tables that will not appear on your exam paper. Meanwhile, when the actual exam twists a rolling friction problem on an inclined plane or asks an Assertion-Reasoning question on Gauss's law with non-symmetric charges, formulas from memory suddenly fail.

I wrote this book because I wanted to hand you the exact companion I wished I had when studying: honest, rigorous, beautifully organized, and talking to you straight without any fake "miracle tricks" or empty motivation. 

Here is how this book is built, and how you should use it:

\begin{enumerate}[leftmargin=*]
  \item \textbf{Bedrock Principles Over Rote Memorization:} Every major chapter starts from first principles. When we look at work-energy, fluid dynamics, or electromagnetic induction, you will see the complete mathematical derivation. Why? Because when you understand where a formula comes from and what assumptions were made to reach it, you become immune to the traps exam setters lay for unsuspecting students.
  
  \item \textbf{The Five Tactical Callout Systems:} Throughout every chapter, you will encounter five distinct color-coded boxes. Treat them like field markers:
  \begin{itemize}
    \item \textbf{Core Principle Boxes (\texttt{conceptbox}):} The foundational laws and definitions. Pay close attention to these---NTA draws multi-statement and factual questions directly from these definitions.
    \item \textbf{Master Formula Boxes (\texttt{formulabox}):} Every critical governing equation with explicit variable definitions, limits of integration, and SI units.
    \item \textbf{Application Regime Boxes (\texttt{usecasebox}):} The real-world conditions where formulas work, where they break down, and shortcuts for common numerical situations.
    \item \textbf{NEET Trap Boxes (\texttt{trapbox}):} The exact spots where thousands of students lose 5 marks (-1 penalty plus the 4 marks they missed). These cover sign convention mistakes, hidden assumptions, and misleading exceptions.
    \item \textbf{Direct NCERT Lines (\texttt{ncertbox}):} Verbatim textual extractions and table data that frequently form the basis of Assertion-Reasoning items.
  \end{itemize}

  \item \textbf{Strict NMC Syllabus Calibration:} Everything in this book conforms strictly to the revised NMC syllabus for NEET UG 2027. Obsolete topics like Carnot engines, free and damped oscillations, potentiometers, and transistor amplifiers have been flagged and excised from the core theory. You will not waste a single hour on deleted material.

  \item \textbf{Experimental Skills (Unit 20) Integration:} The NMC added explicit weightage to practical physics. Chapter 6 is dedicated entirely to the 18 prescribed experimental skills---from Vernier calipers and screw gauges to sonometer wires, focal length determination, and meter bridges.
\end{enumerate}

A personal piece of advice: do not read physics like a novel. If you are sitting on your bed flipping pages without a pen in your hand, you are not studying physics. Pick up a notebook, derive the equations alongside the text, draw every free-body diagram yourself, and work through the problem archetypes with the solutions covered.

Mistakes are going to happen. When you get a question wrong in a practice test, do not get demoralized. An error made in practice is a gift: it reveals a blind spot today so you don't repeat it on exam day.

You have the capability and the time to master this subject. Stay consistent, stay disciplined, and keep your focus on the prize. I'll see you on the other side with that white coat.

\vspace{1cm}
\begin{flushright}
  \textbf{Satya Prakash}\\
  Author \& Dedicated Mentor\\
  \href{mailto:spdedsec@hotmail.com}{spdedsec@hotmail.com}\\
  \textit{October 2026}
\end{flushright}
\cleardoublepage

% --- Syllabus Blueprint & NMC Rationalization Guide ---
\chapter*{Syllabus Blueprint \& NMC Rationalization Guide}
\addcontentsline{toc}{chapter}{Syllabus Blueprint \& NMC Rationalization Guide}

The National Eligibility cum Entrance Test (NEET UG 2027) follows the curriculum prescribed by the Under Graduate Medical Education Board (UGMEB) of the National Medical Commission (NMC). This section outlines the structure of the examination, subject weightage, and critical syllabus deletions.

\section*{Official Physics Examination Architecture}

\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{l c c c c Y}
\toprule
\textbf{Component} & \textbf{Section A} & \textbf{Section B} & \textbf{Total Questions} & \textbf{Marks} & \textbf{Question Typology} \\
\midrule
\textbf{Physics} & 35 & 15 (Attempt 10) & 45 & 180 & Single Choice, MCQs, \\
\textbf{Exam Total} & 140 & 60 (Attempt 40) & 180 & 720 & Assertion-Reason, Matrix Match \\
\bottomrule
\end{tabularx}
\caption{NEET UG Physics Examination Scheme (+4 for correct response, $-1$ for incorrect response, 0 for unattempted).}
\end{table}

\section*{Official 20-Unit Physics Syllabus Structure}

\begin{enumerate}[leftmargin=*]
  \item \textbf{Unit 1: Physics and Measurement} (Units, dimensions, error propagation, significant figures, Vernier calipers, screw gauge).
  \item \textbf{Unit 2: Kinematics} (Frame of reference, rectilinear motion, relative velocity, 2D projectile motion, uniform circular motion).
  \item \textbf{Unit 3: Laws of Motion} (Newton's laws, momentum conservation, equilibrium, friction dynamics, circular dynamics and banking).
  \item \textbf{Unit 4: Work, Energy and Power} (Work-energy theorem, conservative forces, potential energy of springs, vertical circular motion, collisions).
  \item \textbf{Unit 5: Rotational Motion} (Centre of mass, moment of inertia, parallel and perpendicular axis theorems, torque, angular momentum, pure rolling).
  \item \textbf{Unit 6: Gravitation} (Kepler's laws, universal gravitation, acceleration due to gravity variation, gravitational potential and energy, orbital velocity, escape speed).
  \item \textbf{Unit 7: Properties of Solids and Liquids} (Elasticity, Hooke's law, Young's/bulk/shear moduli, Pascal's law, Archimedes principle, surface tension, capillarity, viscosity, Stokes' law, Bernoulli's theorem).
  \item \textbf{Unit 8: Thermodynamics} (Thermal equilibrium, zeroth law, heat, work, first law of thermodynamics, isothermal, adiabatic, isobaric, isochoric processes, second law).
  \item \textbf{Unit 9: Kinetic Theory of Gases} (Equation of state of perfect gas, kinetic postulates, pressure formulation, kinetic interpretation of temperature, rms speed, degrees of freedom, equipartition of energy, mean free path).
  \item \textbf{Unit 10: Oscillations and Waves} (Periodic motion, SHM kinematics and dynamics, spring-mass systems, simple pendulum, wave motion, longitudinal and transverse waves, superposition, standing waves in strings and pipes, beats).
  \item \textbf{Unit 11: Electrostatics} (Coulomb's law, electric field, electric dipole, Gauss's law and applications, electric potential, equipotential surfaces, capacitors, dielectrics).
  \item \textbf{Unit 12: Current Electricity} (Electric current, drift velocity, Ohm's law, resistivity, temperature dependence, Kirchhoff's laws, Wheatstone bridge, internal resistance).
  \item \textbf{Unit 13: Magnetic Effects of Current and Magnetism} (Biot-Savart law, Ampère's circuital law, force on moving charges and current-carrying conductors, magnetic dipole, moving coil galvanometer).
  \item \textbf{Unit 14: Electromagnetic Induction and Alternating Currents} (Faraday's laws, Lenz's law, eddy currents, self and mutual inductance, AC circuits, impedance, LCR series circuits, resonance, power in AC, transformers).
  \item \textbf{Unit 15: Electromagnetic Waves} (Displacement current, Maxwell's equations characteristics, electromagnetic spectrum from radio waves to gamma rays).
  \item \textbf{Unit 16: Optics} (Ray optics: reflection, refraction, total internal reflection, lens maker's formula, prisms, microscopes, telescopes; Wave optics: Huygens' principle, interference, Young's double slit, diffraction at single slit).
  \item \textbf{Unit 17: Dual Nature of Matter and Radiation} (Photoelectric effect, Hertz and Lenard's observations, Einstein's photoelectric equation, de Broglie relation).
  \item \textbf{Unit 18: Atoms and Nuclei} (Alpha-particle scattering, Rutherford model, Bohr model, energy levels, hydrogen spectrum, atomic nuclei, mass defect, binding energy per nucleon).
  \item \textbf{Unit 19: Electronic Devices} (Semiconductors, energy bands, intrinsic and extrinsic semiconductors, p-n junction diode, I-V characteristics, diode as rectifier, logic gates: OR, AND, NOT, NAND, NOR).
  \item \textbf{Unit 20: Experimental Skills} (18 prescribed experiments including Vernier calipers, screw gauge, simple pendulum, Metre Scale principle of moments, Young's modulus by Searle's method, surface tension by capillary rise, viscosity of liquid, sonometer, resonance tube, Ohm's law, meter bridge, p-n junction diode characteristics).
\end{enumerate}

\begin{trapbox}[Zero-Tolerance NMC Exclusions: Topics Strictly Deleted from Physics]
Candidates must note that legacy textbooks and coaching modules contain several topics that have been \textbf{completely eliminated} by the NMC:
\begin{itemize}
  \item \textbf{Carnot Engine, Carnot Cycle \& Refrigerators} (Completely eliminated from Thermodynamics).
  \item \textbf{Free, Damped \& Forced Oscillations, Resonance} (Eliminated from Oscillations).
  \item \textbf{Doppler Effect in Sound} (Eliminated from Waves).
  \item \textbf{Potentiometer and its applications} (Replaced in practicals by Meter Bridge and Multimeter).
  \item \textbf{Earth's Magnetism and Magnetic Elements} (Eliminated from Magnetism).
  \item \textbf{Cyclotron} (Eliminated from Moving Charges).
  \item \textbf{Radioactive Decay Law, Alpha/Beta/Gamma Decay, Half-Life} (Eliminated from Nuclear Physics).
  \item \textbf{Transistor and its characteristics, Transistor as Amplifier/Oscillator} (Eliminated from Semiconductors).
\end{itemize}
\textbf{Preparation Directive:} Do not waste valuable study time practicing numericals or derivations on these excluded topics.
\end{trapbox}

\section*{Empirical Question Weightage Matrix}

\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{L c c}
\toprule
\textbf{Physics Domain} & \textbf{Typical Questions} & \textbf{Marks Weightage} \\
\midrule
Classical Mechanics (Kinematics, Dynamics, Work-Energy, Rotation, Gravitation, Fluids) & 16--18 & 64--72 Marks \\
Thermal Physics, Thermodynamics, Kinetic Theory \& Oscillations & 6--8 & 24--32 Marks \\
Electrodynamics, Magnetism, EMI \& AC Circuits & 11--13 & 44--52 Marks \\
Optics (Ray \& Wave Optics) & 4--5 & 16--20 Marks \\
Modern Physics \& Semiconductors (Dual Nature, Atoms, Nuclei, Diodes/Gates) & 6--8 & 24--32 Marks \\
Experimental Skills (Unit 20 Laboratory Practicals) & 2--3 & 8--12 Marks \\
\midrule
\textbf{Total Physics Paper} & \textbf{45 Attempted / 50} & \textbf{180 Marks} \\
\bottomrule
\end{tabularx}
\caption{Empirical Question Distribution in Recent NEET UG Papers.}
\end{table}

\cleardoublepage

% --- Table of Contents ---
\setcounter{tocdepth}{2}
\setcounter{secnumdepth}{2}
\tableofcontents
\cleardoublepage

% =========================================================================
% MAIN MATTER
% =========================================================================
\mainmatter

% =========================================================================
% PART I: CLASSICAL MECHANICS & FLUID DYNAMICS
% =========================================================================
\part{Classical Mechanics \& Fluid Dynamics}

\chapter{Foundations of Mechanics: Kinematics, Dynamics, Work, Energy \& Collisions}

This chapter establishes the core mechanics principles for NEET UG. We begin with the mathematical foundation of physical measurements, dimensional homogeneity, and error calculus, progressing into rectilinear and two-dimensional kinematics, Newton's laws of motion with constrained multi-block dynamics, microscopic friction mechanisms, vertical and banked circular motion, and the calculus of work, energy, and collision impulse.

""" + b_mechanics + r"""

\chapter{System of Particles, Rotational Dynamics, Gravitation \& Fluid Mechanics}

In this chapter, we bridge translational physics with rotational mechanics, celestial gravitation, and the mechanics of deformable media. Topics include the calculus of continuous mass distributions, moment of inertia theorems, angular momentum conservation, pure rolling on rough inclines, Kepler's laws, gravitational field/potential energy formulations, elastic moduli, surface tension, capillarity, and Bernoulli's hydrodynamic theorem.

""" + b_rot_grav + r"""

% =========================================================================
% PART II: HEAT, THERMODYNAMICS & WAVE MECHANICS
% =========================================================================
\part{Thermal Physics, Thermodynamics \& Wave Mechanics}

\chapter{Thermal Properties, Thermodynamics, Kinetic Theory \& Oscillations}

This chapter covers the thermal and vibrational behavior of matter. We explore thermal expansion, calorimetry, radiation laws, the first and second laws of thermodynamics with explicit NMC boundary exclusions, the molecular kinetic theory of gases with degrees of freedom and equipartition of energy, simple harmonic motion kinematics and spring-pendulum dynamics, and wave motion in strings and organ pipes.

""" + b_thermal + r"""

% =========================================================================
% PART III: ELECTRODYNAMICS, MAGNETISM & ALTERNATING CURRENTS
% =========================================================================
\part{Electrodynamics, Magnetism \& Alternating Currents}

\chapter{Electrostatics, Capacitance, Current Electricity \& Electromagnetism}

Electrodynamics represents over 25\% of the NEET Physics paper. In this chapter, we build from Coulomb's law and continuous charge distributions to Gauss's flux theorem, dielectric physics and capacitance networks, Ohm's drift dynamics and DC circuits, the magnetic effects of moving charges via Biot-Savart and Ampère laws, electromagnetic induction, LCR resonance in AC circuits, and Maxwell's electromagnetic wave spectrum.

""" + b_electro + r"""

% =========================================================================
% PART IV: OPTICS, MODERN PHYSICS & SEMICONDUCTORS
% =========================================================================
\part{Optics, Modern Physics \& Semiconductor Electronics}

\chapter{Ray Optics, Wave Optics, Quantum Radiation, Atomic Physics \& Semiconductors}

This chapter covers geometric and wave optics alongside modern quantum and solid-state physics. We investigate Snell's law, total internal reflection, the lens-maker's equation, optical instruments, Huygens' wavelets, Young's double-slit interference, single-slit diffraction, Einstein's photoelectric effect, de Broglie matter waves, Bohr's atomic postulates and spectral emissions, nuclear binding energy, and p-n junction diode electronics with digital logic gates.

""" + b_optics_mod + r"""

% =========================================================================
% PART V: EXPERIMENTAL SKILLS & PRACTICAL PHYSICS
% =========================================================================
\part{Experimental Skills \& Practical Physics}

\chapter{Practical Physics \& Prescribed Experimental Lab Skills (NMC Unit 20)}

Under the revised NMC guidelines, experimental physics forms a dedicated unit tested directly in both Section A and Section B. This chapter provides a rigorous, step-by-step analytical manual for all 18 prescribed laboratory experiments, focusing on least count derivations, zero errors, reading formulas, experimental precautions, and high-frequency exam traps.

""" + b_unit20 + r"""

% =========================================================================
% PART VI: MASTER FORMULA COMPENDIUMS & QUICK REVISION HANDBOOK
% =========================================================================
\part{Master Formula Compendiums \& Quick Revision Handbook}

\chapter{High-Yield Formula Compendium: Mechanics, Gravitation, Thermal \& SHM}

This chapter brings together every governing equation, parameter definition, validity boundary condition, and NEET trap across Class 11 Physics (Units 2 through 10). Use this compendium for rapid revision before full-length tests and final preparation cycles.

""" + f_mech + "\n\n" + f_rot_therm + r"""

\chapter{High-Yield Formula Compendium: Electrodynamics, Optics \& Modern Physics}

This chapter compiles all core formulas, vector relations, circuit equations, optical relations, quantum constants, and logic gate truth tables spanning Class 12 Physics (Units 11 through 19).

""" + f_electro + "\n\n" + f_optics + r"""

% =========================================================================
% BACK MATTER
% =========================================================================
\backmatter

\chapter*{About the Author \& Errata Submissions}
\addcontentsline{toc}{chapter}{About the Author \& Errata Submissions}

\textbf{Satya Prakash} is an educator, curriculum researcher, and author dedicated to creating rigorous, student-first learning resources for competitive examinations in India. His focus is on eliminating cognitive overload, dismantling obsolete legacy syllabi, and restoring conceptual rigor and mathematical transparency to competitive pre-medical preparation.

\section*{Official Project Repository \& Continuous Improvement}

Science education thrives on continuous scrutiny and collective refinement. If you identify a typo, numerical discrepancy, or pedagogical ambiguity, or if you wish to suggest an enhancement for future editions, please submit your feedback:

\begin{itemize}
  \item \textbf{Direct Author Email:} \href{mailto:spdedsec@hotmail.com}{spdedsec@hotmail.com}
  \item \textbf{GitHub Open-Source Repository:} \url{https://github.com/spdedsec/neet-study-materials}
  \item \textbf{Errata Tracker:} Verified corrections and updates are posted directly to the project repository.
\end{itemize}

\vspace{1.5cm}
\begin{center}
  \rule{0.6\textwidth}{0.6pt}\\[6pt]
  {\small\textbf{\color{primarydark}NEET UG 2027 Master Reference Series}}\\[2pt]
  {\footnotesize\color{gray}Authored by Satya Prakash $\cdot$ All Rights Reserved}
\end{center}

\end{document}
"""
    return tex


def build_chemistry_book() -> str:
    """Assemble the complete manuscript for Chemistry Master Textbook."""
    
    # Extract source chapters
    b_phys_chem = extract_body("chapters/chemistry/physical_chemistry_master_theory.tex")
    b_inorg = extract_body("chapters/chemistry/inorganic_chemistry_master_compendium.tex")
    b_org_theory = extract_body("chapters/chemistry/organic_chemistry_master_theory.tex")
    b_org_mech = extract_body("chapters/chemistry/organic_reaction_mechanisms_handbook.tex")
    b_lab = extract_body("chapters/chemistry/practical_chemistry_lab_manual.tex")

    # Split physical chemistry into Foundations (Units 1, 2, 4) and Dynamics (Units 5, 6, 7, 8)
    split_marker = r"\section{Chemical \& Ionic Equilibrium (Unit 6)}"
    split_pos = b_phys_chem.find(split_marker)
    if split_pos != -1:
        b_phys_part1 = b_phys_chem[:split_pos].strip()
        b_phys_part2 = b_phys_chem[split_pos:].strip()
    else:
        b_phys_part1 = b_phys_chem
        b_phys_part2 = ""

    # Extract formula modules
    f_phys1 = extract_body("formulas/chemistry/physical_chemistry_core_formulas.tex")
    f_phys2 = extract_body("formulas/chemistry/solutions_electrochemistry_kinetics_formulas.tex")
    f_inorg = extract_body("formulas/chemistry/inorganic_chemistry_compendium.tex")
    f_org = extract_body("formulas/chemistry/organic_chemistry_reactions.tex")

    tex = r"""\documentclass[10pt,twoside,openright]{book}
\usepackage{../styles/neet_book}

\begin{document}

% =========================================================================
% FRONT MATTER
% =========================================================================
\frontmatter

% --- Half-Title Page ---
\thispagestyle{empty}
\vspace*{4cm}
\begin{center}
  {\Huge\bfseries\color{primarydark} NEET UG CHEMISTRY}\\[0.6cm]
  {\Large\bfseries\color{accentblue} MASTER TEXTBOOK}\\[1.5cm]
  {\normalsize\color{gray} NEET UG 2027 Master Reference Series $\cdot$ Authoritative KDP Edition}
\end{center}
\cleardoublepage

% --- Full Title Page ---
\thispagestyle{empty}
\vspace*{2cm}
\begin{center}
  {\Huge\bfseries\color{primarydark} NEET UG CHEMISTRY}\\[0.4cm]
  {\LARGE\bfseries\color{primarydark} MASTER TEXTBOOK}\\[0.8cm]
  {\Large\bfseries\color{accentblue} Physical Chemistry, Inorganic Compendium, Organic Theory,}\\[0.2cm]
  {\Large\bfseries\color{accentblue} Reaction Mechanisms, Qualitative Lab Manual \& Formulas}\\[2cm]
  
  {\large\textbf{Authored by}}\\[0.3cm]
  {\LARGE\bfseries\color{primarydark} Satya Prakash}\\[1.5cm]

  {\normalsize\textbf{Strictly Calibrated to the Revised NMC Syllabus \& Rationalized NCERT Textbooks}}\\[0.3cm]
  {\small Target Examination: National Eligibility cum Entrance Test (NEET UG 2027)}\\[2.5cm]

  {\footnotesize Published for Independent Medical Aspirants, Educators \& Academic Study Circles}\\[0.2cm]
  {\footnotesize Print-on-Demand $\cdot$ Amazon KDP Distribution}
\end{center}
\cleardoublepage

% --- Professional Copyright Page ---
\thispagestyle{empty}
\vspace*{\fill}
\begin{flushleft}
{\small
\textbf{NEET UG CHEMISTRY MASTER TEXTBOOK}\\[2pt]
\textit{Complete Theory, Reaction Mechanisms, Qualitative Analysis \& Formula Compendium}\\[8pt]
\textbf{Author:} Satya Prakash\\
\textbf{Editorial Correspondence \& Academic Feedback:} \href{mailto:spdedsec@hotmail.com}{spdedsec@hotmail.com}\\
\textbf{Source Repository \& Official Errata:} \url{https://github.com/spdedsec/neet-study-materials}\\[10pt]

\copyright\ 2026--2027 Satya Prakash. All rights reserved.\\[8pt]

\textbf{First Edition:} October 2026\\
\textbf{Publishing Imprint:} Independent Academic Publishing / Amazon Kindle Direct Publishing (KDP)\\
\textbf{Target Cycle:} NEET UG 2027 (Undergraduate Medical Admissions Entrance Examination)\\
\textbf{ISBN-13 (Paperback):} 979-8-XXXXXXXXX (Placeholder for KDP Assigned ISBN)\\
\textbf{ISBN-13 (Hardcover):} 979-8-XXXXXXXXX (Placeholder for KDP Assigned ISBN)\\[10pt]

\textbf{All Rights Reserved.} No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any form or by any means---electronic, mechanical, photocopying, recording, scanning, or otherwise---without the prior written permission of the author, except for brief quotations embodied in critical reviews or scholarly analysis as permitted under copyright law.\\[8pt]

\textbf{Academic \& Legal Disclaimer:} This textbook is an independent preparation manual authored by Satya Prakash to assist candidates preparing for the National Eligibility cum Entrance Test (NEET UG). While every effort has been made to verify scientific accuracy and strict concordance with the National Medical Commission (NMC) curriculum and rationalized NCERT textbooks, the author and publisher make no official claims of affiliation with or endorsement by the National Testing Agency (NTA), the National Medical Commission (NMC), or the Ministry of Education, Government of India. The author disclaims any liability for errors or omissions.\\[8pt]

\textbf{Typesetting \& Typography:} Typeset in \LaTeXe\ with the Tectonic XeTeX engine using Latin Modern typefaces. Chemical nomenclature and IUPAC rules strictly observed. Produced and printed via Amazon Kindle Direct Publishing (KDP).\\[4pt]
Printed in the United States of America / United Kingdom / India.
}
\end{flushleft}
\cleardoublepage

% --- Dedication Page ---
\thispagestyle{empty}
\vspace*{5cm}
\begin{center}
  \itshape\large
  To my parents, whose boundless love and quiet sacrifices gave me the courage to pursue knowledge;\\
  \vspace{1.2cm}
  To the chemistry teachers who revealed that reactions are not random rules to be memorized,\\
  but the logical dance of electrons seeking thermodynamic stability;\\
  \vspace{1.2cm}
  And to every medical aspirant battling balancing equations, acid-base equilibria, and organic mechanisms---\\
  may this book be your clearest guide, turning what felt overwhelming into your greatest competitive strength.
\end{center}
\cleardoublepage

% --- Acknowledgements ---
\chapter*{Acknowledgements}
\addcontentsline{toc}{chapter}{Acknowledgements}

This comprehensive chemistry textbook reflects years of academic analysis, teaching, and systematic alignment with national medical entrance examinations. I wish to express my profound gratitude to all who contributed to its realization.

I thank my family for their unending patience, love, and constant moral support during the intensive writing and typesetting process.

I am deeply grateful to the chemistry educators and academic colleagues whose rigorous insights helped shape the structural framework of this book. Their insistence on clear mechanistic arrow-pushing, thermodynamic sign discipline, and crystal field theory clarity has elevated the quality of every discussion.

I owe special thanks to the students whose candid feedback and test error sheets provided direct insight into the most persistent conceptual pitfalls in competitive chemistry. The "NEET Trap" callouts throughout these pages are a direct response to those common stumbling blocks.

Finally, I express my sincere appreciation to the \LaTeXe\ open-source community for creating typographical tools that allow complex chemical equations, tabular reaction matrices, and color-coded callouts to be typeset with uncompromised aesthetic and mathematical precision.

\vspace{1cm}
\begin{flushright}
  \textbf{Satya Prakash}\\
  \textit{October 2026}
\end{flushright}
\cleardoublepage

% --- Author's Preface ---
\chapter*{Author's Preface: Straight Talk on Chemistry}
\addcontentsline{toc}{chapter}{Author's Preface: Straight Talk on Chemistry}

Let's sit down and talk honestly about NEET Chemistry.

Every year, students fall into one of two dangerous traps. On one hand, you have students who treat chemistry like a phonebook: they memorize hundreds of isolated reactions, random exceptions, and formula sheets without ever understanding electron density, inductive effects, or thermodynamic driving forces. The moment NTA twists a question into an Assertion-Reasoning format or gives a substituted benzaldehyde they haven't seen in a coaching worksheet, their memorized answers crumble.

On the other hand, you have students who waste hundreds of hours studying legacy coaching material that still includes nine entire chapters that the National Medical Commission (NMC) completely eliminated from the syllabus: Solid State, States of Matter, Surface Chemistry, Hydrogen, the s-Block, Metallurgy, Polymers, Chemistry in Everyday Life, and Environmental Chemistry. Think about that: nearly 35\% of the old syllabus is gone! 

Why does this matter to you? Because the NMC didn't reduce the syllabus to make NEET easier. They reduced the volume so they could demand \textbf{much deeper conceptual clarity} in the chapters that remain: Chemical Bonding, Coordination Compounds, General Organic Chemistry (GOC), Carbonyl Chemistry, Chemical Equilibrium, and Electrochemistry.

I created this master book to give you a single, unified, and uncompromisingly clear roadmap for NEET UG 2027:

\begin{enumerate}[leftmargin=*]
  \item \textbf{Physical Chemistry Built on First Principles:} We don't skip algebraic derivations. From the de Broglie wavelength to the Nernst equation and integrated rate laws, every equation is derived step-by-step with explicit units. You will understand exactly when an equation is valid and when it breaks down.
  
  \item \textbf{Mechanistic Organic Chemistry:} Organic chemistry is not a list of reagents; it is the logical movement of electron pairs from nucleophilic sites to electrophilic centers. Chapter 5 gives you a dedicated handbook of curved-arrow mechanisms, transition states, and carbocation rearrangements for all major reaction classes.
  
  \item \textbf{Inorganic Chemistry Demystified:} Instead of asking you to memorize isolated facts group by group, we use periodic trends, effective nuclear charge ($Z_{\text{eff}}$), inert pair effect, back-bonding, and crystal field splitting energy ($\Delta_o$) to explain why elements behave the way they do.
  
  \item \textbf{Comprehensive Lab Manual (Practical Chemistry):} Practical chemistry is now tested with high frequency. Chapter 6 provides the complete analytical procedure for cation group separation, anion confirmatory tests, and volumetric redox titrations.
  
  \item \textbf{The 5-Color Tactical Box Pedagogy:} Use the \texttt{conceptbox}, \texttt{formulabox}, \texttt{usecasebox}, \texttt{trapbox}, and \texttt{ncertbox} callouts to guide your study. Pay special attention to the Red Trap boxes---they highlight the exact sign conventions, hidden assumptions, and tricky exceptions where students consistently lose marks.
\end{enumerate}

Here is my study advice to you as a friend: work with paper and pen. Balance every redox equation by ion-electron method yourself. Draw out the curved arrows in organic mechanisms. Check the units in every physical chemistry numerical before hitting the calculator.

Stay steady, stay curious, and keep putting in the honest hours. The results will follow.

\vspace{1cm}
\begin{flushright}
  \textbf{Satya Prakash}\\
  Author \& Dedicated Mentor\\
  \href{mailto:spdedsec@hotmail.com}{spdedsec@hotmail.com}\\
  \textit{October 2026}
\end{flushright}
\cleardoublepage

% --- Syllabus Blueprint & NMC Rationalization Guide ---
\chapter*{Syllabus Blueprint \& NMC Rationalization Guide}
\addcontentsline{toc}{chapter}{Syllabus Blueprint \& NMC Rationalization Guide}

This section details the official NEET UG 2027 Chemistry curriculum prescribed by the National Medical Commission (NMC), highlighting the examination scheme, unit distribution, and critical syllabus exclusions.

\section*{Official Chemistry Examination Architecture}

\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{l c c c c Y}
\toprule
\textbf{Component} & \textbf{Section A} & \textbf{Section B} & \textbf{Total Questions} & \textbf{Marks} & \textbf{Question Typology} \\
\midrule
\textbf{Chemistry} & 35 & 15 (Attempt 10) & 45 & 180 & Single Choice, MCQs, \\
\textbf{Exam Total} & 140 & 60 (Attempt 40) & 180 & 720 & Assertion-Reason, Matrix Match \\
\bottomrule
\end{tabularx}
\caption{NEET UG Chemistry Examination Scheme (+4 for correct response, $-1$ for incorrect response, 0 for unattempted).}
\end{table}

\section*{Official 20-Unit Chemistry Syllabus Structure}

\begin{enumerate}[leftmargin=*]
  \item \textbf{Unit 1: Some Basic Concepts in Chemistry} (Matter and laws of chemical combination, mole concept, molar mass, stoichiometry and stoichiometric calculations).
  \item \textbf{Unit 2: Atomic Structure} (Bohr model and limitations, dual nature, de Broglie relation, Heisenberg uncertainty, quantum mechanical model, orbitals, quantum numbers, Hund's rule, Pauli exclusion, Aufbau principle).
  \item \textbf{Unit 3: Chemical Bonding and Molecular Structure} (Ionic bonding, lattice energy, Born-Haber cycle, covalent bond, VSEPR theory, hybridization, dipole moment, MOT for homonuclear diatomic molecules, hydrogen bonding).
  \item \textbf{Unit 4: Chemical Thermodynamics} (First law, enthalpy, Hess's law, bond dissociation enthalpy, spontaneous processes, entropy, Gibbs free energy criterion for spontaneity).
  \item \textbf{Unit 5: Solutions} (Types of solutions, Raoult's law, colligative properties: lowering of vapor pressure, elevation of boiling point, depression of freezing point, osmotic pressure, van 't Hoff factor).
  \item \textbf{Unit 6: Equilibrium} (Law of mass action, $K_p$ and $K_c$, Le Chatelier's principle, ionic equilibrium: ionization of acids/bases, pH scale, common ion effect, buffer solutions, solubility product $K_{sp}$).
  \item \textbf{Unit 7: Redox Reactions and Electrochemistry} (Oxidation states, balancing redox, conductance in electrolytic solutions, Kohlrausch's law, electrochemical cells, EMF, Nernst equation, Gibbs energy and EMF).
  \item \textbf{Unit 8: Chemical Kinetics} (Rate of reaction, rate law, order and molecularity, integrated rate equations for zero and first order, half-life, Arrhenius equation, activation energy).
  \item \textbf{Unit 9: Classification of Elements and Periodicity} (Modern periodic law, periodic trends: atomic/ionic radii, ionization enthalpy, electron gain enthalpy, electronegativity, valence).
  \item \textbf{Unit 10: $p$-Block Elements} (General electronic configuration and periodic trends across Groups 13 through 18, comparative chemistry, anomalous properties of first element).
  \item \textbf{Unit 11: $d$- and $f$-Block Elements} (Transition elements: electronic configuration, oxidation states, catalytic properties, magnetic properties, colored ions, lanthanoids and actinoids, lanthanoid contraction).
  \item \textbf{Unit 12: Coordination Compounds} (Werner's theory, IUPAC nomenclature, isomerism, Valence Bond Theory, Crystal Field Theory, spectrochemical series, stability and biological significance).
  \item \textbf{Unit 13: Purification and Characterization of Organic Compounds} (Qualitative and quantitative analysis: Lassaigne's test, Dumas, Kjeldahl, Carius methods).
  \item \textbf{Unit 14: Some Basic Principles of Organic Chemistry} (IUPAC nomenclature, inductive, electromeric, resonance and hyperconjugation effects, reactive intermediates: carbocations, carbanions, free radicals).
  \item \textbf{Unit 15: Hydrocarbons} (Alkanes: conformation of ethane; Alkenes: geometrical isomerism, Markovnikov/anti-Markovnikov addition; Alkynes: acidity, addition; Arenes: aromaticity, EAS mechanisms).
  \item \textbf{Unit 16: Organic Compounds Containing Halogens} (Haloalkanes and haloarenes: $S_N1$ and $S_N2$ mechanisms, environmental effects of polyhalogen compounds).
  \item \textbf{Unit 17: Organic Compounds Containing Oxygen} (Alcohols, phenols and ethers: Lucas test, Kolbe reaction, Reimer-Tiemann, Williamson synthesis; Aldehydes, ketones and carboxylic acids: nucleophilic addition, aldol condensation, Cannizzaro, Hell-Volhard-Zelinsky).
  \item \textbf{Unit 18: Organic Compounds Containing Nitrogen} (Amines: basicity, Hinsberg test, carbylamine test; Diazonium salts: synthetic applications).
  \item \textbf{Unit 19: Biomolecules} (Carbohydrates: aldoses, ketoses, glucose, fructose, glycosidic bond; Proteins: peptide bond, primary/secondary/tertiary structures, denaturation; Nucleic acids: DNA, RNA).
  \item \textbf{Unit 20: Principles Related to Practical Chemistry} (Qualitative salt analysis: cations and anions; Volumetric titrations: oxalic acid vs KMnO$_4$, Mohr's salt vs KMnO$_4$).
\end{enumerate}

\begin{trapbox}[Zero-Tolerance NMC Exclusions: The 9 Deleted Chemistry Chapters]
Under revised NMC regulations, the following \textbf{nine legacy chapters are completely deleted} from the NEET examination:
\begin{enumerate}
  \item \textbf{Solid State} (Unit cells, packing efficiency, point defects).
  \item \textbf{States of Matter (Gaseous \& Liquid Bulk States)} (Ideal gas equations remain in Unit 1; van der Waals equation and critical phenomena are eliminated).
  \item \textbf{Surface Chemistry} (Adsorption, colloids, micelles, catalysts).
  \item \textbf{General Principles of Metallurgy} (Extraction of metals, Ellingham diagrams).
  \item \textbf{Hydrogen} (Hydrides, heavy water, hydrogen peroxide).
  \item \textbf{s-Block Elements} (Alkali and alkaline earth metals).
  \item \textbf{Polymers} (Classification, polymerization reactions, plastics).
  \item \textbf{Chemistry in Everyday Life} (Drugs, medicines, soaps, detergents).
  \item \textbf{Environmental Chemistry} (Pollution, acid rain, ozone depletion).
\end{enumerate}
\textbf{Study Directive:} Do not invest study hours in these eliminated topics. All cognitive energy must focus on the rigorously tested Class 11 and Class 12 units above.
\end{trapbox}

\section*{Empirical Question Weightage Matrix}

\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{L c c}
\toprule
\textbf{Chemistry Domain} & \textbf{Typical Questions} & \textbf{Marks Weightage} \\
\midrule
Physical Chemistry (Mole concept, Atomic, Thermo, Equilibrium, Solutions, Electro, Kinetics) & 15--17 & 60--68 Marks \\
Inorganic Chemistry (Periodicity, Bonding, Coordination, $p$-Block, $d$-\&$f$-Block) & 13--15 & 52--60 Marks \\
Organic Chemistry (GOC, Hydrocarbons, Haloalkanes, Oxygen, Nitrogen, Biomolecules) & 14--16 & 56--64 Marks \\
Practical Chemistry (Qualitative Salt Analysis \& Volumetric Redox Titrations) & 2--3 & 8--12 Marks \\
\midrule
\textbf{Total Chemistry Paper} & \textbf{45 Attempted / 50} & \textbf{180 Marks} \\
\bottomrule
\end{tabularx}
\caption{Empirical Question Distribution in Recent NEET UG Papers.}
\end{table}

\cleardoublepage

% --- Table of Contents ---
\setcounter{tocdepth}{2}
\setcounter{secnumdepth}{2}
\tableofcontents
\cleardoublepage

% =========================================================================
% MAIN MATTER
% =========================================================================
\mainmatter

% =========================================================================
% PART I: PHYSICAL CHEMISTRY
% =========================================================================
\part{Physical Chemistry}

\chapter{Foundations of Physical Chemistry: Stoichiometry, Atomic Structure \& Thermodynamics}

Physical chemistry provides the quantitative foundation for all chemical systems. This chapter begins with mole concept stoichiometry and empirical laws of chemical combination, progresses into wave mechanics and quantum numbers, and establishes the first and second laws of thermodynamics with explicit enthalpy, entropy, and Gibbs free energy derivations.

""" + b_phys_part1 + r"""

\chapter{Chemical Dynamics: Equilibrium, Solutions, Electrochemistry \& Kinetics}

This chapter explores how and why chemical reactions proceed. We cover the dynamic equilibrium of reversible reactions, ionic equilibria and buffer solutions, Raoult's law and colligative properties, electrochemical cell EMF and the Nernst equation, and the calculus of chemical reaction kinetics with integrated rate laws and Arrhenius activation energy.

""" + b_phys_part2 + r"""

% =========================================================================
% PART II: INORGANIC CHEMISTRY
% =========================================================================
\part{Inorganic Chemistry}

\chapter{Inorganic Chemistry: Periodic Trends, Chemical Bonding, Coordination \& Block Elements}

Inorganic chemistry requires structural understanding rather than rote memorization. In this comprehensive compendium, we analyze modern periodic trends, molecular orbital theory (MOT) and VSEPR geometries, coordination compounds with crystal field theory (CFT) splitting, and comparative trends across the p-block and transition d/f-block elements.

""" + b_inorg + r"""

% =========================================================================
% PART III: ORGANIC CHEMISTRY & REACTION PATHWAYS
% =========================================================================
\part{Organic Chemistry \& Reaction Pathways}

\chapter{Organic Chemistry: Electronic Effects, Functional Groups \& Biomolecules}

This chapter spans the core of NEET Organic Chemistry. We develop the foundational electronic effects (inductive, resonance, hyperconjugation) and reactive intermediates, proceed through aliphatic and aromatic hydrocarbons, haloalkanes, oxygen-containing functional groups (alcohols, phenols, ethers, carbonyls, carboxylic acids), nitrogen derivatives (amines, diazonium salts), and conclude with biomolecules (carbohydrates, proteins, nucleic acids).

""" + b_org_theory + r"""

\chapter{Advanced Organic Reaction Mechanisms Handbook}

To answer multi-step synthesis and Assertion-Reasoning questions with confidence, students must master the underlying reaction mechanisms. This chapter presents a rigorous, curved-arrow mechanistic breakdown of electrophilic aromatic substitution, nucleophilic aliphatic substitution ($S_N1$ vs $S_N2$), elimination pathways ($E1$ vs $E2$), carbonyl additions and condensations, and carboxylic acid derivative substitutions.

""" + b_org_mech + r"""

% =========================================================================
% PART IV: PRACTICAL CHEMISTRY & QUALITATIVE ANALYSIS
% =========================================================================
\part{Practical Chemistry \& Qualitative Analysis}

\chapter{Practical Chemistry: Qualitative Salt Analysis \& Volumetric Redox Titrations}

With the NMC's renewed emphasis on practical laboratory skills, qualitative and quantitative analysis questions appear regularly. This chapter provides a complete laboratory manual covering systematic group separation of basic radicals (cations), confirmatory tests for acidic radicals (anions), and volumetric redox titrations with KMnO$_4$.

""" + b_lab + r"""

% =========================================================================
% PART V: MASTER FORMULA COMPENDIUMS & REACTION QUICK-REFERENCE
% =========================================================================
\part{Master Formula Compendiums \& Reaction Quick-Reference}

\chapter{Physical Chemistry Core Formulas \& Thermodynamic Equations}

This chapter compiles all mathematical formulations, equilibrium relations, colligative equations, electrochemical relations, and kinetic rate laws for rapid revision before major examinations.

""" + f_phys1 + "\n\n" + f_phys2 + r"""

\chapter{Inorganic Trends \& Organic Named Reactions Compendium}

This quick-reference compendium brings together inorganic electronic configurations, crystal field splitting patterns, and all 35+ prescribed organic named reactions, complete with reagents, conditions, and functional distinction tests.

""" + f_inorg + "\n\n" + f_org + r"""

% =========================================================================
% BACK MATTER
% =========================================================================
\backmatter

\chapter*{About the Author \& Errata Submissions}
\addcontentsline{toc}{chapter}{About the Author \& Errata Submissions}

\textbf{Satya Prakash} is an educator, curriculum researcher, and author dedicated to creating rigorous, student-first learning resources for competitive examinations in India. His focus is on eliminating cognitive overload, dismantling obsolete legacy syllabi, and restoring conceptual rigor and mathematical transparency to competitive pre-medical preparation.

\section*{Official Project Repository \& Continuous Improvement}

Science education thrives on continuous scrutiny and collective refinement. If you identify a typo, numerical discrepancy, or pedagogical ambiguity, or if you wish to suggest an enhancement for future editions, please submit your feedback:

\begin{itemize}
  \item \textbf{Direct Author Email:} \href{mailto:spdedsec@hotmail.com}{spdedsec@hotmail.com}
  \item \textbf{GitHub Open-Source Repository:} \url{https://github.com/spdedsec/neet-study-materials}
  \item \textbf{Errata Tracker:} Verified corrections and updates are posted directly to the project repository.
\end{itemize}

\vspace{1.5cm}
\begin{center}
  \rule{0.6\textwidth}{0.6pt}\\[6pt]
  {\small\textbf{\color{primarydark}NEET UG 2027 Master Reference Series}}\\[2pt]
  {\footnotesize\color{gray}Authored by Satya Prakash $\cdot$ All Rights Reserved}
\end{center}

\end{document}
"""
    return tex


def build_biology_book() -> str:
    """Assemble the complete manuscript for Biology Master Textbook."""
    
    # Extract Botany chapters
    b_plant_phys = extract_body("chapters/botany/plant_physiology_master_notes.tex")
    b_genetics = extract_body("chapters/botany/genetics_and_molecular_basis.tex")
    b_reprod = extract_body("chapters/botany/reproduction_and_biotechnology.tex")
    b_ecology = extract_body("chapters/botany/ecology_diversity_and_families.tex")
    
    # Extract Zoology chapters
    b_cell = extract_body("chapters/zoology/cell_diversity_and_animal_morphology.tex")
    b_human_phys = extract_body("chapters/zoology/human_physiology_master_notes.tex")
    b_health = extract_body("chapters/zoology/human_health_disease_and_evolution.tex")

    tex = r"""\documentclass[10pt,twoside,openright]{book}
\usepackage{../styles/neet_book}

\begin{document}

% =========================================================================
% FRONT MATTER
% =========================================================================
\frontmatter

% --- Half-Title Page ---
\thispagestyle{empty}
\vspace*{4cm}
\begin{center}
  {\Huge\bfseries\color{primarydark} NEET UG BIOLOGY}\\[0.6cm]
  {\Large\bfseries\color{accentblue} MASTER TEXTBOOK}\\[1.5cm]
  {\normalsize\color{gray} NEET UG 2027 Master Reference Series $\cdot$ Authoritative KDP Edition}
\end{center}
\cleardoublepage

% --- Full Title Page ---
\thispagestyle{empty}
\vspace*{2cm}
\begin{center}
  {\Huge\bfseries\color{primarydark} NEET UG BIOLOGY}\\[0.4cm]
  {\LARGE\bfseries\color{primarydark} MASTER TEXTBOOK}\\[0.8cm]
  {\Large\bfseries\color{accentblue} Complete Botany \& Zoology: Genetics, Plant Physiology,}\\[0.2cm]
  {\Large\bfseries\color{accentblue} Reproduction, Ecology, Cell Biology, Human Physiology,}\\[0.2cm]
  {\Large\bfseries\color{accentblue} Health, Evolution \& Quantitative Matrices}\\[2cm]
  
  {\large\textbf{Authored by}}\\[0.3cm]
  {\LARGE\bfseries\color{primarydark} Satya Prakash}\\[1.5cm]

  {\normalsize\textbf{Strictly Calibrated to the Revised NMC Syllabus \& Rationalized NCERT Textbooks}}\\[0.3cm]
  {\small Target Examination: National Eligibility cum Entrance Test (NEET UG 2027)}\\[2.5cm]

  {\footnotesize Published for Independent Medical Aspirants, Educators \& Academic Study Circles}\\[0.2cm]
  {\footnotesize Print-on-Demand $\cdot$ Amazon KDP Distribution}
\end{center}
\cleardoublepage

% --- Professional Copyright Page ---
\thispagestyle{empty}
\vspace*{\fill}
\begin{flushleft}
{\small
\textbf{NEET UG BIOLOGY MASTER TEXTBOOK}\\[2pt]
\textit{Complete Botany, Zoology, Plant Families, Human Physiology \& Quantitative Matrices}\\[8pt]
\textbf{Author:} Satya Prakash\\
\textbf{Editorial Correspondence \& Academic Feedback:} \href{mailto:spdedsec@hotmail.com}{spdedsec@hotmail.com}\\
\textbf{Source Repository \& Official Errata:} \url{https://github.com/spdedsec/neet-study-materials}\\[10pt]

\copyright\ 2026--2027 Satya Prakash. All rights reserved.\\[8pt]

\textbf{First Edition:} October 2026\\
\textbf{Publishing Imprint:} Independent Academic Publishing / Amazon Kindle Direct Publishing (KDP)\\
\textbf{Target Cycle:} NEET UG 2027 (Undergraduate Medical Admissions Entrance Examination)\\
\textbf{ISBN-13 (Paperback):} 979-8-XXXXXXXXX (Placeholder for KDP Assigned ISBN)\\
\textbf{ISBN-13 (Hardcover):} 979-8-XXXXXXXXX (Placeholder for KDP Assigned ISBN)\\[10pt]

\textbf{All Rights Reserved.} No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any form or by any means---electronic, mechanical, photocopying, recording, scanning, or otherwise---without the prior written permission of the author, except for brief quotations embodied in critical reviews or scholarly analysis as permitted under copyright law.\\[8pt]

\textbf{Academic \& Legal Disclaimer:} This textbook is an independent preparation manual authored by Satya Prakash to assist candidates preparing for the National Eligibility cum Entrance Test (NEET UG). While every effort has been made to verify biological accuracy and strict concordance with the National Medical Commission (NMC) curriculum and rationalized NCERT textbooks, the author and publisher make no official claims of affiliation with or endorsement by the National Testing Agency (NTA), the National Medical Commission (NMC), or the Ministry of Education, Government of India. The author disclaims any liability for errors or omissions.\\[8pt]

\textbf{Typesetting \& Typography:} Typeset in \LaTeXe\ with the Tectonic XeTeX engine using Latin Modern typefaces. Biological taxonomic nomenclature follows the International Code of Nomenclature for algae, fungi, and plants (ICN) and the International Code of Zoological Nomenclature (ICZN). Produced and printed via Amazon Kindle Direct Publishing (KDP).\\[4pt]
Printed in the United States of America / United Kingdom / India.
}
\end{flushleft}
\cleardoublepage

% --- Dedication Page ---
\thispagestyle{empty}
\vspace*{5cm}
\begin{center}
  \itshape\large
  To my parents, whose selfless dedication and love illuminated every step of my journey;\\
  \vspace{1.2cm}
  To the biologists and physicians whose tireless investigations into the living world\\
  revealed the exquisite unity of cellular and molecular life;\\
  \vspace{1.2cm}
  And to you, future doctor---\\
  may the biological wonders detailed in these pages inspire not only your success in NEET UG,\\
  but a lifelong reverence for the human body and the living systems you will soon heal.
\end{center}
\cleardoublepage

% --- Acknowledgements ---
\chapter*{Acknowledgements}
\addcontentsline{toc}{chapter}{Acknowledgements}

Writing an exhaustive, 360-mark reference textbook for NEET UG Biology requires balancing two essential qualities: absolute textual loyalty to rationalized NCERT benchmarks, and clinical conceptual depth that renders a student completely immune to tricky Assertion-Reasoning and Statement-based questions.

I express my deepest gratitude to my family for their unending understanding, encouragement, and sacrifices throughout the compilation of this manuscript.

I thank the academic biology faculty, medical researchers, and botanists whose critical discussions helped ensure that every floral formula, enzyme kinetic relation, and endocrine loop was represented with anatomical and physiological precision.

I am especially grateful to the hundreds of medical aspirants whose questions, doubts, and mock examination analyses directly shaped the high-yield tables and "NEET Trap" callouts throughout this book. Your pursuit of excellence was the primary catalyst for this work.

Finally, I acknowledge the developers of \LaTeXe\ and Tectonic, whose typesetting ecosystem allowed us to integrate comprehensive taxonomic matrices, biochemical pathways, and color-coded diagnostic summaries into a publication-ready Amazon KDP manuscript.

\vspace{1cm}
\begin{flushright}
  \textbf{Satya Prakash}\\
  \textit{October 2026}
\end{flushright}
\cleardoublepage

% --- Author's Preface ---
\chapter*{Author's Preface: Straight Talk on NEET Biology}
\addcontentsline{toc}{chapter}{Author's Preface: Straight Talk on NEET Biology}

Let's cut straight to the chase: Biology carries exactly \textbf{360 marks out of 720} in NEET UG. Exactly half the examination.

Because of this, you have probably heard the common advice a thousand times: \textit{"Just read NCERT ten times and you will get 360/360."}

Let me tell you what actually happens in the examination hall. Every year, thousands of brilliant, hardworking students read NCERT ten times, walk into the exam, and come out with 310 or 320 instead of 360. Why? Because they memorized the lines passively without understanding the underlying physiological mechanisms, without analyzing the exceptions in comparative tables, and without realizing how NTA twists two unrelated NCERT sentences into a lethal Assertion-Reasoning pair.

Furthermore, the National Medical Commission (NMC) significantly reorganized the syllabus:
\begin{itemize}
  \item \textbf{Deleted Chapters:} Entire legacy units were deleted---including \textit{Digestion and Absorption}, \textit{Transport in Plants}, \textit{Mineral Nutrition}, and \textit{Strategies for Enhancement in Food Production}. If you are spending hours memorizing nitrogenase enzyme mechanisms from Mineral Nutrition or digestive enzymes in the duodenum, you are burning study hours on zero-yield topics.
  \item \textbf{Newly Mandated Topics:} The NMC explicitly mandated \textbf{seven distinct angiosperm families} (Malvaceae, Cruciferae/Brassicaceae, Fabaceae/Leguminosae, Asteraceae/Compositae, Poaceae/Gramineae, Solanaceae, and Liliaceae) and reinstated detailed animal morphology for both \textbf{Frog} and \textbf{Cockroach}.
\end{itemize}

I wrote this master book to give you the ultimate, zero-compromise Biology textbook for NEET UG 2027:

\begin{enumerate}[leftmargin=*]
  \item \textbf{Complete Integration of Botany and Zoology:} Part I gives you the complete Botany curriculum---from photosynthesis and molecular genetics to reproductive biology, ecology, and all seven prescribed plant families. Part II delivers complete Zoology---cell biology, mitosis/meiosis, animal taxonomy, frog and cockroach morphology, integrated human physiology, immunology, and evolutionary biology.
  
  \item \textbf{Quantitative Biology \& Mathematical Formulations (Chapter 8):} Most biology books treat genetics and physiology as purely descriptive. But NEET regularly tests dihybrid and trihybrid probability calculations, recombination frequencies and gene mapping (centimorgan calculations), Hardy-Weinberg equilibrium algebra ($p^2+2pq+q^2=1$), pulmonary spirometry volumes, cardiac output calculations, and renal net filtration pressure. Chapter 8 brings all these quantitative principles together with full derivations.
  
  \item \textbf{The Five-Color Callout Architecture:}
  \begin{itemize}
    \item \textbf{Concept Boxes (\texttt{conceptbox}):} Structural definitions, anatomical relationships, and cellular pathways.
    \item \textbf{Formula Boxes (\texttt{formulabox}):} Exact biochemical equations, genetic ratios, and physiological measurements.
    \item \textbf{Use-Case Boxes (\texttt{usecasebox}):} Clinical correlations, ecological applications, and biotechnology techniques.
    \item \textbf{NEET Trap Boxes (\texttt{trapbox}):} Tricky exceptions, easily confused terms (e.g., tracheids vs vessels, juxtamedullary vs cortical nephrons, homologous vs analogous structures), and Assertion-Reason traps.
    \item \textbf{Direct NCERT Lines (\texttt{ncertbox}):} Verbatim high-yield sentences and table extractions that NTA loves to test.
  \end{itemize}
\end{enumerate}

My advice to you as a friend: do not just highlight sentences. When you study a physiological loop (like the Renin-Angiotensin-Aldosterone System or the photolysis of water), close the book and draw the flowchart from memory. When you study genetics, work out the Punnett squares by hand.

You have the discipline within you to master all 360 marks of Biology. Treat this book as your constant companion, review your error logs honestly, and stay committed to the dream that drove you to start this journey.

\vspace{1cm}
\begin{flushright}
  \textbf{Satya Prakash}\\
  Author \& Dedicated Mentor\\
  \href{mailto:spdedsec@hotmail.com}{spdedsec@hotmail.com}\\
  \textit{October 2026}
\end{flushright}
\cleardoublepage

% --- Syllabus Blueprint & NMC Rationalization Guide ---
\chapter*{Syllabus Blueprint \& NMC Rationalization Guide}
\addcontentsline{toc}{chapter}{Syllabus Blueprint \& NMC Rationalization Guide}

This section details the official NEET UG 2027 Biology curriculum prescribed by the National Medical Commission (NMC), covering both Botany and Zoology domains, examination weightage, and critical syllabus deletions.

\section*{Official Biology Examination Architecture}

\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{l c c c c Y}
\toprule
\textbf{Subject Domain} & \textbf{Section A} & \textbf{Section B} & \textbf{Total Questions} & \textbf{Marks} & \textbf{Question Typology} \\
\midrule
\textbf{Botany} & 35 & 15 (Attempt 10) & 45 & 180 & Single Choice, MCQs, \\
\textbf{Zoology} & 35 & 15 (Attempt 10) & 45 & 180 & Assertion-Reason, Statement I/II, \\
\midrule
\textbf{Master Biology Total} & \textbf{70} & \textbf{30 (Attempt 20)} & \textbf{90} & \textbf{360} & Match the Column (Matrix) \\
\bottomrule
\end{tabularx}
\caption{NEET UG Biology Examination Scheme (+4 for correct response, $-1$ for incorrect response, 0 for unattempted).}
\end{table}

\section*{Official 10-Unit Biology Syllabus Structure}

\begin{enumerate}[leftmargin=*]
  \item \textbf{Unit 1: Diversity in Living World} (What is living? Biodiversity, taxonomic hierarchy, binomial nomenclature, five-kingdom classification: Monera, Protista, Fungi, Plantae, Animalia; Salient features of non-chordates up to phyla level and chordates up to class level).
  \item \textbf{Unit 2: Structural Organisation in Animals and Plants} (Morphology, anatomy and functions of different parts of flowering plants: Root, stem, leaf, inflorescence, flower, fruit and seed; Description of families: Malvaceae, Cruciferae/Brassicaceae, Fabaceae/Leguminosae, Asteraceae/Compositae, Poaceae/Gramineae, Solanaceae, Liliaceae; Animal tissues; Morphology, anatomy and functions of digestive, circulatory, respiratory, nervous and reproductive systems of Frog and Cockroach).
  \item \textbf{Unit 3: Cell Structure and Function} (Cell theory, prokaryotic and eukaryotic cells, plant and animal cells, cell envelope, organelles: nucleus, mitochondria, chloroplast, endomembrane system; Biomolecules: carbohydrates, proteins, nucleic acids, enzymes; Cell cycle: interphase, mitosis and meiosis).
  \item \textbf{Unit 4: Plant Physiology} (Photosynthesis in higher plants: light reactions, photolysis, cyclic and non-cyclic photophosphorylation, Calvin cycle, C$_4$ pathway, photorespiration; Respiration in plants: glycolysis, TCA cycle, electron transport system, oxidative phosphorylation; Plant growth and development: auxins, gibberellins, cytokinins, ethylene, abscisic acid).
  \item \textbf{Unit 5: Human Physiology} (Breathing and respiration: pulmonary volumes, alveolar gas exchange, oxygen dissociation; Body fluids and circulation: blood composition, ABO/Rh grouping, cardiac cycle, ECG; Excretory products and elimination: nephron function, counter-current mechanism, RAAS; Locomotion and movement: sliding filament theory, skeletal joints; Neural control: action potentials, synapses; Chemical coordination: endocrine hormones and mechanisms).
  \item \textbf{Unit 6: Reproduction} (Sexual reproduction in flowering plants: microsporogenesis, megasporogenesis, double fertilization, apomixis; Human reproduction: male and female reproductive systems, gametogenesis, menstrual cycle, fertilization, embryogeny; Reproductive health: contraception, sexually transmitted infections, assisted reproductive technologies).
  \item \textbf{Unit 7: Genetics and Evolution} (Heredity and variation: Mendelian ratios, incomplete dominance, codominance, multiple alleles, linkage and crossing over, sex determination, sex-linked disorders; Molecular basis of inheritance: DNA structure, replication, transcription, genetic code, translation, lac operon, DNA fingerprinting; Evolution: origin of life, Darwinian selection, evidence for evolution, Hardy-Weinberg equilibrium, human evolution).
  \item \textbf{Unit 8: Biology and Human Welfare} (Health and disease: pathogens causing typhoid, pneumonia, malaria, amoebiasis, ringworm, filariasis; Basic principles of immunology: innate and acquired immunity, vaccines; AIDS and cancer: etiology, diagnosis, treatment; Microbes in human welfare: household products, industrial processing, sewage treatment, biofertilizers).
  \item \textbf{Unit 9: Biotechnology and Its Applications} (Principles and processes: recombinant DNA technology, restriction enzymes, cloning vectors, PCR; Applications in agriculture and medicine: genetically modified crops, Bt cotton, RNA interference, human insulin, gene therapy, transgenic animals).
  \item \textbf{Unit 10: Ecology and Environment} (Organisms and populations: population growth models, species interactions; Ecosystem: structure, productivity, decomposition, energy flow, ecological pyramids; Biodiversity and conservation: patterns of biodiversity, red data book, in-situ and ex-situ conservation).
\end{enumerate}

\begin{trapbox}[Zero-Tolerance NMC Exclusions: Topics Strictly Deleted from Biology]
Under revised NMC regulations, the following topics and chapters have been \textbf{completely eliminated}:
\begin{itemize}
  \item \textbf{Digestion and Absorption} (Entire human digestion chapter eliminated).
  \item \textbf{Transport in Plants} (Xylem/phloem transport mechanisms, water potential, transpiration pull eliminated from Plant Physiology).
  \item \textbf{Mineral Nutrition} (Macro/micronutrients, nitrogen metabolism, deficiency symptoms eliminated).
  \item \textbf{Strategies for Enhancement in Food Production} (Animal husbandry and plant breeding eliminated).
  \item \textbf{Environmental Issues} (Pollution, solid waste, global warming eliminated from Ecology).
  \item \textbf{Anatomy of Flowering Plants (legacy sections)} (Secondary growth, anomalous structures eliminated).
\end{itemize}
\textbf{Important Additions to Note:}
\begin{itemize}
  \item \textbf{Prescribed 7 Plant Families:} Malvaceae, Cruciferae/Brassicaceae, Fabaceae/Leguminosae, Asteraceae/Compositae, Poaceae/Gramineae, Solanaceae, and Liliaceae must be studied thoroughly.
  \item \textbf{Frog \& Cockroach Morphology:} Both are explicitly in the syllabus.
\end{itemize}
\end{trapbox}

\section*{Empirical Question Weightage Matrix}

\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{L c c}
\toprule
\textbf{Biology Domain} & \textbf{Typical Questions} & \textbf{Marks Weightage} \\
\midrule
Genetics \& Molecular Basis of Inheritance (Units 7A, 7B) & 15--18 & 60--72 Marks \\
Human Physiology (Respiration, Circulation, Excretion, Locomotion, Neuro-Endocrine) & 12--15 & 48--60 Marks \\
Plant Physiology (Photosynthesis, Respiration, Plant Growth Regulators) & 6--8 & 24--32 Marks \\
Cell Biology \& Cell Division (Cell Structure, Biomolecules, Mitosis, Meiosis) & 7--9 & 28--36 Marks \\
Reproduction \& Biotechnology (Plant/Human Reproduction, Health, rDNA, Biotech) & 14--16 & 56--64 Marks \\
Ecology \& Environment (Populations, Ecosystems, Biodiversity) & 8--10 & 32--40 Marks \\
Diversity in Living World \& Systematic Plant Families (Taxonomy, 7 Families, Frog/Cockroach) & 10--12 & 40--48 Marks \\
Immunology, Human Health \& Evolutionary Biology & 6--8 & 24--32 Marks \\
\midrule
\textbf{Total Biology Paper} & \textbf{90 Attempted / 100} & \textbf{360 Marks} \\
\bottomrule
\end{tabularx}
\caption{Empirical Question Distribution in Recent NEET UG Papers.}
\end{table}

\cleardoublepage

% --- Table of Contents ---
\setcounter{tocdepth}{2}
\setcounter{secnumdepth}{2}
\tableofcontents
\cleardoublepage

% =========================================================================
% MAIN MATTER
% =========================================================================
\mainmatter

% =========================================================================
% PART I: BOTANY: PLANT BIOLOGY, GENETICS, ECOLOGY & ANGIOSPERM FAMILIES
% =========================================================================
\part{Botany: Plant Biology, Genetics, Ecology \& Angiosperm Families}

\chapter{Plant Physiology: Photosynthesis, Cellular Respiration \& Phytohormones}

Plant Physiology forms the biochemical core of botany. In this chapter, we explore chloroplast thylakoid architectures, the Z-scheme of light reactions, cyclic and non-cyclic photophosphorylation, the Calvin $C_3$ cycle, the $C_4$ dicarboxylic acid pathway with Kranz anatomy, photorespiration, mitochondrial cellular respiration (glycolysis, link reaction, Krebs cycle, and the electron transport system), and the physiological roles of the five major phytohormone classes.

""" + b_plant_phys + r"""

\chapter{Genetics \& Molecular Basis of Inheritance}

Genetics is the highest-weightage domain in the entire NEET examination, typically generating between 15 and 18 questions. This chapter covers classical Mendelian principles of segregation and independent assortment, incomplete dominance, codominance, chromosomal theories of linkage, pedigree analysis, DNA structure, semi-conservative replication, prokaryotic and eukaryotic transcription, the universal genetic code, translation, the lac operon, and DNA fingerprinting.

""" + b_genetics + r"""

\chapter{Sexual Reproduction \& Applied Biotechnology}

This chapter bridges plant and human reproduction with modern molecular biotechnology. We analyze microsporogenesis, megasporogenesis, pollen-pistil interactions, double fertilization, endosperm development, apomixis, human gametogenesis and hormonal regulation, contraceptive methods, and the principles and tools of recombinant DNA technology including restriction endonucleases, plasmid vectors, PCR amplification, Bt transgenic crops, and gene therapy.

""" + b_reprod + r"""

\chapter{Ecology, Environmental Biology \& Systematic Plant Families}

Ecology examines the interactions of organisms with their abiotic and biotic environment, population growth kinetics, ecosystem trophic pyramids, and global biodiversity conservation strategies. Furthermore, this chapter provides a systematic morphological analysis of the seven angiosperm families specifically prescribed by the National Medical Commission: Malvaceae, Cruciferae (Brassicaceae), Fabaceae (Leguminosae), Asteraceae (Compositae), Poaceae (Gramineae), Solanaceae, and Liliaceae.

""" + b_ecology + r"""

% =========================================================================
% PART II: ZOOLOGY: CELLULAR LIFE, ANIMAL DIVERSITY, HUMAN PHYSIOLOGY & HEALTH
% =========================================================================
\part{Zoology: Cellular Life, Animal Diversity, Human Physiology \& Health}

\chapter{Cell Biology, Cell Division \& Animal Morphology}

Every biological inquiry starts at the cellular level. This chapter analyzes prokaryotic and eukaryotic ultrastructure, organelle compartmentalization, enzyme catalytic mechanics, the stages of mitosis and meiosis with synapsis and crossing over, the phylogenetic classification of animal phyla, and the complete anatomical systems of the frog (\textit{Rana tigrina}) and cockroach (\textit{Periplaneta americana}).

""" + b_cell + r"""

\chapter{Human Physiology: Integrated Organ Systems}

Human Physiology represents the core clinical foundation for medical aspirants. In this chapter, we explore the mechanical and biochemical processes of breathing and alveolar gas exchange, body fluids and the cardiac cycle, nephron counter-current exchange and osmoregulation, musculoskeletal excitation-contraction coupling in sliding filament mechanics, and neuro-endocrine coordination via action potentials and peptide/steroid hormone cascades.

""" + b_human_phys + r"""

\chapter{Immunology, Human Pathogens, Disease \& Evolutionary Biology}

This chapter explores human health, host-pathogen interactions, defense mechanisms, and the history of life on Earth. Topics include innate vs acquired immunity, antibody structure, active and passive immunization, major bacterial/viral/protozoan/helminthic diseases, oncogenesis, chemical evolution, homologous vs analogous morphological evidence, natural selection, the Hardy-Weinberg equilibrium principle, and the timeline of human evolution.

""" + b_health + r"""

% =========================================================================
% PART III: HIGH-YIELD QUANTITATIVE BIOLOGY & DIAGNOSTIC MATRICES
% =========================================================================
\part{High-Yield Quantitative Biology \& Diagnostic Matrices}

\chapter{Quantitative Biology, Genetic Formulations \& High-Yield Diagnostic Matrices}

To achieve a perfect score of 360 in NEET Biology, students must master both qualitative concepts and quantitative formulations. This chapter provides a unified analytical compendium of genetic probability calculations, recombination frequencies, population genetics models, physiological capacity values, floral formula matrices for all seven prescribed plant families, and high-frequency Assertion-Reasoning anchors.

\section{Quantitative Genetics \& Probability Calculus}

\begin{conceptbox}[Foundational Mendelian Probability Principles]
Mendelian inheritance patterns obey the fundamental laws of probability:
\begin{enumerate}[leftmargin=*]
  \item \textbf{Rule of Multiplication (Product Rule):} The probability of two independent events occurring simultaneously is the product of their individual probabilities:
  \begin{equation}
    P(A \cap B) = P(A) \times P(B)
  \end{equation}
  \textit{Application:} Probability of obtaining a homozygous recessive genotype ($aabb$) from a dihybrid cross ($AaBb \times AaBb$) is $P(aa) \times P(bb) = \frac{1}{4} \times \frac{1}{4} = \frac{1}{16}$.
  
  \item \textbf{Rule of Addition (Sum Rule):} The probability of either of two mutually exclusive events occurring is the sum of their individual probabilities:
  \begin{equation}
    P(A \cup B) = P(A) + P(B)
  \end{equation}
  \textit{Application:} In a monohybrid cross ($Aa \times Aa$), the probability of obtaining a heterozygote ($Aa$) via either maternal or paternal allele donation is $\frac{1}{4} + \frac{1}{4} = \frac{1}{2}$.
\end{enumerate}
\end{conceptbox}

\begin{formulabox}[Master Combinatorial Formulas for Multi-Gene Crosses]
For a cross involving $n$ independently assorting heterozygous gene pairs ($AaBbCc\dots$):
\begin{align}
  \text{Number of Genetically Distinct Gametes: } & N_{\text{gametes}} = 2^n \\
  \text{Total Number of Offspring Genotypes: } & N_{\text{genotypes}} = 3^n \\
  \text{Total Number of Offspring Phenotypes: } & N_{\text{phenotypes}} = 2^n \quad (\text{assuming complete dominance}) \\
  \text{Number of Squares in Punnett Grid: } & N_{\text{grid}} = 2^n \times 2^n = 4^n \\
  \text{Fraction of Completely Homozygous Recessive: } & F_{\text{recessive}} = \left(\frac{1}{4}\right)^n \\
  \text{Fraction of Completely Homozygous Dominant: } & F_{\text{dominant}} = \left(\frac{1}{4}\right)^n \\
  \text{Fraction of Completely Heterozygous Individuals: } & F_{\text{hetero}} = \left(\frac{1}{2}\right)^n
\end{align}
\end{formulabox}

\begin{usecasebox}[Chi-Square ($\chi^2$) Goodness-of-Fit Test in Genetic Analysis]
To determine whether observed offspring numbers deviate significantly from theoretical Mendelian expectations:
\begin{equation}
  \chi^2 = \sum \frac{(O - E)^2}{E}
\end{equation}
where $O$ is the observed frequency, $E$ is the expected frequency based on Mendelian ratio, and degrees of freedom $df = k - 1$ (where $k$ is the number of phenotypic classes). If $\chi^2_{\text{calc}} < \chi^2_{\text{critical}}$ at $p = 0.05$, the observed deviation is attributed strictly to random chance and the Mendelian hypothesis is accepted.
\end{usecasebox}

\section{Recombination Frequency \& Chromosome Mapping Calculus}

\begin{formulabox}[Morgan-Sturtevant Gene Mapping Formulations]
The recombination frequency ($RF$) between two linked genes on a chromosome is directly proportional to the physical distance between them:
\begin{equation}
  RF = \left(\frac{\text{Total Number of Recombinant Offspring}}{\text{Total Number of Offspring Progeny}}\right) \times 100\%
\end{equation}
\textbf{Units \& Metric Standards:}
\begin{itemize}
  \item $1\%$ Recombination Frequency $= 1\,\text{Map Unit (m.u.)} = 1\,\text{centimorgan (cM)}$.
  \item Maximum observable recombination frequency for two genes on the same chromosome is $\mathbf{50\%}$ (at which point they assort independently, indistinguishable from unlinked genes on different chromosomes).
\end{itemize}
\textbf{Three-Point Test Cross \& Interference Formulations:}
\begin{align}
  \text{Coefficient of Coincidence } (C) &= \frac{\text{Observed Frequency of Double Crossovers}}{\text{Expected Frequency of Double Crossovers}} \\
  \text{Interference } (I) &= 1 - C
\end{align}
\textit{Interpretation:} If $I > 0$ (positive interference), a crossover in one interval suppresses crossover formation in an adjacent chromosomal region. If $I = 1$, double crossovers are completely suppressed.
\end{formulabox}

\section{Population Genetics: Hardy-Weinberg Mathematical Model}

\begin{formulabox}[Hardy-Weinberg Equilibrium Equations]
For a diploid population with two alleles ($A$ and $a$) at a single locus with frequencies $p$ and $q$:
\begin{align}
  \text{Allelic Frequency Identity: } & p + q = 1 \\
  \text{Genotypic Frequency Expansion: } & (p + q)^2 = p^2 + 2pq + q^2 = 1
\end{align}
where:
\begin{itemize}
  \item $p^2$: Frequency of homozygous dominant individuals ($AA$).
  \item $2pq$: Frequency of heterozygous carrier individuals ($Aa$).
  \item $q^2$: Frequency of homozygous recessive affected individuals ($aa$).
\end{itemize}
\end{formulabox}

\begin{trapbox}[NEET Trap: Allelic Frequency vs Genotypic Frequency]
Pay meticulous attention to the wording in Hardy-Weinberg exam questions:
\begin{itemize}
  \item If given "frequency of recessive \textbf{allele}": that is $q$.
  \item If given "frequency of recessive \textbf{disease / phenotype / individuals}": that is $q^2$. You must take the square root $\sqrt{q^2} = q$ first, then find $p = 1 - q$, and finally compute carrier frequency $2pq$.
  \item \textbf{Equilibrium Preconditions:} Strictly valid only for: (1) large population size, (2) random mating, (3) no gene flow / migration, (4) no mutation, and (5) no natural selection.
\end{itemize}
\end{trapbox}

\section{Quantitative Human Physiology Matrices}

\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{L c L}
\toprule
\textbf{Physiological Parameter} & \textbf{Standard Value} & \textbf{Mathematical Definition / Formula} \\
\midrule
Tidal Volume (TV) & $500\,\si{mL}$ & Volume inspired or expired during normal breathing \\
Inspiratory Reserve Volume (IRV) & $2500$--$3000\,\si{mL}$ & Extra volume inspired forcibly above TV \\
Expiratory Reserve Volume (ERV) & $1000$--$1100\,\si{mL}$ & Extra volume expired forcibly after normal expiration \\
Residual Volume (RV) & $1100$--$1200\,\si{mL}$ & Gas remaining in lungs after maximal expiration \\
Vital Capacity (VC) & $3500$--$4500\,\si{mL}$ & $\mathrm{VC} = \mathrm{TV} + \mathrm{IRV} + \mathrm{ERV}$ \\
Total Lung Capacity (TLC) & $5000$--$6000\,\si{mL}$ & $\mathrm{TLC} = \mathrm{VC} + \mathrm{RV} = \mathrm{TV} + \mathrm{IRV} + \mathrm{ERV} + \mathrm{RV}$ \\
\midrule
Cardiac Output (CO) & $\approx 5000\,\si{mL/min}$ & $\mathrm{CO} = \text{Stroke Volume } (70\,\si{mL}) \times \text{Heart Rate } (72\,\si{bpm})$ \\
Glomerular Filtration Rate (GFR) & $125\,\si{mL/min}$ & Equivalent to $180\,\si{L/day}$ across both kidneys \\
Net Filtration Pressure (NFP) & $10\,\si{mmHg}$ & $\mathrm{NFP} = \mathrm{GHP}\,(60) - [\mathrm{BCOP}\,(32) + \mathrm{CHP}\,(18)]$ \\
Urine Excretion Rate & $1.0$--$1.5\,\si{L/day}$ & $>99\%$ of filtrate is reabsorbed by renal tubules \\
\bottomrule
\end{tabularx}
\caption{Master Diagnostic Matrix: Quantitative Human Physiological Constants.}
\end{table}

\section{Master Systematic Comparison of All 7 Prescribed Plant Families}

\begin{table}[htbp]
\centering
\scriptsize
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{l L L L L}
\toprule
\textbf{Family} & \textbf{Floral Formula} & \textbf{Androecium} & \textbf{Gynoecium} & \textbf{Key Diagnostic Examples} \\
\midrule
\textbf{Malvaceae} & $\oplus\:\text{Epi}_{3-8}\:\text{K}_{(5)}\:\text{C}_5\:\text{A}_{(\infty)}\:\underline{\text{G}}_{(5-\infty)}$ & Monadelphous stamens, monothecous reniform anthers & Syncarpous, superior, axile placentation & \textit{Hibiscus}, Cotton (\textit{Gossypium}), Lady's finger (\textit{Abelmoschus}) \\
\textbf{Cruciferae} & $\oplus\:\text{K}_{2+2}\:\text{C}_{4}\:\text{A}_{2+4}\:\underline{\text{G}}_{(2)}$ & Tetradynamous stamens ($2\text{ short outer} + 4\text{ long inner}$) & Bicarpellary, unilocular becoming bilocular via false septum (replum) & Mustard (\textit{Brassica}), Radish (\textit{Raphanus}), Turnip \\
\textbf{Fabaceae} & $\% \:\text{K}_{(5)}\:\text{C}_{1+2+(2)}\:\text{A}_{(9)+1}\:\underline{\text{G}}_1$ & Diadelphous stamens $[(9)+1]$, dithecous & Monocarpellary, superior, marginal placentation & Gram, Pea, Soybean, Sunnhemp, Lupin, \textit{Sesbania} \\
\textbf{Asteraceae} & $\oplus \text{ or } \%\:\text{K}_{\text{pappus}}\:\text{C}_{(5)}\:\text{A}_{(5)}\:\overline{\text{G}}_{(2)}$ & Syngenesious (anthers fused, filaments free) & Bicarpellary, inferior, basal placentation, single ovule & Sunflower (\textit{Helianthus}), Marigold, \textit{Taraxacum} \\
\textbf{Poaceae} & $\% \:\text{P}_{2}\:\text{A}_{3 \text{ or } 6}\:\underline{\text{G}}_1$ & Stamens versatile, pendulous & Monocarpellary, superior, basal placentation, feathery stigma & Wheat (\textit{Triticum}), Rice, Maize, Bamboo, Sugarcane \\
\textbf{Solanaceae} & $\oplus\:\text{K}_{(5)}\:\text{C}_{(5)}\:\text{A}_5\:\underline{\text{G}}_{(2)}$ & Epipetalous stamens, alternipetalous & Bicarpellary, syncarpous, superior, obliquely placed ovary, swollen placenta & Potato, Tomato, Brinjal, Chilli, Belladonna, Ashwagandha, Tobacco \\
\textbf{Liliaceae} & $\oplus\:\text{P}_{(3+3)}\:\text{A}_{3+3}\:\underline{\text{G}}_{(3)}$ & Epiphyllous stamens in two whorls & Tricarpellary, syncarpous, superior, axile placentation & \textit{Allium} (Onion, Garlic), \textit{Aloe}, \textit{Asparagus}, \textit{Colchicum autumnale} \\
\bottomrule
\end{tabularx}
\caption{Systematic Comparative Diagnostic Matrix for the 7 NMC-Prescribed Angiosperm Families.}
\end{table}

\begin{ncertbox}[Direct NCERT High-Yield Assertion-Reason Anchors]
\begin{itemize}
  \item \textbf{Floral Formulas as Definitive Identifiers:} In Solanaceae, the ovary is characteristically \textbf{obliquely placed} with a swollen placenta bearing many ovules; in Cruciferae, the ovary becomes bilocular due to a false septum called \textbf{replum}.
  \item \textbf{Staminal Adaptations:} Diadelphous stamens $[(9)+1]$ are unique to Fabaceae; monadelphous stamens with monothecous anthers are diagnostic of Malvaceae; tetradynamous stamens ($2+4$) are exclusive to Cruciferae; and syngenesious stamens are hallmark to Asteraceae.
  \item \textbf{Placentation Anchor:} Marginal (Fabaceae/Pea), Parietal with replum (Cruciferae/Mustard), Axile (Solanaceae, Malvaceae, Liliaceae), Basal (Asteraceae/Sunflower, Poaceae/Wheat).
\end{itemize}
\end{ncertbox}

% =========================================================================
% BACK MATTER
% =========================================================================
\backmatter

\chapter*{About the Author \& Errata Submissions}
\addcontentsline{toc}{chapter}{About the Author \& Errata Submissions}

\textbf{Satya Prakash} is an educator, curriculum researcher, and author dedicated to creating rigorous, student-first learning resources for competitive examinations in India. His focus is on eliminating cognitive overload, dismantling obsolete legacy syllabi, and restoring conceptual rigor and mathematical transparency to competitive pre-medical preparation.

\section*{Official Project Repository \& Continuous Improvement}

Science education thrives on continuous scrutiny and collective refinement. If you identify a typo, biological discrepancy, or pedagogical ambiguity, or if you wish to suggest an enhancement for future editions, please submit your feedback:

\begin{itemize}
  \item \textbf{Direct Author Email:} \href{mailto:spdedsec@hotmail.com}{spdedsec@hotmail.com}
  \item \textbf{GitHub Open-Source Repository:} \url{https://github.com/spdedsec/neet-study-materials}
  \item \textbf{Errata Tracker:} Verified corrections and updates are posted directly to the project repository.
\end{itemize}

\vspace{1.5cm}
\begin{center}
  \rule{0.6\textwidth}{0.6pt}\\[6pt]
  {\small\textbf{\color{primarydark}NEET UG 2027 Master Reference Series}}\\[2pt]
  {\footnotesize\color{gray}Authored by Satya Prakash $\cdot$ All Rights Reserved}
\end{center}

\end{document}
"""
    return tex


def main():
    BOOKS_DIR.mkdir(parents=True, exist_ok=True)
    
    print("=" * 70)
    print("NEET UG 2027 MASTER BOOK GENERATION & COMPILATION SUITE")
    print("Prepared by Satya Prakash <spdedsec@hotmail.com>")
    print("=" * 70)
    
    books = [
        ("physics_master_book.tex", build_physics_book),
        ("chemistry_master_book.tex", build_chemistry_book),
        ("biology_master_book.tex", build_biology_book),
    ]

    for filename, builder in books:
        filepath = BOOKS_DIR / filename
        print(f"\n--> Step 1: Generating {filename}...")
        tex_content = builder()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(tex_content)
        print(f"    Written {len(tex_content.splitlines())} lines to {filepath}")

        # Validate syntax using validate_latex.py
        val_script = ROOT_DIR / "scripts" / "validate_latex.py"
        print(f"--> Step 2: Validating LaTeX syntax for {filename}...")
        res = subprocess.run([sys.executable, str(val_script), str(filepath)], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"    Validation FAILED:\n{res.stdout}\n{res.stderr}")
            sys.exit(1)
        print("    Validation PASSED: All environments and braces strictly matched.")

        # Compile with Tectonic
        print(f"--> Step 3: Compiling {filename} with Tectonic...")
        cmd = [COMPILER, str(filepath)]
        comp_res = subprocess.run(cmd, cwd=ROOT_DIR, capture_output=True, text=True)
        if comp_res.returncode != 0:
            print(f"    Compilation FAILED:\n{comp_res.stdout}\n{comp_res.stderr}")
            sys.exit(1)
        
        pdf_name = filename.replace(".tex", ".pdf")
        pdf_path = BOOKS_DIR / pdf_name
        if pdf_path.exists():
            size_kb = pdf_path.stat().st_size / 1024
            print(f"    SUCCESS: Generated {pdf_path} ({size_kb:.1f} KB)")
        else:
            print(f"    ERROR: Output PDF {pdf_path} not found!")
            sys.exit(1)

    print("\n" + "=" * 70)
    print("ALL THREE MASTER BOOKS SUCCESSFULLY GENERATED AND COMPILED!")
    print("=" * 70)


if __name__ == "__main__":
    main()
