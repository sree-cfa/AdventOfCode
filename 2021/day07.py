def part1(numbers):
    min_fuel = 10000000

    for i in numbers:
        f = 0
        for j in numbers:
            f += abs(i - j)
        min_fuel = min(f, min_fuel)

    return min_fuel


def part2(numbers):
    min_fuel = 100000000000

    for j in range(max(numbers)):
        f = 0
        for i in numbers:
            n = abs(i - j)
            f += n * (n + 1) / 2
        min_fuel = min(f, min_fuel)

    return int(min_fuel)


heights = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

print("part1:", part1(heights))
print("part2:", part2(heights))
