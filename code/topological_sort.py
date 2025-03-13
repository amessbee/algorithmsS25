from collections import deque
import networkx as nx
import random


# - For each of the vertices, find their in-degree.
# Add all vertices with in-degree zero to a Queue.
# As long as there are vertices in the Queue, do the following:
# - Remove a vertex from the Queue.
# - Add this vertex to the topological order.
# - For all vertices adjacent to the removed vertex, reduce their in-degree by 1.
# If the in-degree of a vertex becomes zero, add it to the Queue.
# If the topological order has all vertices, return it.
# Otherwise, return an empty list.

def topological_sort(G):
    # H = G.reverse(copy=True)
    # in_degree = {n: H.degree(n) for n in H.nodes()}

    # in_degree = {n: 0 for n in G.nodes()}
    # for node in G.nodes():
    #     for neighbor in G.successors(node):
    #         in_degree[neighbor] += 1
    in_degree = {}
    for node in G:
        in_degree[node] = 0
    for node in G:
        for nxt in G.successors(node):
            in_degree[nxt] += 1
    queue = deque([n for n in G.nodes() if in_degree[n] == 0])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in G.successors(node):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return result if len(result) == len(G.nodes()) else []





import matplotlib.pyplot as plt

G_random = nx.DiGraph()
G_random.add_nodes_from(range(8))

while G_random.number_of_edges() < 12:
    u = random.randint(0, 7)
    v = random.randint(0, 7)
    if u != v and not G_random.has_edge(u, v):
        G_random.add_edge(u, v)
        if not nx.is_directed_acyclic_graph(G_random):
            G_random.remove_edge(u, v)

H = G_random.reverse(copy=True)
# plt.figure(figsize=(12, 6))
pos = nx.circular_layout(G_random)
nx.draw(G_random, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_color='black')
# plt.subplot(121)
nx.draw_circular(G_random)
plt.title("G_random")

print( topological_sort(G_random) )
# plt.subplot(122)
# nx.draw_networkx(H)
# plt.title("H")

plt.show()