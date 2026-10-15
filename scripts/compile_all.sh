#!/usr/bin/env bash
# Compilation automation script for NEET UG 2027 LaTeX Suite
# Prepared by Satya Prakash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

echo "=== NEET UG 2027 LaTeX Compiler Suite ==="
echo "Working directory: ${ROOT_DIR}"

# 1. Run ampersand fixer and syntax validation
echo "--> Step 1: Normalizing and validating LaTeX files..."
python3 "${SCRIPT_DIR}/fix_ampersands.py"
find "${ROOT_DIR}" -name "*.tex" -print0 | while IFS= read -r -d '' file; do
    python3 "${SCRIPT_DIR}/validate_latex.py" "${file}"
done

# 2. Check for LaTeX compiler (check tectonic first)
COMPILER=""
if [ -x "/home/spdedsec/.local/bin/tectonic" ]; then
    COMPILER="/home/spdedsec/.local/bin/tectonic"
elif command -v tectonic &> /dev/null; then
    COMPILER="tectonic"
elif command -v latexmk &> /dev/null; then
    COMPILER="latexmk -pdf -interaction=nonstopmode"
elif command -v pdflatex &> /dev/null; then
    COMPILER="pdflatex -interaction=nonstopmode"
elif command -v xelatex &> /dev/null; then
    COMPILER="xelatex -interaction=nonstopmode"
fi

if [ -z "${COMPILER}" ]; then
    echo "(!) No LaTeX compiler detected on PATH."
    exit 1
fi

echo "--> Step 2: Compiling documents using ${COMPILER}..."
find "${ROOT_DIR}" -name "*.tex" ! -name "macros.tex" -print0 | while IFS= read -r -d '' tex_file; do
    dir="$(dirname "${tex_file}")"
    base="$(basename "${tex_file}")"
    echo "Compiling ${base} in ${dir}..."
    (cd "${dir}" && ${COMPILER} "${base}")
done

echo "=== Compilation Complete: All PDFs successfully generated ==="
