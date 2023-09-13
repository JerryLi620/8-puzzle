from random import shuffle


class Puzzle:
    def __init__(self, numbers=None):
        if numbers == None:
            numbers = list(range(0, 9))
            shuffle(numbers)
            while not self.is_solvable(numbers):
                shuffle(numbers)

        self.board = [numbers[i:i+3] for i in range(0, 9, 3)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.board])

    def solved(self):
        goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        return self.board == goal

    def is_solvable(self, numbers):
        inversion = 0

        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] > numbers[j]:
                    inversion += 1
        return inversion % 2 == 0


puzzle = Puzzle()
print(puzzle)
