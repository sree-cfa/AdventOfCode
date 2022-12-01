from util.inputReader import *


def part1(input_list):
    max_calories = 0
    curr_calories = 0
    for line in input_list:
        if line == '':
            max_calories = max(curr_calories, max_calories)
            curr_calories = 0
        else:
            curr_calories = curr_calories + int(line)
    return max_calories


def part2(input_list):
    max_calories = []
    curr_calories = 0
    for line in input_list:
        if line == '':
            max_calories.append(curr_calories)
            curr_calories = 0
        else:
            curr_calories = curr_calories + int(line)
    max_calories.sort()
    max_calories.reverse()
    return sum(max_calories[0:3])


lines = read_as_strings("../inputs/2022_01.txt")
print("part1:", part1(lines))
print("part2:", part2(lines))
