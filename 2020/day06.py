from util.inputReader import read_as_strings
from parse import *


def part1and2(inputs):
    count1, count2 = 0, 0
    yes_answers1 = set()
    yes_answers2 = set()
    is_new_set = True
    for nav in inputs:
        if nav == "":
            count1 += len(yes_answers1)
            count2 += len(yes_answers2)
            yes_answers1.clear()
            yes_answers2.clear()
            is_new_set = True
        else:
            s = set(nav)
            if is_new_set:
                yes_answers2 = s
            else:
                yes_answers2 = yes_answers2.intersection(s)

            is_new_set = False
            yes_answers1 = yes_answers1 | s

    print("part1: ", count1 + len(yes_answers1))
    print("part2: ", count2 + len(yes_answers2))


my_input = read_as_strings("../inputs/2020_06.txt")
part1and2(my_input)

