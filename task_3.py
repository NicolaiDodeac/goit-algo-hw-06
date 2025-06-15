import heapq
from task_1 import create_hadley_graph

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0

    previous = {node: None for node in graph.nodes}
    visited = set()

    queue = [(0, start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            new_dist = current_dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = current_node
                heapq.heappush(queue, (new_dist, neighbor))

    return distances, previous

def reconstruct_path(previous, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = previous[current]
        if current is None:
            return None
    path.append(start)
    path.reverse()
    return path

if __name__ == "__main__":
    G = create_hadley_graph()
    start = "Hadley"

    distances, previous = dijkstra(G, start)

    print(f"Найкоротші шляхи від {start} до всіх інших вершин:\n")
    for node in G.nodes:
        if node != start:
            path = reconstruct_path(previous, start, node)
            if path:
                print(f"{start} → {node}: шлях = {path}, час = {distances[node]} хв")
            else:
                print(f"{start} → {node}: шлях не знайдено")
