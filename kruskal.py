from typing import Optional

import pandas as pd


class Graph:
    """Class that represents a graph that allows to compute Kruskal's algorithm over it."""
    
    def __init__(self, vertex: int) -> None:
        """Builds a graph with this number of vertices."""
        self.V = vertex
        self.graph = []
 
    def add_edge(self, u: int, v: int, w: float) -> None:
        """Adds an edge from u to v with the specified weight (w)."""
        self.graph.append([u, v, w])
 
    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])
 
    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self, max_links: Optional[int]=None) -> pd.DataFrame:
        """Returns a DataFrame containing Kruskal's edges (from vertex, to vertex) with its weight."""
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1 and (max_links is None or e < max_links):
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        return pd.DataFrame(data=result, columns=['id_a', 'id_b', 'weight'])
