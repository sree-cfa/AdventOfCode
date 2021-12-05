from util.inputReader import *


def part1(list_of_ints):
    inc_count = 0
    prev = max(list_of_ints)
    for i in list_of_ints:
        if prev < i:
            inc_count += 1
        prev = i
    return inc_count


def part2(list_of_ints):
    inc_count = 0
    n = len(list_of_ints)
    prev = sum(list_of_ints[0:3])
    for i in range(2, n - 1):
        new_sum = prev - list_of_ints[i - 2] + list_of_ints[i + 1]
        if prev < new_sum:
            inc_count += 1
        prev = new_sum

    return inc_count


lines = read_as_ints("../inputs/2021_01.txt")
print("part1:", part1(lines))
print("part2:", part2(lines))

# 1653 too low
