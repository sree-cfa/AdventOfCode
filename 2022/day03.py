from util.inputReader import read_as_strings


def part1(list_of_strings):
    result = 0
    for string in list_of_strings:
        comp_size = int(len(string) / 2)
        e = set(string[0:comp_size]).intersection(set(string[comp_size:])).pop()
        p = ord(e)
        result = result + p - (96 if p > 90 else 38)
    return result


def part2(list_of_strings):
    i = 0
    result = 0
    while i < len(list_of_strings):
        sack1 = set(list_of_strings[i])
        sack2 = set(list_of_strings[i + 1])
        sack3 = set(list_of_strings[i + 2])
        e = sack1.intersection(sack2).intersection(sack3).pop()
        p = ord(e)
        result = result + p - (96 if p > 90 else 38)

        i += 3
    return result


lines = read_as_strings("../inputs/2022_03.txt")
print("part1:", part1(lines))
print("part2:", part2(lines))
