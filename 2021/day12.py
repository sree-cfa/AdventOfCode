from util.inputReader import *
from collections import deque
import re


def part1():
    connections = {}
    for line in lines:
        x, y = line.split('-')
        ys = connections[x] if x in connections else list()
        ys.append(y)
        connections[x] = ys

        if x != 'start' and y != 'end':
            xs = connections[y] if y in connections else list()
            xs.append(x)
            connections[y] = xs

    path_count = 0
    queue = deque()
    queue.append(',start')

    while len(queue) > 0:
        last_path = queue.pop()
        caves = last_path.split(',')
        last_cave = caves[len(caves) - 1]

        if last_cave in connections:
            next_caves = connections[last_cave]

            for next_cave in next_caves:
                if next_cave == 'end':
                    path_count += 1
                    print(last_path + "," + next_cave)
                elif next_cave not in caves or re.match("[A-Z]+", next_cave):
                    queue.append(last_path + "," + next_cave)

    return path_count

def part2():
    connections = {}
    for line in lines:
        x, y = line.split('-')
        ys = connections[x] if x in connections else list()
        ys.append(y)
        connections[x] = ys

        if x != 'start' and y != 'end':
            xs = connections[y] if y in connections else list()
            xs.append(x)
            connections[y] = xs

    path_count = 0
    queue = deque()
    queue.append(',start')

    while len(queue) > 0:
        last_path = queue.pop()
        caves = last_path.split(',')
        last_cave = caves[len(caves) - 1]

        if last_cave in connections:
            next_caves = connections[last_cave]

            for next_cave in next_caves:
                if next_cave == 'end':
                    path_count += 1
                    print(last_path + "," + next_cave)
                elif next_cave not in caves or re.match("[A-Z]+", next_cave):
                    queue.append(last_path + "," + next_cave)
                else:
                    counts = map(lambda x: 0 if re.match("[A-Z]+", x) else caves.count(x), caves)
                    if 2 not in counts:
                        queue.append(last_path + "," + next_cave)

    return path_count


lines = read_as_strings("../inputs/2021_12.txt")

print("part1:", part1())
print("part2:", part2())
