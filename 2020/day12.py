from util.inputReader import read_as_strings
import re


def part1(list_of_strings):
    x_dist = 0
    y_dist = 0

    facing = 1  # east
    for instructions in list_of_strings:
        (direction, distance) = p.findall(instructions)[0]
        if direction == 'R':
            facing = int((facing + int(distance) / 90) % 4)
        elif direction == 'L':
            facing = int((facing + 4 - int(distance) / 90) % 4)
        else:
            move_direction = facing
            if direction in rotations:
                move_direction = rotations.index(direction)

            move = cardinals[rotations[move_direction]]
            x_dist += move[0] * int(distance)
            y_dist += move[1] * int(distance)

    return abs(x_dist) + abs(y_dist)


def part2(list_of_strings):
    waypoint = (10, 1)
    x_dist = 0
    y_dist = 0

    facing = 1  # east
    for instructions in list_of_strings:
        (direction, distance) = p.findall(instructions)[0]
        if direction == 'R':
            facing = int((facing + int(distance) / 90) % 4)
        elif direction == 'L':
            facing = int((facing + 4 - int(distance) / 90) % 4)
        else:
            move_direction = facing
            if direction in rotations:
                move_direction = rotations.index(direction)

            move = cardinals[rotations[move_direction]]
            x_dist += move[0] * int(distance)
            y_dist += move[1] * int(distance)

    return abs(x_dist) + abs(y_dist)


p = re.compile('(\\w)(\\d+)')
cardinals = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
rotations = ['N', 'E', 'S', 'W']

lines = read_as_strings("../inputs/2020_12.txt")
print("part1:", part1(lines))
# print("part2:", part2(lines))

# 689 too low
