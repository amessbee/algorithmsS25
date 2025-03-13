import networkx as nx
import random
import heapq

# Prim's algorithm for finding Minimum Spanning Tree (MST)
# pick a arbitrary vertex as the starting point
# put all the edges incident on that vertex to a priority queue
# while the priority queue is not empty:
#     pop the edge with the smallest weight
#    if the edge connects two vertices that are not in the MST:
#         add the edge to the MST
#         add the vertex to the MST
#         put all the edges incident on that vertex to the priority queue
# return the MST and the total cost of the MST
def prim(n, edges):
    # Create a graph from the edges
    graph = [[] for _ in range(n)]
    for u, v, weight in edges:
        graph[u].append((weight, v))
        graph[v].append((weight, u))

    # Initialize the MST and the priority queue
    mst = []
    total_cost = 0
    visited = [False] * n
    pq = []

    # Start from vertex 0 (arbitrary choice)
    visited[0] = True
    for edge in graph[0]:
        heapq.heappush(pq, (edge[0], 0, edge[1]))

    while pq:
        weight, u, v = heapq.heappop(pq)
        if not visited[v]:
            visited[v] = True
            mst.append((u, v, weight))
            total_cost += weight
            for edge in graph[v]:
                if not visited[edge[1]]:
                    heapq.heappush(pq, (edge[0], v, edge[1]))

    return mst, total_cost

# Example usage:
import matplotlib.pyplot as plt

# Generate a random graph with 8 vertices and 15 edges
n = 8
edges = []
while len(edges) < 15:
    u = random.randint(0, n-1)
    v = random.randint(0, n-1)
    if u != v:
        weight = random.randint(1, 20)
        edge = (u, v, weight)
        if edge not in edges and (v, u, weight) not in edges:
            edges.append(edge)


# # Create a NetworkX graph
# G = nx.Graph()
# G.add_weighted_edges_from(edges)

# # Compute MST using Prim's algorithm
# mst, mst_cost = prim(n, edges)

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
