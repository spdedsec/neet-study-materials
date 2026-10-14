#!/usr/bin/env bash
# Compilation automation script for NEET UG 2027 LaTeX Suite
# Prepared by Satya Prakash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

echo "=== NEET UG 2027 LaTeX Compiler Suite ==="
echo "Working directory: ${ROOT_DIR}"

# 1. Run syntax validation first
echo "--> Step 1: Validating LaTeX syntax across all .tex files..."
find "${ROOT_DIR}" -name "*.tex" -print0 | while IFS= read -r -d '' file; do
    python3 "${SCRIPT_DIR}/validate_latex.py" "${file}"
done

# 2. Check for LaTeX compiler
COMPILER=""
if command -v latexmk &> /dev/null; then
    COMPILER="latexmk -pdf -interaction=nonstopmode"
elif command -v pdflatex &> /dev/null; then
    COMPILER="pdflatex -interaction=nonstopmode"
elif command -v xelatex &> /dev/null; then
    COMPILER="xelatex -interaction=nonstopmode"
fi

if [ -z "${COMPILER}" ]; then
    echo "(!) No local LaTeX compiler (latexmk / pdflatex / xelatex) detected on PATH."
    echo "    Files can be compiled using:"
    echo "    - Overleaf / TeX Live online"
    echo "    - VS Code with LaTeX Workshop extension"
    echo "    - Install TeX Live via: sudo apt-get install texlive-latex-extra texlive-fonts-recommended"
    exit 0
fi

echo "--> Step 2: Compiling documents using ${COMPILER}..."
find "${ROOT_DIR}" -name "*.tex" ! -name "macros.tex" -print0 | while IFS= read -r -d '' tex_file; do
    dir="$(dirname "${tex_file}")"
    base="$(basename "${tex_file}")"
    echo "Compiling ${base} in ${dir}..."
    (cd "${dir}" && ${COMPILER} "${base}")
done

echo "=== Compilation Complete ==="
