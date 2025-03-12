#!/usr/bin/env python3
import sys
from collections import deque

def tail(f, n):
    return deque(f, maxlen=n)

def main():
    files = sys.argv[1:]
    if not files:
        lines = tail(sys.stdin, 17)
        for line in lines:
            print(line, end='')
    else:
        multiple_files = len(files) > 1
        for idx, filename in enumerate(files):
            try:
                with open(filename, 'r') as file:
                    lines = tail(file, 10)
                    if multiple_files:
                        if idx > 0:
                            print()
                        print(f"==> {filename} <==")
                    for line in lines:
                        print(line, end='')
            except FileNotFoundError:
                print(f"tail.py: cannot open '{filename}' for reading: No such file or directory", file=sys.stderr)

if __name__ == "__main__":
    main()