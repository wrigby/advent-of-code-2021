#!/usr/bin/env python3

import sys


def main():
    previous = 0
    increases = -1
    for line in sys.stdin:
        value = int(line)
        if value > previous:
            increases += 1
        previous = value
    print(increases)


if __name__ == "__main__":
    main()
