from puzzle import Puzzle
from heapq import heappush, heappop
from scipy.optimize import newton

class Node:
    def __init__(self, puzzle, parent, g, h):
        self.puzzle = puzzle
        self.parent = parent
        self.g = g
        self.h = h
        self.f = h+g

    def __lt__(self, other):
        return self.f < other.f

def ebf_equation(b, N, d):
    return 1 - b**(d + 1) - (N + 1) * (1 - b)

def ebf_derivative(b, N, d):
    return -((d + 1) * b**d) + (N + 1)

def calculate_ebf(N, d, initial_guess =2):
    return newton(ebf_equation, initial_guess, fprime=ebf_derivative, args=(N, d))

def astar_search(start_state, heuristic):
    frontier = []
    visited = set()

    heuristic_func = start_state.misplaced_titles if heuristic == "misplaced_titles" else start_state.manhattan

    start_node = Node(start_state, None, g=0, h=heuristic_func())
    heappush(frontier, start_node)

    visited.add(str(start_state))
    total_nodes = 1
    while frontier:
        current_node = heappop(frontier)

        if current_node.puzzle.solved():
            depth = current_node.g
            branching_factor = calculate_ebf(total_nodes, depth)
            return depth, total_nodes,branching_factor

        for puzzle in current_node.puzzle.neighbors():
            h = puzzle.misplaced_titles() if heuristic == "misplaced_titles" else puzzle.manhattan()
            neighbor_node = Node(puzzle, current_node, current_node.g + 1, h)

            if str(puzzle.board) not in visited:
                heappush(frontier, neighbor_node)
                visited.add(str(puzzle.board))
                total_nodes += 1