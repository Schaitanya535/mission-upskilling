from collections import deque  # noqa: F401 -- you'll need it (BFS queue); unused until you implement

"""
Problem 2 — Shortest hops from a source (unweighted graph).

Pick one start node `src`. For EVERY node i in the graph, find how far it is
from src — where "distance" = the fewest edges you must cross to get from src
to i (every edge counts as 1 hop, since the graph is unweighted).

Return a list `dist` of length n: `dist[i]` = that fewest-hop count from src
to node i, or -1 if node i can't be reached from src at all.
`dist[src]` is always 0 (src is zero hops from itself).

Index-based adjacency list again (`adj[i]` = list of i's neighbour ids).

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
    result = [-1] * n
    q: deque[int] = deque()
    q.append(src)
    result[src] = 0
    while q:
        front = q.popleft()
        adj_nodes = adj[front]
        for node in adj_nodes:
            if result[node] == -1:
                result[node] = result[front] + 1
                q.append(node)
    return result


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
        print(got)
        # assert got == want == brute_shortest_hops(n, adj, src), (n, adj, src, got, want)
    print("ok")
