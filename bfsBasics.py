from collections import deque

def bfs(graph, start):
    '''
    In this implementation, the graph parameter represents the graph in the 
    form of an adjacency list. It should be a dictionary where the keys are 
    the vertices, and the values are lists of adjacent vertices.
    '''
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)


# Application :

# Sample graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting vertex for BFS
start_vertex = 'A'

# Perform BFS traversal
bfs(graph, start_vertex)
