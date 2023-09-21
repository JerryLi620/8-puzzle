from puzzle import Puzzle

def dls(puzzle, limit, nodes_generated):
    visited = set()
    stack = [(puzzle, 0)]

    while stack:
        current_puzzle, current_depth = stack.pop()

        if current_puzzle.solved():
            ebf = nodes_generated ** (1 / current_depth) if current_depth != 0 else 0
            return current_depth, nodes_generated, ebf

        visited.add(str(current_puzzle.board))

        if current_depth < limit:
            for neighbor_puzzle in current_puzzle.neighbors():
                if str(neighbor_puzzle.board) not in visited:
                    nodes_generated += 1
                    stack.append((neighbor_puzzle, current_depth + 1))

    return None, nodes_generated, None

def ids(start_state, depth_limit):
    nodes_generated = 0  # Initialize nodes_generated
    for limit in range(depth_limit + 1):
        depth, nodes_generated, ebf = dls(start_state, limit, nodes_generated)  # Update nodes_generated
        if depth is not None:
            return depth, nodes_generated, ebf
