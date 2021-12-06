from util.inputReader import *


def part1(time, ids):
    earliest = time * 2
    earliest_id = -1
    for bus_id in ids:
        if time % bus_id == 0:
            return 0  # no wait time

        closest_time = (int(time / bus_id) + 1) * bus_id
        if earliest > closest_time:
            earliest = closest_time
            earliest_id = bus_id

    return earliest_id * (earliest - time)


lines = read_as_strings("../inputs/2020_13.txt")
print("part1:", part1(1000104, [41, 37, 659, 23, 13, 19, 29, 937, 17]))

# print("part2:", part2(lines))
