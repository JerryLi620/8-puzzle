from puzzle import Puzzle

def dls(puzzle, limit):
    visited = set()
    stack = [(puzzle, 0)]
    nodes_generated  = 0

    while stack:
        current_puzzle, current_depth = stack.pop()

        if current_puzzle.solved():
            ebf = nodes_generated**(1/current_depth)
            return current_depth, nodes_generated,ebf
        
        visited.add(str(current_puzzle.board))

        if current_depth < limit:
            for puzzle in current_puzzle.neighbors():
                if str(puzzle.board) not in visited:
                    nodes_generated +=1
                    stack.append((puzzle, current_depth+1))

def ids(start_state, depth_limit):
    for limit in range(depth_limit +1):
        result = dls(start_state, limit)
        if result:
            return result
        