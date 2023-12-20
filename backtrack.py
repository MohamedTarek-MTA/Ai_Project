import networkx as nx
import matplotlib.pyplot as plt

def create_colored_graph(graph):
    G = nx.Graph(graph)
    max_colors_needed = FindMinColorNeeded(G)
    return G, max_colors_needed

def FindMinColorNeeded(Graph):
    colors = dict.fromkeys(Graph.nodes(), 0)
    max_colors_needed = 0

    def color_node(node, current_color):
        nonlocal colors
        neighbors = list(Graph.neighbors(node))
        used_colors = set(colors[neighbor] for neighbor in neighbors)
        
        color = 1
        while color in used_colors or color == current_color:
            color += 1

        colors[node] = color

    def dfs(node):
        nonlocal colors, max_colors_needed
        neighbors = list(Graph.neighbors(node))

        max_neighbor_color = max(colors[neighbor] for neighbor in neighbors) if neighbors else 0

        color_node(node, max_neighbor_color)
        max_colors_needed = max(max_colors_needed, colors[node])

        for neighbor in neighbors:
            if colors[neighbor] == 0:
                dfs(neighbor)

    components = list(nx.connected_components(Graph))
    component_number = 1

    for component in components:
        start_node = next(iter(component))
        dfs(start_node)
        component_number += 1

    nx.set_node_attributes(Graph, colors, 'color')

    return max_colors_needed
