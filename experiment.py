
import csv
from puzzle import Puzzle 
import numpy as np

from astar import astar_search  
from ids import ids 
from generate_data import generate_dataset

def run_experiment(n, depth_limit):
    # Generate dataset
    generate_dataset(n)
    data = np.load("data.npy")

    # Create a CSV file to store the results
    with open("experiment_results.csv", "w", newline='') as csvfile:
        fieldnames = ["Algorithm", "Heuristic/Depth Limit", "Depth", "Nodes Generated", "Effective Branching Factor"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for puzzle_array in data:
            puzzle = Puzzle(numbers=puzzle_array.tolist())

            # Run A* with Manhattan distance
            depth, nodes, ebf = astar_search(puzzle, "manhattan")
            writer.writerow({"Algorithm": "A*", "Heuristic/Depth Limit": "Manhattan", "Depth": depth, "Nodes Generated": nodes, "Effective Branching Factor": ebf})

            # Run A* with misplaced titles
            depth, nodes, ebf = astar_search(puzzle, "misplaced_titles")
            writer.writerow({"Algorithm": "A*", "Heuristic/Depth Limit": "Misplaced Titles", "Depth": depth, "Nodes Generated": nodes, "Effective Branching Factor": ebf})

            # Run IDS
            depth, nodes, ebf = ids(puzzle, depth_limit)
            writer.writerow({"Algorithm": "IDS", "Heuristic/Depth Limit": "N/A", "Depth": depth, "Nodes Generated": nodes, "Effective Branching Factor": ebf})

if __name__ == "__main__":
    run_experiment(500, 100)