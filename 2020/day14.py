from collections import deque

from parse import parse

from util.inputReader import read_as_strings


class Node:
    def __init__(self, i: int, p):
        self.idx = i
        self.path = p


def part1(my_input):
    memory = {}
    mask = []
    for comm in my_input:
        if comm.startswith("mem"):
            addr, val = parse("mem[{}] = {}", comm).fixed
            val = list(bin(int(val)))
            val[1] = '0'
            val = ['0'] * (36 - len(val)) + val
            for i, c in enumerate(val):
                if mask[i] != 'X':
                    val[i] = mask[i]

            memory[int(addr)] = int("".join(val), 2)
        else:
            mask = list(parse("mask = {}", comm).fixed[0])

    return sum(memory.values())


def part2(my_input):
    memory = {}
    mask = []
    for comm in my_input:
        if comm.startswith("mem"):
            addr, val = parse("mem[{}] = {}", comm).fixed
            val = list(bin(int(val)))
            val[1] = '0'
            val = ['0'] * (36 - len(val)) + val

            q = deque()
            q.append(mask)

            while len(q) > 0:
                contains_x = False
                val_i = q.pop()
                for i, c in enumerate(val):
                    if mask[i] == 'X':
                        contains_x = True
                        val_i[i] = '0'
                        q.append(val_i.deepcopy())
                        val_i[i] = '1'
                        q.append(val_i.deepcopy())

                if not contains_x:

                    memory[int(addr)] = int("".join(val), 2)
        else:
            mask = list(parse("mask = {}", comm).fixed[0])

    return sum(memory.values())


# too high 16363683105667
commands = read_as_strings("../inputs/2020_14.txt")
# print("part1:", part1(commands))
print("part2:", part2(commands))
