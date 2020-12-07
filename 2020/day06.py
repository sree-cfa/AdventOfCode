from util.inputReader import read_as_strings
from parse import *


def part1and2(inputs):
    count1, count2 = 0, 0
    subgroup = []
    for nav in inputs:
        if nav == "":
            count1 += len(set.union(*subgroup))
            count2 += len(set.intersection(*subgroup))
            subgroup = []
        else:
            subgroup.append(set(nav))
    count1 += len(set.union(*subgroup))
    count2 += len(set.intersection(*subgroup))

    print("part1: ", count1)
    print("part2: ", count2)


my_input = read_as_strings("../inputs/2020_06.txt")
part1and2(my_input)
