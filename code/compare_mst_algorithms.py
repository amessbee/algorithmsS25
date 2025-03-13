import time
import matplotlib.pyplot as plt
import networkx as nx
import random
import numpy as np
from prims import prim
from kruskals import kruskal

def generate_random_graph(n, edge_density=0.3):
    """
    Generate a random graph with n vertices and approximately edge_density * n*(n-1)/2 edges.
    Returns a list of edges in the format (u, v, weight).
    """
    edge_density = 20/n
    max_edges = n * (n - 1) // 2
    num_edges = int(max_edges * edge_density)
    
    # Ensure the graph is connected by including a spanning tree
    edges = []
    visited = [0]
    unvisited = list(range(1, n))
    
    # Create a spanning tree to ensure connectivity
    while unvisited:
        u = random.choice(visited)
        v = random.choice(unvisited)
        weight = random.randint(1, 100)
        edges.append((u, v, weight))
        visited.append(v)
        unvisited.remove(v)
    
    # Add additional random edges
    while len(edges) < num_edges:
        u = random.randint(0, n-1)
        v = random.randint(0, n-1)
        if u != v:
            weight = random.randint(1, 100)
            edge = (u, v, weight)
            reverse_edge = (v, u, weight)
            if edge not in edges and reverse_edge not in edges:
                edges.append(edge)
    
    return edges

def measure_performance(sizes, trials=3):
    """
    Measure the performance of Prim's and Kruskal's algorithms on graphs of different sizes.
    Returns the average runtime for each algorithm and graph size.
    """
    prim_times = []
    kruskal_times = []
    
    for size in sizes:
        prim_trial_times = []
        kruskal_trial_times = []
        
        for _ in range(trials):
            # Generate a random graph
            edges = generate_random_graph(size)
            
            # Measure Prim's algorithm
            start_time = time.time()
            prim(size, edges)
            prim_time = time.time() - start_time
            prim_trial_times.append(prim_time)
            
            # Measure Kruskal's algorithm
            start_time = time.time()
            kruskal(size, edges)
            kruskal_time = time.time() - start_time
            kruskal_trial_times.append(kruskal_time)
        
        # Calculate average times
        prim_times.append(np.mean(prim_trial_times))
        kruskal_times.append(np.mean(kruskal_trial_times))
        
        print(f"Size {size}: Prim's = {prim_times[-1]:.6f}s, Kruskal's = {kruskal_times[-1]:.6f}s")
    
    return prim_times, kruskal_times

def plot_results(sizes, prim_times, kruskal_times):
    """
    Plot the performance results of both algorithms.
    """
    plt.figure(figsize=(12, 8))
    
    # Runtime comparison
    plt.subplot(2, 1, 1)
    plt.plot(sizes, prim_times, 'o-', label="Prim's Algorithm")
    plt.plot(sizes, kruskal_times, 's-', label="Kruskal's Algorithm")
    plt.xlabel('Number of Vertices')
    plt.ylabel('Runtime (seconds)')
    plt.title('MST Algorithm Runtime Comparison')
    plt.legend()
    plt.grid(True)
    
    # Runtime ratio
    plt.subplot(2, 1, 2)
    ratio = [k/p if p > 0 else 1 for p, k in zip(prim_times, kruskal_times)]
    plt.plot(sizes, ratio, 'x-')
    plt.axhline(y=1, color='r', linestyle='--')
    plt.xlabel('Number of Vertices')
    plt.ylabel('Kruskal/Prim Runtime Ratio')
    plt.title('Runtime Ratio (Kruskal/Prim)')
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('mst_comparison.png')
    plt.show()

def theoretical_complexity(sizes):
    """
    Plot the theoretical complexity of both algorithms.
    Prim's: O(E log V) with binary heap
    Kruskal's: O(E log E) or O(E log V)
    """
    plt.figure(figsize=(10, 6))
    
    # For connected graphs, E is approximately V^2
    e_prim = [n * np.log2(n) for n in sizes]  # E log V where E ~ V^2
    e_kruskal = [n**2 * np.log2(n) for n in sizes]  # E log E where E ~ V^2
    
    # Normalize for comparison
    max_val = max(max(e_prim), max(e_kruskal))
    e_prim = [e/max_val for e in e_prim]
    e_kruskal = [e/max_val for e in e_kruskal]
    
    plt.plot(sizes, e_prim, 'o-', label="Prim's: O(E log V)")
    plt.plot(sizes, e_kruskal, 's-', label="Kruskal's: O(E log E)")
    plt.xlabel('Number of Vertices')
    plt.ylabel('Normalized Complexity')
    plt.title('Theoretical Complexity Comparison')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('theoretical_complexity.png')
    plt.show()

if __name__ == "__main__":
    # Define the sizes of graphs to test
    sizes = [100, 200, 400, 1000, 2000]
    
    # Measure performance
    prim_times, kruskal_times = measure_performance(sizes)
    
    # Plot results
    plot_results(sizes, prim_times, kruskal_times)
    
    # Plot theoretical complexity
    theoretical_complexity(sizes)
    
    # Print conclusion
    print("\nConclusion:")
    print("------------")
    if np.mean([k/p for k, p in zip(kruskal_times, prim_times)]) > 1:
        print("On average, Prim's algorithm was faster for the tested graph sizes.")
    else:
        print("On average, Kruskal's algorithm was faster for the tested graph sizes.")
    
    print("\nTheoretical vs. Practical:")
    print("For sparse graphs, Kruskal's algorithm can be more efficient.")
    print("For dense graphs, Prim's algorithm is typically more efficient.")
    print("The actual performance depends on implementation details and graph structure.")
