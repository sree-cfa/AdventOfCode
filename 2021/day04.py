from util.inputReader import *


class Board:
    def winner(self):
        counter = [0] * 5
        for row in self.rows:
            row_count = 0
            for i, c in enumerate(row[1:-1].split()):
                if c == 'X':
                    counter[i] += 1
                    row_count += 1
            if row_count == 5:
                return True
        return 5 in counter

    def sum(self):
        total = 0
        for row in self.rows:
            for c in row.split():
                total += int(c) if c != 'X' else 0
        return total

    def mark(self, number):
        for i, row in enumerate(self.rows):
            buffered_number = " " + number + " "
            if buffered_number in row:
                self.rows[i] = row.replace(buffered_number, " X ")

    def __init__(self, rows):
        self.rows = rows


def part1(called, list_of_strings):
    boards = build_boards(list_of_strings)

    for number in called:
        for b in boards:
            b.mark(str(number))
            if b.winner():
                return number * b.sum()

    return -1


def part2(called, list_of_strings):
    boards = build_boards(list_of_strings)

    for number in called:
        offset = 0
        for i in range(len(boards)):
            b = boards[i - offset]
            b.mark(str(number))
            if b.winner():
                boards.remove(b)
                offset += 1
                if len(boards) == 0:
                    return number * b.sum()


def build_boards(list_of_strings):
    boards = list()
    board = Board(list())
    for string in list_of_strings:
        if string == "":
            boards.append(board)
            board = Board(list())
        else:
            board.rows.append(' ' + string + ' ')
    return boards


lines = read_as_strings("../inputs/2021_04.txt")
numbers_called = [38, 54, 68, 93, 72, 12, 33, 8, 98, 88, 21, 91, 53, 61, 26, 36, 18, 80, 73, 47, 3, 5, 55, 92, 67, 52,
                  25, 40, 56, 95, 9, 62, 30, 31, 85, 65, 14, 2, 78, 75, 15, 39, 87, 27, 58, 42, 60, 32, 41, 83, 51, 77,
                  10, 66, 70, 4, 37, 6, 89, 23, 16, 49, 48, 63, 94, 97, 86, 64, 74, 82, 7, 0, 11, 71, 44, 43, 50, 69,
                  45, 81, 20, 28, 46, 79, 90, 34, 35, 96, 99, 59, 1, 76, 22, 24, 17, 57, 13, 19, 84, 29]

print("part1:", part1(numbers_called, lines))
print("part2:", part2(numbers_called, lines))

# 6732 too high
