from puzzle import Puzzle
import numpy as np


def generate_dataset(n):
    data = []
    visited = set()
    while len(visited) < n:
        cur_puzzle = Puzzle()
        if str(cur_puzzle) not in visited:
            puzzle_array = [num for row in cur_puzzle.board for num in row]
            data.append(puzzle_array)
            visited.add(str(cur_puzzle))
    data = np.array(data)
    np.save("data.npy", data)


if __name__ == "__main__":
    generate_dataset(1400)
