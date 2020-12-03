from util.inputReader import read_as_strings


def part1(slope_grid):
    trees = 0
    slope = 1

    for i, line in enumerate(slope_grid):
        if i % 2 == 0 and line[(int(i / 2) * slope) % len(line)] == '#':
            trees += 1
    return trees


grid = read_as_strings("../inputs/2020_03.txt")
print("part1:", part1(grid))
print("part2:", 278 * 90 * 88 * 98 * 45)
