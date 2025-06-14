import networkx as nx
import matplotlib.pyplot as plt

def create_hadley_graph():
    G = nx.Graph()

    # Add nodes
    places = [
        "Hadley", "Ketley", "Leegomery", "Trench", "Donnington",
        "Hortonwood", "Wellington", "Telford Central", "Priorslee", "Oakengates"
    ]
    G.add_nodes_from(places)

    # Add weighted, typed connections
    connections = [
        ("Hadley", "Ketley", 7, "bus"),
        ("Hadley", "Leegomery", 5, "bus"),
        ("Hadley", "Trench", 6, "bus"),
        ("Hadley", "Donnington", 10, "bus"),
        ("Hadley", "Hortonwood", 5, "bus"),
        ("Hadley", "Wellington", 10, "bus"),
        ("Hadley", "Telford Central", 15, "bus"),
        ("Hadley", "Oakengates", 10, "bus"),
        ("Donnington", "Priorslee", 8, "bus"),
        ("Telford Central", "Priorslee", 6, "bus"),
        ("Wellington", "Telford Central", 12, "train"),
        ("Oakengates", "Telford Central", 5, "train"),
        ("Wellington", "Oakengates", 7, "train")
    ]

    for u, v, time, route_type in connections:
        G.add_edge(u, v, weight=time, type=route_type)

    return G

if __name__ == "__main__":
    G = create_hadley_graph()

    pos = nx.spring_layout(G, seed=42)
    edge_colors = ["blue" if G[u][v]["type"] == "train" else "green" for u, v in G.edges()]
    edge_labels = nx.get_edge_attributes(G, "weight")

    plt.figure(figsize=(12, 8))
    nx.draw(
        G, pos, with_labels=True, node_color="lightyellow", node_size=2200,
        edge_color=edge_colors, width=2, font_size=10, font_weight="bold"
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("📍 Hadley-Centered Telford Local Transport Network", fontsize=14)
    plt.show()

    print(f"Total places (nodes): {G.number_of_nodes()}")
    print(f"Total connections (edges): {G.number_of_edges()}")

    print("\nDegree (прямих з'єднань) per place:")
    for node, degree in G.degree():
        print(f"{node}: {degree}")

    most_connected = max(G.degree, key=lambda x: x[1])
    print(f"\nНайбільш зєднана точка: {most_connected[0]} ({most_connected[1]} зв'язків)")
