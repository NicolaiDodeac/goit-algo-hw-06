from collections import deque
from task_1 import create_hadley_graph

G = create_hadley_graph()

def dfs_path(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    visited.add(start)
    path = path + [start]

    if start == goal:
        return path

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result = dfs_path(graph, neighbor, goal, path, visited)
            if result:
                return result
    return None

def bfs_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                new_path = path + [neighbor]
                queue.append(new_path)
    return None


start = "Hadley"
destination = "Telford Central"

if __name__ == "__main__":
    dfs_result = dfs_path(G, start, destination)
    bfs_result = bfs_path(G, start, destination)

    print(f"DFS path from {start} to {destination}: {dfs_result}")
    print(f"BFS path from {start} to {destination}: {bfs_result}")
