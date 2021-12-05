from collections import deque

from util.inputReader import read_as_strings


class Node:
    def __init__(self, i: int, p):
        self.idx = i
        self.path = p


def part1(my_input):
    total_rows = len(my_input)
    total_cols = len(my_input[0])
    rows = range(total_rows)
    cols = range(total_cols)

    inputs = []
    [inputs.append(list(x)) for x in my_input]
    changed = True
    while changed:
        # _print_seat_map(inputs)
        next_map = []
        changed = False
        for r in rows:
            next_map.append([])
            for c in cols:
                next_map[r].append(inputs[r][c])
                seats = {'#': 0, 'L': 0, '.': 0}
                if r > 0:
                    seats[inputs[r - 1][c]] += 1
                    if c > 0:
                        seats[inputs[r - 1][c - 1]] += 1
                    if c < total_cols - 1:
                        seats[inputs[r - 1][c + 1]] += 1
                if c > 0:
                    seats[inputs[r][c - 1]] += 1
                if c < total_cols - 1:
                    seats[inputs[r][c + 1]] += 1
                if r < total_rows - 1:
                    seats[inputs[r + 1][c]] += 1
                    if c > 0:
                        seats[inputs[r + 1][c - 1]] += 1
                    if c < total_cols - 1:
                        seats[inputs[r + 1][c + 1]] += 1
                if seats['#'] == 0 and inputs[r][c] == 'L':
                    changed = inputs[r][c] != '#'
                    next_map[r][c] = '#'
                elif seats['#'] >= 4 and inputs[r][c] == '#':
                    changed = inputs[r][c] != 'L'
                    next_map[r][c] = 'L'

        inputs = next_map

    count = 0
    for i in inputs:
        count += i.count('#')
    return count


def part2(my_input):
    total_rows = len(my_input)
    total_cols = len(my_input[0])
    rows = range(total_rows)
    cols = range(total_cols)

    inputs = []
    [inputs.append(list(x)) for x in my_input]
    changed = True
    while changed:
        # _print_seat_map(inputs)
        next_map = []
        changed = False
        for r in rows:
            next_map.append([])
            for c in cols:
                next_map[r].append(inputs[r][c])
                seats = {'#': 0, 'L': 0, '.': 0}
                if r > 0:
                    seats[inputs[r - 1][c]] += 1
                    if c > 0:
                        seats[inputs[r - 1][c - 1]] += 1
                    if c < total_cols - 1:
                        seats[inputs[r - 1][c + 1]] += 1
                if c > 0:
                    seats[inputs[r][c - 1]] += 1
                if c < total_cols - 1:
                    seats[inputs[r][c + 1]] += 1
                if r < total_rows - 1:
                    seats[inputs[r + 1][c]] += 1
                    if c > 0:
                        seats[inputs[r + 1][c - 1]] += 1
                    if c < total_cols - 1:
                        seats[inputs[r + 1][c + 1]] += 1
                if seats['#'] == 0 and inputs[r][c] == 'L':
                    changed = inputs[r][c] != '#'
                    next_map[r][c] = '#'
                elif seats['#'] >= 4 and inputs[r][c] == '#':
                    changed = inputs[r][c] != 'L'
                    next_map[r][c] = 'L'

        inputs = next_map

    count = 0
    for i in inputs:
        count += i.count('#')
    return count


def _print_seat_map(inputs):
    for i in inputs:
        print(" ".join(i))
    print()


seat_map = read_as_strings("../inputs/2020_11.txt")
print("part1:", part1(seat_map))
# print("part2:", part2(inputs))
