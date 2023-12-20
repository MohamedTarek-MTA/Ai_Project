# graph.py
import networkx as nx
import matplotlib.pyplot as plt 

def create_graph(adjacency_list):
    # Process the adjacency list
    lines = adjacency_list.split('\n')

    # Initialize an empty graph
    G = nx.Graph()

    # Process each line in the adjacency list
    for line in lines:
        parts = line.split(':')
        if len(parts) == 2:
            vertex, neighbors = parts
            vertex = vertex.strip()

            # Add the vertex to the graph if not present
            G.add_node(vertex)

            neighbors = neighbors.strip().split()
            # Add edges for each neighbor, but avoid duplicates
            for neighbor in neighbors:
                if not G.has_edge(vertex, neighbor):
                    G.add_edge(vertex, neighbor)

    return G


def visualize_graph(G, coloring):
    # Convert the keys of coloring to strings
    coloring = {str(vertex): color for vertex, color in coloring.items()}
    node_colors = [coloring[vertex] for vertex in G.nodes]

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.rainbow, font_color='black', font_weight='bold')
    plt.show()
