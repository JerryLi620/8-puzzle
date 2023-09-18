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
                if numbers[i] > numbers[j] and numbers[i] != 0 and numbers[j] != 0:
                    inversion += 1
        return inversion % 2 == 0

    def neighbors(self):
        neighbors = []

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:

                    directions = [[i-1, j], [i+1, j], [i, j+1], [i, j-1]]

                    for new_i, new_j in directions:
                        if 0 <= new_i < len(self.board) and 0 <= new_j < len(self.board[0]):
                            new_board = [row[:] for row in self.board]
                            new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]
                            neighbor_puzzle = Puzzle(
                                numbers=[num for row in new_board for num in row])
                            neighbors.append(neighbor_puzzle)
                    return neighbors

    def manhattan(self):
        distance = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                title = self.board[i][j]
                if title != 0:
                    goal_i, goal_j = divmod(title, 3)
                    distance += abs(goal_i-i)+abs(goal_j-j)
        return distance

    def misplaced_titles(self):
        goal = 0
        misplaced = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != goal and self.board[i][j] != 0:
                    misplaced += 1
                goal += 1
        return misplaced
