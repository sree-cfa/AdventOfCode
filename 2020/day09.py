from util.inputReader import read_as_ints


def part1(list_of_ints):
    preamble = 25

    for i, _ in enumerate(list_of_ints):
        seen = set()
        my_sum = list_of_ints[i + preamble]
        found_values = False
        for j in range(i, i + preamble):
            v = list_of_ints[j]
            seen.add(v)
            if (my_sum - v) in seen:
                found_values = True
                break
        if not found_values:
            return my_sum


def part2(list_of_ints):
    part1_ans = 1212510616
    total, start, stop = list_of_ints[0], 0, 0
    while total != part1_ans:
        if total > part1_ans:
            start += 1
            stop = start
            total = list_of_ints[start]
        else:
            stop += 1
            total += list_of_ints[stop]
    subarr = list_of_ints[start:stop + 1]
    return max(subarr) + min(subarr)


inputs = read_as_ints("../inputs/2020_09.txt")
print("part1:", part1(inputs))
print("part2:", part2(inputs))
