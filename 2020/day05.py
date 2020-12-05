from util.inputReader import read_as_strings
from parse import *


def part1and2(inputs):
    seats_open = [True for i in range(127 * 8)]
    max_id = 0
    for nav in inputs:
        row = _find_id(127, 0, 0, 7, nav, 'F')
        col = _find_id(7, 0, 7, 10, nav, 'L')
        this_id = row * 8 + col
        max_id = max(max_id, this_id)
        seats_open[this_id] = False
    print("part1: ", max_id)

    first_idx = seats_open.index(False)
    my_seat = seats_open.index(True, first_idx)
    print("part2: ", my_seat)


def _find_id(hi, lo, a, b, nav, ch):
    for i in range(a, b):
        if nav[i] == ch:
            hi = (hi + lo) / 2
        else:
            lo = (hi + lo) / 2
    return int(hi)


my_input = read_as_strings("../inputs/2020_05.txt")
part1and2(my_input)

