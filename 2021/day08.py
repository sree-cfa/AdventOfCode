from util.inputReader import read_as_strings


def part1():
    count = 0

    for i in lines:
        code, output = i.split(" | ")
        lens = map(lambda x: len(x), output.split())
        for l in lens:
            if l in (2, 3, 4, 7):
                count += 1

    return count


def part2():
    sum_of_outputs = 0
    for i in lines:
        code, output = i.split(" | ")
        wires = {}
        wire_to_nums = {}
        while len(wires) < 10:
            for c in code.split():
                c_len = len(c)
                c_set = sorted(c)
                if c_len == 2:  # 1
                    wire_to_nums[1] = c_set
                    wires[''.join(c_set)] = 1
                elif c_len == 4:  # 4
                    wire_to_nums[4] = c_set
                    wires[''.join(c_set)] = 4
                elif c_len == 3:  # 7
                    wire_to_nums[7] = c_set
                    wires[''.join(c_set)] = 7
                elif c_len == 7:  # 8
                    wire_to_nums[8] = c_set
                    wires[''.join(c_set)] = 8
                elif c_len == 6:  # 0, 6, 9
                    if 4 in wire_to_nums and all(elem in c_set for elem in wire_to_nums[4]):
                        wire_to_nums[9] = c_set
                        wires[''.join(c_set)] = 9
                    elif 7 in wire_to_nums and all(elem in c_set for elem in wire_to_nums[7]):
                        wire_to_nums[0] = c_set
                        wires[''.join(c_set)] = 0
                    elif 4 in wire_to_nums and 7 in wire_to_nums:
                        wire_to_nums[6] = c_set
                        wires[''.join(c_set)] = 6
                elif c_len == 5:  # 2, 3, 5
                    if 7 in wire_to_nums and all(elem in c_set for elem in wire_to_nums[7]):
                        wire_to_nums[3] = c_set
                        wires[''.join(c_set)] = 3
                    elif 6 in wire_to_nums and all(elem in wire_to_nums[6] for elem in c_set):
                        wire_to_nums[5] = c_set
                        wires[''.join(c_set)] = 5
                    elif 6 in wire_to_nums and 7 in wire_to_nums:
                        wire_to_nums[2] = c_set
                        wires[''.join(c_set)] = 2
        outputs_formatted = list(map(lambda x: ''.join(sorted(x)), output.split()))
        sum_of_output = wires[outputs_formatted[0]] * 1000 + \
                        wires[outputs_formatted[1]] * 100 + \
                        wires[outputs_formatted[2]] * 10 + \
                        wires[outputs_formatted[3]]
        sum_of_outputs += sum_of_output
    return sum_of_outputs


lines = read_as_strings("../inputs/2021_08.txt")

print("part1:", part1())
print("part2:", part2())  # 981149 too low
