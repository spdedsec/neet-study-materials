#!/usr/bin/env python3
import glob

align_envs = {'tabular', 'tabularx', 'longtable', 'array', 'align', 'align*', 'aligned', 'matrix', 'bmatrix', 'pmatrix', 'cases'}

def fix_file(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    env_stack = []

    for line in lines:
        # Check start of environment
        for token in line.split():
            if '\\begin{' in token:
                start = token.find('\\begin{') + 7
                end = token.find('}', start)
                if end != -1:
                    env_name = token[start:end]
                    if env_name in align_envs:
                        env_stack.append(env_name)

        if not env_stack:
            # Replace & that is not preceded by \
            temp = line.replace('\\&', '__AMP__')
            temp = temp.replace('&', '\\&')
            fixed_line = temp.replace('__AMP__', '\\&')
            new_lines.append(fixed_line)
        else:
            new_lines.append(line)

        # Check end of environment
        for token in line.split():
            if '\\end{' in token:
                start = token.find('\\end{') + 5
                end = token.find('}', start)
                if end != -1:
                    env_name = token[start:end]
                    if env_stack and env_stack[-1] == env_name:
                        env_stack.pop()

    with open(fpath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Fixed {fpath}")

if __name__ == '__main__':
    for p in glob.glob('/home/spdedsec/neet-study-materials/**/*.tex', recursive=True):
        fix_file(p)
