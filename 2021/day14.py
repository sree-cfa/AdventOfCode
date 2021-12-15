from util.inputReader import read_as_strings


def part1and2(steps):
    formula_counts = {}
    for i in range(len(template) - 1):
        update_count(1, template[i:i + 2], formula_counts)

    rules = {}
    for r in rule_lines:
        pair, poly_insert = r.split(" -> ")
        rules[pair] = poly_insert

    for step in range(steps):
        new_formula_counts = {}
        for pair in formula_counts:
            pair_count = formula_counts[pair]
            poly_insert = rules[pair]
            update_count(pair_count, pair[0] + poly_insert, new_formula_counts)
            update_count(pair_count, poly_insert + pair[1], new_formula_counts)
        formula_counts = new_formula_counts

    poly_count = {}
    for pair in formula_counts:
        pair_count = formula_counts[pair]
        update_count(pair_count, pair[0], poly_count)
        update_count(pair_count, pair[1], poly_count)

    max_count = max(poly_count.values()) / 2
    min_count = min(poly_count.values()) / 2
    print(max_count, min_count)
    return int(max_count - min_count)


def update_count(num, key, count_map):
    if key not in count_map:
        count_map[key] = 0
    count_map[key] += num


lines = read_as_strings("../inputs/2021_14.txt")
template = lines[0]
rule_lines = lines[2:]

print("part1:", part1and2(10))
print("part2:", part1and2(40))
