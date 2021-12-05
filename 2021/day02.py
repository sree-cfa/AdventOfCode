from util.inputReader import read_as_strings
import re


def part1(list_of_strings):
    fwd = 0
    depth = 0
    for i in list_of_strings:
        inst, x = p.findall(i)[0]
        if inst == "forward":
            fwd += int(x)
        elif inst == "down":
            depth += int(x)
        elif inst == "up":
            depth -= int(x)
    return fwd * depth


def part2(list_of_strings):
    aim = 0
    fwd = 0
    depth = 0
    for i in list_of_strings:
        inst, x = p.findall(i)[0]
        if inst == "forward":
            fwd += int(x)
            depth += aim * int(x)
        elif inst == "down":
            aim += int(x)
        elif inst == "up":
            aim -= int(x)
    return fwd * depth



p = re.compile('(\\w+) (\\d+)')

lines = read_as_strings("../inputs/2021_02.txt")
print("part1:", part1(lines))
print("part2:", part2(lines))

# 1653 too low
