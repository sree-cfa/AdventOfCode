from util.inputReader import *
import re


def part1(list_of_strings):
    count = 0

    for string in list_of_strings:
        a1, a2, b1, b2 = map(int, p.findall(string)[0])
        if a1 >= b1 and a2 <= b2:
            count += 1
        elif a1 <= b1 and a2 >= b2:
            count += 1

    return count


def part2(list_of_strings):
    count = 0

    for string in list_of_strings:
        a1, a2, b1, b2 = map(int, p.findall(string)[0])
        if a1 <= b1 <= a2:
            count += 1
        elif a1 <= b2 <= a2:
            count += 1
        elif b1 <= a1 <= b2:
            count += 1
        elif b1 <= a2 <= b2:
            count += 1

    return count


p = re.compile('(\\d+)-(\\d+),(\\d+)-(\\d+)')

lines = read_as_strings("../inputs/2022_04.txt")

print("part1:", part1(lines))
print("part2:", part2(lines))
