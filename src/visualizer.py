
"""
BeeRoute: Visualizer
====================
Generates visual representations of the colony's optimization process.
"""

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class HiveVisualizer:
    def __init__(self, node_count):
        self.node_count = node_count
        self.G = nx.complete_graph(node_count)
        # Generate random positions for nodes to simulate a map
        self.pos = nx.spring_layout(self.G, seed=42)

    def plot_route(self, route, distance, filename="route_result.png"):
        """
        Plots the network and highlights the best route found.
        """
        plt.figure(figsize=(10, 8))
        
        # Draw all nodes and edges (faintly)
        nx.draw_networkx_nodes(self.G, self.pos, node_color='lightgray', node_size=500)
        nx.draw_networkx_edges(self.G, self.pos, alpha=0.1)
        nx.draw_networkx_labels(self.G, self.pos, font_size=10, font_family='sans-serif')

        # Highlight the optimal route
        if route:
            path_edges = list(zip(route, route[1:]))
            nx.draw_networkx_edges(
                self.G, 
                self.pos, 
                edgelist=path_edges, 
                edge_color='#F7D917', # Bee Yellow
                width=3.0,
                alpha=0.9
            )
            nx.draw_networkx_nodes(
                self.G, 
                self.pos, 
                nodelist=route, 
                node_color='#BF2E1A', # Trabzon Red
                node_size=600
            )

        plt.title(f"BeeRoute Optimization Result\nDistance: {distance:.2f} (Trabzon Metrics)", fontsize=14, fontweight='bold')
        plt.axis('off')
        
        plt.savefig(filename, bbox_inches='tight', facecolor='white')
        print(f"[VISUALIZER] Graph saved to {filename}")
        plt.close()
