from util.inputReader import read_as_strings
from collections import deque


def part1(dots):
    s = range(1500)
    grid = [['.' for _x in s] for _y in s]

    dots = list(map(lambda x: eval(x), dots))

    for s in splits:
        dir, num = s.split('=')
        num = int(num)
        new_dots = list()
        for c, r in dots:
            grid[r][c] = '.'
            if dir == 'y' and r > num:
                r = 2 * num - r
            if dir == 'x' and c > num:
                c = 2 * num - c
            if (c, r) not in new_dots:
                new_dots.append((c, r))
            grid[r][c] = '#'
        dots = new_dots

    for i in range(6):
        print(' '.join(grid[i][:50]))
    return 0


lines = read_as_strings("../inputs/2021_13.txt")
split_idx = lines.index("")
dots = lines[0:split_idx]
splits = lines[split_idx + 1:]

print("part1:", part1(dots))
