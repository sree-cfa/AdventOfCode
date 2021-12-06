from util.inputReader import *
import re


def part1(lines):
    s = range(1000)
    grid = [[0 for _x in s] for _y in s]

    for line in lines:
        x1, y1, x2, y2 = map(lambda n: int(n), p.findall(line)[0])
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1][x] += 1
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[y][x1] += 1

    overlaps = 0
    for y in s:
        for x in s:
            if grid[y][x] > 1:
                overlaps += 1
    return overlaps


def part2(lines):
    s = range(1000)
    grid = [[0 for _x in s] for _y in s]

    for line in lines:
        x1, y1, x2, y2 = map(lambda n: int(n), p.findall(line)[0])

        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1][x] += 1
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[y][x1] += 1
        elif x1 > x2 and y1 < y2:
            for x in range(x2, x1 + 1):
                y = y2 - (x - x2)
                grid[y][x] += 1
        elif x1 > x2 and y1 > y2:
            for x in range(x2, x1 + 1):
                y = y2 + (x - x2)
                grid[y][x] += 1
        elif x1 < x2 and y1 < y2:
            for x in range(x1, x2 + 1):
                y = y1 + (x - x1)
                grid[y][x] += 1
        elif x1 < x2 and y1 > y2:
            for x in range(x1, x2 + 1):
                y = y1 - (x - x1)
                grid[y][x] += 1

    overlaps = 0
    for y in s:
        for x in s:
            if grid[y][x] > 1:
                overlaps += 1
    return overlaps


p = re.compile('(\\d+),(\\d+) -> (\\d+),(\\d+)')
lines = read_as_strings("../inputs/2021_05.txt")
print("part1:", part1(lines))
print("part2:", part2(lines))

# 17864 too low
