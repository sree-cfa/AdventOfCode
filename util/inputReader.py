def read_as_strings(filename):
    f = open(filename, "r")
    res = f.read().split("\n")
    return res

def read_as_ints(filename):
    f = open(filename, "r")
    res = map(int, f.read().split("\n"))
    return list(res)
