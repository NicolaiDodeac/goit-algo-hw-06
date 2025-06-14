import networkx as nx
from task_1 import create_hadley_graph

G = create_hadley_graph()

shortest_paths = nx.single_source_dijkstra_path(G, source='Hadley', weight='weight')
shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source='Hadley', weight='weight')

print("Shortest paths from Hadley to all other nodes:")
for target in sorted(shortest_paths.keys()):
    if target != "Hadley":
        path = shortest_paths[target]
        length = shortest_path_lengths[target]
        print(f"Hadley → {target}: path = {path}, total time = {length} minutes")
