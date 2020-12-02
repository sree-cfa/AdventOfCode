from util.inputReader import read_as_strings
import re


def part1and2(my_input):
    count1, count2 = 0, 0
    for s in my_input:
        matches = p.findall(s)
        a = int(matches[0])
        b = int(matches[1])
        c = matches[2][0]
        s = matches[3]

        char_count = s.count(c)
        if a <= char_count <= b:
            count1 += 1

        if (s[a - 1] == c) != (s[b - 1] == c):
            count2 += 1

    print("part1", count1)
    print("part2", count2)


p = re.compile('\\d+|\\w:|\\w\\w+')

inputs = read_as_strings("../inputs/2020_02.txt")
part1and2(inputs)
