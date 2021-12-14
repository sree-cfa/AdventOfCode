from util.inputReader import read_as_strings
from collections import deque


def part1():
    flash_count = 0
    for step in range(100):
        print(step)
        for ri in range(1, 11):
            print(''.join(map(lambda x: str(x), lines[ri][1:-1])))

        for ri in range(1, 11):
            rn = lines[ri]
            for ci in range(1, 11):
                rn[ci] = rn[ci] + 1

        no_change = False
        while not no_change:
            no_change = True
            for ri in range(1, 11):
                rn = lines[ri]
                for ci in range(1, 11):
                    if rn[ci] > 9:
                        flash_count += 1
                        no_change = False
                        rn[ci] = 0
                        rn[ci - 1] = rn[ci - 1] if rn[ci - 1] == 0 else rn[ci - 1] + 1
                        rn[ci + 1] = rn[ci + 1] if rn[ci + 1] == 0 else rn[ci + 1] + 1
                        lines[ri - 1][ci] = lines[ri - 1][ci] if lines[ri - 1][ci] == 0 else lines[ri - 1][ci] + 1
                        lines[ri + 1][ci] = lines[ri + 1][ci] if lines[ri + 1][ci] == 0 else lines[ri + 1][ci] + 1
                        lines[ri - 1][ci - 1] = lines[ri - 1][ci - 1] \
                            if lines[ri - 1][ci - 1] == 0 else lines[ri - 1][ci - 1] + 1
                        lines[ri + 1][ci - 1] = lines[ri + 1][ci - 1] \
                            if lines[ri + 1][ci - 1] == 0 else lines[ri + 1][ci - 1] + 1
                        lines[ri - 1][ci + 1] = lines[ri - 1][ci + 1] \
                            if lines[ri - 1][ci + 1] == 0 else lines[ri - 1][ci + 1] + 1
                        lines[ri + 1][ci + 1] = lines[ri + 1][ci + 1] \
                            if lines[ri + 1][ci + 1] == 0 else lines[ri + 1][ci + 1] + 1

    for ri in range(1, 11):
        print(''.join(map(lambda x: str(x), lines[ri][1:-1])))
    return flash_count


def part2():
    all_zeroes = False
    step = 100
    while not all_zeroes:
        for ri in range(1, 11):
            rn = lines[ri]
            for ci in range(1, 11):
                rn[ci] = rn[ci] + 1

        no_change = False
        while not no_change:
            no_change = True
            for ri in range(1, 11):
                rn = lines[ri]
                for ci in range(1, 11):
                    if rn[ci] > 9:
                        no_change = False
                        rn[ci] = 0
                        rn[ci - 1] = rn[ci - 1] if rn[ci - 1] == 0 else rn[ci - 1] + 1
                        rn[ci + 1] = rn[ci + 1] if rn[ci + 1] == 0 else rn[ci + 1] + 1
                        lines[ri - 1][ci] = lines[ri - 1][ci] if lines[ri - 1][ci] == 0 else lines[ri - 1][ci] + 1
                        lines[ri + 1][ci] = lines[ri + 1][ci] if lines[ri + 1][ci] == 0 else lines[ri + 1][ci] + 1
                        lines[ri - 1][ci - 1] = lines[ri - 1][ci - 1] \
                            if lines[ri - 1][ci - 1] == 0 else lines[ri - 1][ci - 1] + 1
                        lines[ri + 1][ci - 1] = lines[ri + 1][ci - 1] \
                            if lines[ri + 1][ci - 1] == 0 else lines[ri + 1][ci - 1] + 1
                        lines[ri - 1][ci + 1] = lines[ri - 1][ci + 1] \
                            if lines[ri - 1][ci + 1] == 0 else lines[ri - 1][ci + 1] + 1
                        lines[ri + 1][ci + 1] = lines[ri + 1][ci + 1] \
                            if lines[ri + 1][ci + 1] == 0 else lines[ri + 1][ci + 1] + 1

        all_zeroes = True
        for ri in range(1, 11):
            if lines[ri].count(0) != 12:
                all_zeroes = False
        step += 1
    return step


lines = list()
lines.append([0] * 12)
input = read_as_strings("../inputs/2021_11.txt")

for l in input:
    lines.append([0] + list(map(lambda x: int(x), l)) + [0])

lines.append([0] * 12)

print("part1:", part1())  # 1263 too low
print("part2:", part2())
