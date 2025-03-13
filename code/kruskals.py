import networkx as nx
import random

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(n, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    uf = UnionFind(n)
    mst = []
    mst_cost = 0
    
    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
            mst_cost += weight
    
    return mst, mst_cost

# # Example usage:
# import matplotlib.pyplot as plt

# # Generate a random graph with 8 vertices and 15 edges
# n = 8
# edges = []
# while len(edges) < 15:
#     u = random.randint(0, n-1)
#     v = random.randint(0, n-1)
#     if u != v:
#         weight = random.randint(1, 20)
#         edge = (u, v, weight)
#         if edge not in edges and (v, u, weight) not in edges:
#             edges.append(edge)

# # Create a NetworkX graph
# G = nx.Graph()
# G.add_weighted_edges_from(edges)

# # Compute MST using Kruskal's algorithm
# mst, mst_cost = kruskal(n, edges)

# # Create a NetworkX graph for the MST
# MST_G = nx.Graph()
# MST_G.add_weighted_edges_from(mst)

# # Plot the original graph
# plt.figure(figsize=(12, 6))

# plt.subplot(121)
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
# labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# plt.title("Original Graph")

# # Plot the MST
# plt.subplot(122)
# pos = nx.spring_layout(MST_G)
# nx.draw(MST_G, pos, with_labels=True, node_color='lightgreen', edge_color='gray')
# labels = nx.get_edge_attributes(MST_G, 'weight')
# nx.draw_networkx_edge_labels(MST_G, pos, edge_labels=labels)
# plt.title("Minimum Spanning Tree (MST)")

# plt.show()

# print("Edges in MST:", mst)
# print("Total cost of MST:", mst_cost)