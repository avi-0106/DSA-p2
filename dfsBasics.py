'''
There are two type of approach for DFS
1. Recursive DFS Implementation in Python
2. Iterative DFS Implementation in Python
'''

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Recursive DFS Implementation in Python : ")
def dfs_recursive(graph, node, visited):
    visited.add(node)
    print(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph,neighbor,visited)

visited = set()
dfs_recursive(graph,'A',visited)


print("Iterative DFS Implementation in Python : ")
def dfs_iterative(graph,start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            stack.extend(graph[node])

dfs_iterative(graph, 'A')

