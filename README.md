# CS310/5102: Algorithms — Spring 2025

Lecture notes, problem sets, and code examples for the **Algorithms** course taught at [LUMS SSE](https://sse.lums.edu.pk) in Spring 2025.

Topics span algorithm design and analysis from first principles through advanced graph algorithms, dynamic programming, and complexity theory.

## Contents

| Folder | Topic |
|--------|-------|
| `lecture-02/` | Introduction & Asymptotic Analysis |
| `lecture-03/` | Divide and Conquer |
| `lecture-04/` | Recurrences & Master Theorem |
| `lecture-05-06/` | Sorting: MergeSort, QuickSort, HeapSort |
| `lecture-07/` | Multiplication Algorithms & The Hiring Problem |
| `lecture-08/` | Greedy Algorithms |
| `lecture-10/` | Analysis of Algorithms — Amortized Complexity |
| `lecture-11/` | Graph Theory: BFS & DFS (with animations) |
| `lecture-12/` | Articulation Points & Topological Sort |
| `lecture-13/` | DFS Traversal deep-dive |
| `lecture-15/` | Minimum Spanning Trees (Kruskal, Prim) |
| `lecture-17/` | Shortest Paths: Dijkstra & Bellman-Ford |
| `lecture-18/` | Amortized Analysis: Binary Counter |
| `lecture-19/` | Network Flow |
| `lecture-20/` | Complexity Theory: P, NP, NP-completeness |
| `lecture-21/` | Dynamic Programming — Introduction |
| `lecture-21-DP-problems/` | Dynamic Programming — Problem Set |
| `lecture-22/` | DP continued: LCS, Matrix-chain Multiplication |
| `lecture-24/` | Randomized Algorithms |
| `lecture-25/` | String Matching |
| `lecture-26/` | Computational Geometry |
| `lecture-27/` | Advanced Topics |
| `code/` | Python implementations (MST, topological sort) |
| `question-bank/` | Exam question bank (PDF) |

Each lecture folder contains a compiled PDF (`main.pdf` or `intro.pdf`) and the LaTeX source (`main.tex` or `intro.tex`), plus supporting figures.

## Code Examples

The `code/` directory has runnable Python implementations:

| File | What it does |
|------|--------------|
| `kruskals.py` | Kruskal's MST using union-find |
| `prims.py` | Prim's MST using a priority queue |
| `compare_mst_algorithms.py` | Empirical runtime comparison (generates `mst_comparison.png`) |
| `topological_sort.py` | Topological sort via DFS |

```bash
python3 code/kruskals.py
python3 code/compare_mst_algorithms.py
```

## Viewing Lecture Notes

All lecture notes are compiled to PDF and committed alongside their LaTeX source. Open `main.pdf` inside any lecture folder.

To recompile from source (requires [TeX Live](https://www.tug.org/texlive/) or [MacTeX](https://www.tug.org/mactex/)):

```bash
cd lecture-03/Algorithms_lecture3
pdflatex main.tex
```

## Course Info

- **Course:** CS310 / CS5102 — Algorithms
- **Institution:** Lahore University of Management Sciences (LUMS), School of Science and Engineering
- **Term:** Spring 2025
- **Instructor:** [Mudassir Shabbir](https://amessbee.github.io)
