from util.inputReader import read_as_strings
from parse import *
import re


def part1and2(passports):
    req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    seen = {True: set(), False: set()}
    valid1, valid2 = 0, 0
    for key_val in passports:
        if key_val == "":
            if (seen[True] | seen[False]).issuperset(req):
                valid1 += 1
            if seen[True].issuperset(req):
                valid2 += 1

            seen[True].clear()
            seen[False].clear()
        else:
            k, v = key_val.split(':')

            if k in req:
                add_key = False

                if k == "byr":
                    add_key = 1920 <= int(v) <= 2002
                elif k == "iyr":
                    add_key = 2010 <= int(v) <= 2020
                elif k == "eyr":
                    add_key = 2020 <= int(v) <= 2030
                elif k == "hgt":
                    if len(v) > 2:
                        vint = int(v[:-2])
                        if v[-2:] == "cm":
                            add_key = 150 <= vint <= 193
                        elif v[-2:] == "in":
                            add_key = 59 <= vint <= 76
                elif k == "hcl":
                    p = re.compile('#[\\d|a-f]{6}')
                    add_key = p.match(v) is not None
                elif k == "ecl":
                    add_key = v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                elif k == "pid":
                    p = re.compile('\\d{9}')
                    add_key = p.match(v) is not None

                seen[add_key].add(k)

    print("part1:", valid1)
    print("part2:", valid2)


passportlist = read_as_strings("../inputs/2020_04.txt")
part1and2(passportlist)
