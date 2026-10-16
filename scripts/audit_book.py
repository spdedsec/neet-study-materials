#!/usr/bin/env python3
import subprocess
import re
import sys
from pathlib import Path

def audit_book(book_name, threshold=10.0):
    tex_path = Path(f"books/{book_name}.tex")
    print(f"\n=======================================================")
    print(f"COMPILING & LIVE AUDITING: {book_name} (threshold: {threshold}pt)")
    print(f"=======================================================")
    
    cmd = ["/home/spdedsec/.local/bin/tectonic", "-o", "books", str(tex_path)]
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    with open(tex_path, 'r', encoding='utf-8') as f:
        src_lines = f.readlines()
        
    overfulls = []
    pattern = re.compile(re.escape(book_name) + r'\.tex:(\d+): Overfull \\hbox \(([0-9.]+)pt too wide\)')
    
    for l in p.stdout.splitlines():
        m = pattern.search(l)
        if m:
            lno = int(m.group(1))
            width = float(m.group(2))
            overfulls.append((lno, width))
            
    print(f"Total Overfull \\hbox instances: {len(overfulls)}")
    sig = [o for o in overfulls if o[1] >= threshold]
    print(f"Significant Overfull (>= {threshold}pt): {len(sig)}")
    for lno, width in sig:
        snippet = src_lines[lno-1].strip() if lno <= len(src_lines) else ""
        print(f"Line {lno:4d} (+{width:5.1f}pt): {snippet[:95]}")
        
    return len(sig)

if __name__ == '__main__':
    book = sys.argv[1] if len(sys.argv) > 1 else 'biology_master_book'
    thresh = float(sys.argv[2]) if len(sys.argv) > 2 else 10.0
    audit_book(book, thresh)
