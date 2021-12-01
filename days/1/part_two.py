#!/usr/bin/env python3

import sys
from typing import Callable, Iterable


class SlidingWindow:
    """Wrapper iterator to provide a sliding-window aggregation

    This can be accomplished more easily using itertools.tee, but I didn't realize that
    at the time, and wanted to play with writing my own iterable to do it.
    """

    def __init__(
        self, iterator: Iterable, window_size: int, aggregation_function: Callable
    ):
        self.wrapped_iter = iterator
        self.window_size = window_size
        self.aggregation_function = aggregation_function
        # Prime the window buffer by pulling in n-1 values from the wrapped iterator,
        # placing a 0 in the last position, and setting the write cursow to that position
        self.window = [next(iterator) for i in range(window_size - 1)]
        self.window.append(0)
        self.position = self.window_size - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.window[self.position % self.window_size] = next(self.wrapped_iter)
        self.position += 1
        return self.aggregation_function(self.window)


def main():
    windowed = SlidingWindow(
        iterator=(int(l) for l in sys.stdin),
        window_size=3,
        aggregation_function=sum,
    )
    previous = 0
    increases = -1
    for value in windowed:
        if value > previous:
            increases += 1
        previous = value
    print(increases)


if __name__ == "__main__":
    main()
