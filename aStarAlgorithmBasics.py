import heapq

def astar(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while open_set:
        current = heapq.heappop(open_set)[1] # the list is set using priority queue, so that it will always return the minimum value according the priority
        if current == goal:
            break
        
        for neighbor in graph[current]:
            new_cost = cost_so_far[current] + graph[current][neighbor]
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_set, (priority, neighbor))
                came_from[neighbor] = current # setting neighbors' parent as current

    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

# def heuristic(node, goal):
#     dx = abs(node[0] - goal[0])
#     dy = abs(node[1] - goal[1])
#     return dx + dy

def heuristic(node, goal):
    h_values = {
        'A': (0, 0),
        'B': (1, 1),
        'C': (2, 0),
        'D': (2, 1),
        'E': (3, 0),
        'F': (3, 1)
    }
    dx = abs(h_values[node][0] - h_values[goal][0])
    dy = abs(h_values[node][1] - h_values[goal][1])
    return dx + dy


graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 5},
    'C': {'D': 1, 'E': 3},
    'D': {'E': 1, 'F': 2},
    'E': {'F': 1},
    'F': {}
}

start_node = 'A'
goal_node = 'F'

path = astar(graph, start_node,goal_node)
print(path)
