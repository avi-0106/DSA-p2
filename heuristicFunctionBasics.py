
def heuristic(state,goal):
    #Calculates the Manhattan distance
    total_distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:
                goal_pos = find_tile(goal, tile)
                distance = abs(i - goal_pos[0]) + abs(j - goal_pos[1])
                total_distance += distance
    return total_distance
    
def find_tile(state, tile):
    for i in range(3):
        for j in range(3):
            if state[i][j] == tile:
                return (i, j)


'''
Notes::


Explanation of Heuristic Function:
- A heuristic function is an evaluation function used in search algorithms to estimate the cost or distance from a current state/node to the goal state/node.
- It provides a heuristic or approximate evaluation that guides the search algorithm in making informed decisions about which states to explore next.
- The heuristic function aims to estimate the remaining cost or distance without actually computing the entire path or solution.

Python Implementation of Heuristic Function:
- The implementation of a heuristic function will depend on the problem domain and the specific problem you're working on. Let's consider a simple example of a heuristic function for the "8-puzzle" problem.
- In the 8-puzzle problem, you have a 3x3 grid with 8 numbered tiles and an empty space. The goal is to rearrange the tiles from a given initial state to a desired goal state.


'''