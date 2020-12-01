from util.inputReader import read_as_ints


def part1(list_of_ints):
    seen = set()
    for i in list_of_ints:
        if (2020 - i) in seen:
            return i * (2020 - i)
        else:
            seen.add(i)
    return -1


def part2(list_of_ints):
    for index, j in enumerate(list_of_ints):
        seen = set()
        for i in list_of_ints[index:]:
            if (2020 - i - j) in seen:
                return i * (2020 - i - j) * j
            else:
                seen.add(i)
    return -1


input = read_as_ints("../inputs/2020_01.txt")
print("part1:", part1(input))
print("part2:", part2(input))
