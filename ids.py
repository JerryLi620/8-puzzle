from puzzle import Puzzle
from scipy.optimize import newton

def ebf_equation(b, N, d):
    return 1 - b**(d + 1) - (N + 1) * (1 - b)

def ebf_derivative(b, N, d):
    return -((d + 1) * b**d) + (N + 1)

def calculate_ebf(N, d, initial_guess =2):
    return newton(ebf_equation, initial_guess, fprime=ebf_derivative, args=(N, d))

def dls(puzzle, limit, nodes_generated):
    visited = set()
    stack = [(puzzle, 0)]

    while stack:
        current_puzzle, current_depth = stack.pop()

        if current_puzzle.solved():
            ebf = calculate_ebf(nodes_generated, current_depth) if current_depth != 0 else 0
            return current_depth, nodes_generated, ebf

        visited.add(str(current_puzzle.board))

        if current_depth < limit:
            for neighbor_puzzle in current_puzzle.neighbors():
                if str(neighbor_puzzle.board) not in visited:
                    nodes_generated += 1
                    stack.append((neighbor_puzzle, current_depth + 1))

    return None, nodes_generated, None

def ids(start_state, depth_limit):
    nodes_generated = 0  
    for limit in range(depth_limit + 1):
        depth, nodes_generated, ebf = dls(start_state, limit, nodes_generated)
        if depth is not None:
            return depth, nodes_generated, ebf

if __name__ == "__main__":
    puzzle = Puzzle()
    print(ids(puzzle, 100))