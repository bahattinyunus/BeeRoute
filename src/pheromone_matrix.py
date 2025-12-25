
"""
BeeRoute: Feromon Matrisi
=========================
Numpy operasyonlarını kullanan dinamik çizge temsili.

Mimar: Bahattin Yunus Çetin (IT Architect)
Lokasyon: Trabzon / Of
"""

import numpy as np

class PheromoneMatrix:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        # Initialize with small random values to allow exploration
        self.matrix = np.ones((num_nodes, num_nodes)) * 0.1
        self.evaporation_rate = 0.05

    def deposit(self, path, amount=1.0):
        """Reinforces the pheromone trail along a specific path."""
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            # undirected graph assumption for simplicity
            self.matrix[u][v] += amount
            self.matrix[v][u] += amount
    
    def decay(self):
        """Applies evaporation to the entire matrix."""
        self.matrix *= (1 - self.evaporation_rate)
        # Prevent total zeroing out
        self.matrix[self.matrix < 0.01] = 0.01

    def get_probability_weights(self, current_node, unvisited_nodes):
        """Returns probability weights for moving to unvisited nodes based on pheromones."""
        weights = []
        for node in unvisited_nodes:
            weights.append(self.matrix[current_node][node])
        
        # Normalize
        total = sum(weights)
        if total == 0:
            return [1.0 / len(weights)] * len(weights)
        
        return [w / total for w in weights]
