from util.inputReader import *
import re


def part1_and_part2(numbers, days):
    fish_count = {}
    for n in numbers:
        new_count = 1
        if n in fish_count:
            new_count += fish_count[n]
        fish_count[n] = new_count

    for turn in range(days):
        next_iteration = {}
        for entry in fish_count:
            next_fish = entry - 1
            if entry == 0:
                next_fish = 6
                next_iteration[8] = fish_count[entry]
            if next_fish in next_iteration:
                next_iteration[next_fish] += fish_count[entry]
            else:
                next_iteration[next_fish] = fish_count[entry]
        fish_count = next_iteration

    total_fish = 0
    for entry in fish_count:
        total_fish += fish_count[entry]
    return total_fish


starting_numbers = [5, 1, 1, 5, 4, 2, 1, 2, 1, 2, 2, 1, 1, 1, 4, 2, 2, 4, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 5, 3, 1, 4,
                    1, 1, 1, 1, 1, 4, 1, 5, 1, 1, 1, 4, 1, 2, 2, 3, 1, 5, 1, 1, 5, 1, 1, 5, 4, 1, 1, 1, 4, 3, 1, 1, 1,
                    3, 1, 5, 5, 1, 1, 1, 1, 5, 3, 2, 1, 2, 3, 1, 5, 1, 1, 4, 1, 1, 2, 1, 5, 1, 1, 1, 1, 5, 4, 5, 1, 3,
                    1, 3, 3, 5, 5, 1, 3, 1, 5, 3, 1, 1, 4, 2, 3, 3, 1, 2, 4, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 4, 1, 3, 2,
                    5, 2, 1, 1, 1, 4, 2, 1, 1, 1, 4, 2, 4, 1, 1, 1, 1, 4, 1, 3, 5, 5, 1, 2, 1, 3, 1, 1, 4, 1, 1, 1, 1,
                    2, 1, 1, 4, 2, 3, 1, 1, 1, 1, 1, 1, 1, 4, 5, 1, 1, 3, 1, 1, 2, 1, 1, 1, 5, 1, 1, 1, 1, 1, 3, 2, 1,
                    2, 4, 5, 1, 5, 4, 1, 1, 3, 1, 1, 5, 5, 1, 3, 1, 1, 1, 1, 4, 4, 2, 1, 2, 1, 1, 5, 1, 1, 4, 5, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 4, 2, 1, 1, 1, 2, 5, 1, 4, 1, 1, 1, 4, 1, 1, 5, 4, 4, 3,
                    1, 1, 4, 5, 1, 1, 3, 5, 3, 1, 2, 5, 3, 4, 1, 3, 5, 4, 1, 3, 1, 5, 1, 4, 1, 1, 4, 2, 1, 1, 1, 3, 2,
                    1, 1, 4]
# starting_numbers = [3, 4, 3, 1, 2]
print("part1:", part1_and_part2(starting_numbers, 80))
print("part2:", part1_and_part2(starting_numbers, 256))
