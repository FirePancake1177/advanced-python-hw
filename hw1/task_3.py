#!/usr/bin/env python3
import sys

def wc(file):
    lines = words = bytes_count = 0
    for line in file:
        lines += 1
        words += len(line.split())
        bytes_count += len(line.encode())
    return lines, words, bytes_count

def print_counts(lines, words, bytes_count, filename=''):
    print(f"{lines:7} {words:7} {bytes_count:7}" + (f" {filename}" if filename else ""))

def main():
    if len(sys.argv) == 1:
        lines, words, bytes_count = wc(sys.stdin)
        print_counts(lines, words, bytes_count)
    else:
        total_lines = total_words = total_bytes = 0
        for filename in sys.argv[1:]:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    lines, words, bytes_count = wc(f)
                    total_lines += lines
                    total_words += words
                    total_bytes += bytes_count
                    print_counts(lines, words, bytes_count, filename)
            except FileNotFoundError:
                print(f"wc.py: {filename}: No such file or directory", file=sys.stderr)
        if len(sys.argv) > 2:
            print_counts(total_lines, total_words, total_bytes, 'total')

if __name__ == "__main__":
    main()