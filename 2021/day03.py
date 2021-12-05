from util.inputReader import read_as_strings

LENGTH = 12


def part1(list_of_strings):
    one_count = [0] * LENGTH
    zero_count = [0] * LENGTH

    for string in list_of_strings:
        for i, val in enumerate(string):
            if val == '0':
                zero_count[i] += 1
            else:
                one_count[i] += 1

    epsilon = ""
    gamma = ""

    for i in range(LENGTH):
        if one_count[i] >= zero_count[i]:
            epsilon += '1'
            gamma += '0'
        else:
            epsilon += '0'
            gamma += '1'

    return int(epsilon, 2) * int(gamma, 2)


def part2(numbers):

    ogr_str = ""
    co2_str = ""
    ogr_bin, co2_bin = 0, 0
    for i in range(LENGTH):
        ogr_count_0, ogr_count_1 = 0, 0
        co2_count_0, co2_count_1 = 0, 0
        for number in numbers:
            if number.startswith(ogr_str):
                ogr_count_0 += 1 if number[i] == '0' else 0
                ogr_count_1 += 1 if number[i] == '1' else 0
            if number.startswith(co2_str):
                co2_count_0 += 1 if number[i] == '0' else 0
                co2_count_1 += 1 if number[i] == '1' else 0

        if ogr_count_1 + ogr_count_0 == 1:  # one number left
            ogr_str = next(filter(lambda x: x.startswith(ogr_str), numbers))
            ogr_bin = int(ogr_str, 2)
        if co2_count_1 + co2_count_0 == 1:  # one number left
            co2_str = next(filter(lambda x: x.startswith(co2_str), numbers))
            co2_bin = int(co2_str, 2)

        ogr_str += '1' if ogr_count_1 >= ogr_count_0 else '0'
        co2_str += '0' if co2_count_1 >= co2_count_0 else '1'

    if ogr_bin == 0:
        ogr_bin = int(ogr_str, 2)
    if co2_bin == 0:
        co2_bin = int(co2_str, 2)

    return ogr_bin * co2_bin


lines = read_as_strings("../inputs/2021_03.txt")
print("part1:", part1(lines))
print("part2:", part2(lines))

# part2 12723489 too high
