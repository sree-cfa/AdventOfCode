from collections import deque

from util.inputReader import read_as_ints


class Node:
    def __init__(self, i: int, p):
        self.idx = i
        self.path = p


def part1(jolts):
    jolts.sort()
    diff3 = 1
    diff1 = 1
    for i, v in enumerate(jolts):
        if i > 0:
            if jolts[i - 1] == v - 1:
                diff1 += 1
            elif jolts[i - 1] == v - 3:
                diff3 += 1

    return diff3 * diff1


def _get_next_indices(idx, jolts):
    res = []
    for i, v in enumerate(jolts[idx + 1:]):
        if v - jolts[idx] <= 3:
            res.append(idx + 1 + i)
    return res


def part2(jolts):
    jolts.sort()

    seen = set()
    last_idx = len(jolts) - 1
    queue = deque()
    queue.append(Node(0, "(0)"))
    path_ct = 0
    while len(queue) > 0:
        node = queue.pop()
        if node.idx >= last_idx:
            path_ct += 1
        else:

            next_idxs = _get_next_indices(node.idx, jolts)

            for next_idx in next_idxs:
                next_path = node.path + ", " + str(next_idx)
                if next_path not in seen:
                    queue.append(Node(next_idx, next_path))
                    seen.add(next_path)

    full_paths = []
    last_jolt = jolts[-1]
    for x in seen:
        rindex_ = x[x.rindex(' '):]
        if last_jolt - jolts[int(rindex_)] <= 3:
            full_paths.append(x)

    return path_ct


inputs = read_as_ints("../inputs/2020_10.txt")
# print("part1:", part1(inputs))
print("part2:", part2(inputs))
