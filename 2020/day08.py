import string

from parse import parse

from util.inputReader import read_as_strings
import re


def part1(my_input, inst_replace, inst_count):
    acc = 0
    i = 0
    seen = set()
    ct = 0
    while i < len(my_input):
        if i in seen:
            return -1
        seen.add(i)
        inst, n = parse("{:w} {:d}", my_input[i]).fixed
        if inst == "acc":
            acc += n
        elif inst == "jmp":
            if inst_replace == "jmp":
                ct += 1
                if inst_count != ct:
                    i += n - 1
            else:
                i += n - 1
        else:
            if inst_replace == "nop":
                ct += 1
                if inst_count == ct:
                    i += n - 1
        i += 1
    return acc


def part2(my_input):
    for i in range("".join(my_input).count("nop")):
        res = part1(my_input, "nop", i)
        if res != -1:
            return res

    for i in range("".join(my_input).count("jmp")):
        res = part1(my_input, "jmp", i)
        if res != -1:
            return res


inputs = read_as_strings("../inputs/2020_08.txt")
print(part2(inputs))
