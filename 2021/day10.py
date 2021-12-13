from util.inputReader import read_as_strings
from collections import deque


def part1():
    error_score = 0
    for line in lines:
        error_score += get_error_score(line)
    return error_score


def get_error_score(line):
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    closed = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }

    queue = deque()
    for c in line:
        if c in closed.values():
            queue.append(c)
        else:
            last_char = queue.pop()
            if last_char != closed[c]:
                return points[c]

    return 0


def part2():
    scores = list()
    for line in lines:
        score = get_incomplete_score(line)
        if score != -1:
            scores.append(score)
    scores = sorted(scores)
    return scores[int(len(scores) / 2)]


def get_incomplete_score(line):
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    closed = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    opened = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    queue = deque()
    for c in line:
        if c in closed.values():
            queue.append(c)
        else:
            last_char = queue.pop()
            if last_char != closed[c]:
                return -1

    score = 0
    queue.reverse()
    for c in queue:
        score = score * 5 + points[opened[c]]
    return score


lines = read_as_strings("../inputs/2021_10.txt")

print("part1:", part1())
print("part2:", part2())
