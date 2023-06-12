import sys

def dijkstra(graph,start):
    num_nodes = len(graph) 
    distance = [sys.maxsize] * num_nodes # made all the distances infinity
    distance[start] = 0 # except starting node
    visited = [False] * num_nodes 

    while True:
        min_distance = sys.maxsize
        min_node = -1

        for node in range(num_nodes):
            if not visited[node] and distance[node] < min_distance:
                min_distance = distance[node]
                min_node = node
            
        if min_node == -1:
            break
        visited[min_node] = True

        for neighbor in range(num_nodes):
            if (
                not visited[neighbor]
                and graph[min_node][neighbor] != 0
                and distance[min_node] + graph[min_node][neighbor] < distance[neighbor]
            ):
                distance[neighbor] = distance[min_node] + graph[min_node][neighbor]
        
    return distance
    
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]

start_node = 0
distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node)
for i,dist in enumerate(distances):
    print(f"Node {i}: {dist}")

