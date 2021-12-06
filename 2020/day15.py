from util.inputReader import *


def part1(numbers):
    spoken_turn = {}
    spoken_count = {}
    last_spoken = 0
    for i, num in enumerate(numbers):
        spoken_turn[num] = i+1
        spoken_count[num] = 1
        last_spoken = num

    starting_numbers_length = len(numbers)
    for turn in range(starting_numbers_length, 2020):
        last_spoken_count = spoken_count[last_spoken]
        if last_spoken_count == 1:
            last_spoken = 0
        else:
            last_spoken = spoken_turn[last_spoken] - (last_spoken_count - 1)

        if last_spoken not in spoken_count:
            spoken_count[last_spoken] = 0
        spoken_count[last_spoken] += 1
        spoken_turn[last_spoken] = turn + 1

    return last_spoken


print("part1:", part1([0, 3, 6]))
print("part1:", part1([18, 11, 9, 0, 5, 1]))

# print("part2:", part2(lines))
