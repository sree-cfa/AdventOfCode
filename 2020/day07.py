from util.inputReader import read_as_strings
from parse import *


def part1and2(inputs):
    bags_contains_map = {}
    bags_contained_by_map = {}

    for rules in inputs:
        this_bag, contains_bags = rules.split(" bags contain ")
        for bag in contains_bags.split(","):
            bag = bag.strip()
            count, bag_type = parse("{} {} b{:w}", bag).fixed[0:2]
            if count != "no":
                if bags_contains_map.get(this_bag) is None:
                    bags_contains_map[this_bag] = []
                bags_contains_map[this_bag].append((int(count), bag_type))
            if bags_contained_by_map.get(bag_type) is None:
                bags_contained_by_map[bag_type] = []
            bags_contained_by_map[bag_type].append(this_bag)

    seen = set()
    bag_list = list()
    bag_list.extend(bags_contained_by_map["shiny gold"])
    for bag in bag_list:
        if bag != "other" and bags_contained_by_map.get(bag) is not None:
            next_bags = bags_contained_by_map[bag]
            bag_list.extend(next_bags)
        seen.add(bag)

    print("part1: ", len(seen))
    print("part2: ", _count_bags(bags_contains_map, bags_contains_map["shiny gold"]))


def _count_bags(bags_contains_map, bag_map):
    if bag_map is None:
        return 0

    count = 0
    for ct, bag in bag_map:
        count += int(ct)
        count += int(ct) * _count_bags(bags_contains_map, bags_contains_map.get(bag))

    return count


# removed '.' characters from input
my_input = read_as_strings("../inputs/2020_07.txt")
part1and2(my_input)
