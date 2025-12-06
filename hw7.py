# 111210554

import numpy as np

labyrinth = np.array([
    [2,1,1,1,1,1,1,0,1,0],
    [1,0,1,0,0,0,1,0,1,1],
    [1,1,0,0,1,1,1,0,1,0],
    [1,0,0,0,0,0,0,0,1,0],
    [1,1,1,1,1,1,1,1,1,0],
    [0,1,0,0,1,0,0,0,0,0],
    [1,1,0,0,1,0,0,0,1,1],
    [1,0,1,1,1,0,0,1,1,0],
    [1,0,1,0,0,0,0,0,1,0],
    [1,0,1,1,1,1,1,1,1,3]
])

def get_neighbors(position, maze):
    row, col = position
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    neighbors = []
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < maze.shape[0] and 0 <= nc < maze.shape[1]:
            if maze[nr, nc] != 0:
                neighbors.append((nr, nc))
    return neighbors

def depth_first_search(maze):
    start_pos = tuple(np.argwhere(maze == 2)[0])
    visited_nodes = set()

    def visit(node):
        if node in visited_nodes:
            return False
        visited_nodes.add(node)

        r, c = node
        print("Visiting:", node)

        if maze[r, c] == 3:
            print("GOAL FOUND at:", node)
            return True

        for neighbor in get_neighbors(node, maze):
            if visit(neighbor):
                return True
        
        return False
    
    visit(start_pos)

depth_first_search(labyrinth)
