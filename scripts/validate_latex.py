#!/usr/bin/env python3
import sys
import re

def validate_latex(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.splitlines()
    errors = []
    
    # Check environments
    env_stack = []
    begin_re = re.compile(r'\\begin\{([a-zA-Z0-9_\*]+)\}')
    end_re = re.compile(r'\\end\{([a-zA-Z0-9_\*]+)\}')
    
    for idx, line in enumerate(lines, 1):
        # strip comments
        uncommented = re.sub(r'(?<!\\)%.*', '', line)
        
        begins = begin_re.findall(uncommented)
        ends = end_re.findall(uncommented)
        
        for b in begins:
            env_stack.append((b, idx))
            
        for e in ends:
            if not env_stack:
                errors.append(f"Line {idx}: Unexpected \\end{{{e}}} with empty stack")
            else:
                last_b, last_idx = env_stack.pop()
                if last_b != e:
                    errors.append(f"Line {idx}: Mismatched environment. Expected \\end{{{last_b}}} (opened at line {last_idx}), found \\end{{{e}}}")

    while env_stack:
        b, idx = env_stack.pop()
        errors.append(f"Unclosed \\begin{{{b}}} opened at line {idx}")

    # Brace counting (naive check on non-comment lines)
    open_braces = 0
    close_braces = 0
    for idx, line in enumerate(lines, 1):
        uncommented = re.sub(r'(?<!\\)%.*', '', line)
        # ignore escaped braces
        clean = re.sub(r'\\[\{\}]', '', uncommented)
        open_braces += clean.count('{')
        close_braces += clean.count('}')

    if open_braces != close_braces:
        errors.append(f"Brace count mismatch: {open_braces} open '{{' vs {close_braces} close '}}'")

    return errors

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 validate_latex.py <file.tex>")
        sys.exit(1)
        
    target = sys.argv[1]
    errs = validate_latex(target)
    if errs:
        print(f"Validation FAILED for {target}:")
        for e in errs:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"Validation PASSED for {target}: All environments and braces strictly matched.")
