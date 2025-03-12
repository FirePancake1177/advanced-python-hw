#!/usr/bin/env python3

import sys
import fileinput

def nl(file_lines):
    for idx, line in enumerate(file_lines, 1):
        print(f"{idx:>6}\t{line}", end='')

def main():
    if len(sys.argv) > 1:
        files = sys.argv[1:]
        nl(fileinput.input(files))
    else:
        nl(sys.stdin)

if __name__ == "__main__":
    main()
