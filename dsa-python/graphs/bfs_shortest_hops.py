from collections import deque

"""
Problem 2 — Shortest hops from a source (unweighted graph).

Index-based adjacency list again. Return `dist[i]` = fewest edges from `src`
to node i, or -1 if unreachable.

    shortest_hops(n=6, adj=[[1,2],[0,3],[0,3],[1,2,4],[3,5],[4]], src=0)
        -> [0, 1, 1, 2, 3, 4]
    shortest_hops(n=3, adj=[[1],[0],[]], src=0) -> [0, 1, -1]

Constraints: 0 <= src < n. Undirected.

First solution: BFS. A queue + visited; nodes come off the queue in
non-decreasing distance order, so the FIRST time you reach a node is via a
shortest path. Why does that fail for DFS? (DFS can reach a node by a long
path first.) State why BFS is correct for UNWEIGHTED and Dijkstra is needed
once edges have weights — that contrast is the bridge to Problem 3.

Insight to discover:
- Set dist when you ENQUEUE (not when you dequeue) to avoid re-adding.
- This level-order walk is exactly how HNSW explores a single layer before
  the priority queue (weights) takes over in greedy search.

Oracle (write it, different method): iterative-deepening DFS. For depth cap
d = 0,1,2,...: depth-limited DFS from src; the first cap that reaches node i
is its distance. Slow but independent of BFS.

Target: O(n + E) time.
"""


def shortest_hops(n: int, adj: list[list[int]], src: int) -> list[int]:
    raise NotImplementedError


def brute_shortest_hops(n: int, adj: list[list[int]], src: int) -> list[int]:
    """Oracle. Iterative-deepening depth-limited DFS — independent of BFS."""
    raise NotImplementedError


if __name__ == "__main__":
    cases = [
        (6, [[1, 2], [0, 3], [0, 3], [1, 2, 4], [3, 5], [4]], 0, [0, 1, 1, 2, 3, 4]),
        (3, [[1], [0], []], 0, [0, 1, -1]),
        (1, [[]], 0, [0]),
    ]
    for n, adj, src, want in cases:
        got = shortest_hops(n, adj, src)
        assert got == want == brute_shortest_hops(n, adj, src), (n, adj, src, got, want)
    print("ok")
