#!/usr/bin/env python3

import sys


def main():
    horizontal_position = 0
    depth = 0

    for line in sys.stdin:
        direction, amount = line.strip().split()
        amount = int(amount)
        if direction == "up":
            depth -= amount
        elif direction == "down":
            depth += amount
        elif direction == "forward":
            horizontal_position += amount
    
    print(f"Hor: {horizontal_position}, depth: {depth}, product: {horizontal_position * depth}")


if __name__ == "__main__":
    main()
