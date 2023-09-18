from puzzle import Puzzle
from heapq import heappush, heappop


class Node:
    def __init__(self, puzzle, parent, g, h):
        self.puzzle = puzzle
        self.parent = parent
        self.g = g
        self.h = h
        self.f = h+g

    def __lt__(self, other):
        return self.f < other.f


def astar_search(start_state, heuristic):
    frontier = []
    visited = set()

    heuristic_func = start_state.misplaced_titles if heuristic == "misplaced_titles" else start_state.manhattan

    start_node = Node(start_state, None, g=0, h=heuristic_func())
    heappush(frontier, start_node)

    visited.add(str(start_state.board))
    total_nodes = 1
    while frontier:
        print(total_nodes)
        current_node = heappop(frontier)

        if current_node.puzzle.solved():
            depth = current_node.g
            branching_factor = total_nodes ** (1 / depth)
            return depth, branching_factor

        for puzzle in current_node.puzzle.neighbors():
            h = puzzle.misplaced_titles() if heuristic == "misplaced_titles" else puzzle.manhattan()
            neighbor_node = Node(puzzle, current_node, current_node.g + 1, h)

            if str(puzzle.board) not in visited:
                heappush(frontier, neighbor_node)
                visited.add(str(puzzle.board))
                total_nodes += 1


if __name__ == "__main__":
    initial_puzzle = Puzzle()
    print("Initial puzzle:")
    print(initial_puzzle)

    # depth, ebf = astar_search(initial_puzzle, "misplaced_titles")
    depth2, ebf2 = astar_search(initial_puzzle, "manhattan")
    # print(depth, ebf)
    print(depth2, ebf2)
