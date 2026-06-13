import heapq  # noqa: F401 -- you'll need it (min-heap frontier); unused until you implement

"""
Problem 3 — Dijkstra: shortest weighted path from a source.

Index-based, now WEIGHTED. adj[i] = list of (neighbour_id, weight), weights
>= 0. Return dist[i] = min total weight src->i, or -1 if unreachable.

    dijkstra(n=5,
        adj=[[(1,2),(2,5)], [(2,1),(3,2)], [(3,3)], [(4,1)], []],
        src=0) -> [0, 2, 3, 4, 5]
    dijkstra(n=2, adj=[[],[]], src=0) -> [0, -1]

Constraints: weights >= 0 (Dijkstra breaks on negatives — that's Bellman-Ford's
job, hence the oracle below). Directed edges as written.

First solution: a min-heap of (dist_so_far, node). Pop the closest unfinalised
node, relax its edges, push improved neighbours. THIS min-heap-of-candidates,
always expanding the closest frontier node, IS the skeleton of HNSW greedy
search — swap "edge weight" for "distance to the query vector" and you have
Problem 4. Learn it cold here.

Insight to discover:
- A node can be pushed multiple times with different dists (lazy deletion).
  Skip a popped (d, u) if d > dist[u] — it's a stale duplicate. Why is this
  cheaper than a decrease-key?
- Root of the heap = globally closest frontier node = next to finalise.

Oracle (write it, different method): Bellman-Ford. Relax ALL edges (n-1) times.
O(n*E), no heap — totally independent of your Dijkstra.

Target: O((n + E) log n) time.
"""


def dijkstra(n: int, adj: list[list[tuple[int, int]]], src: int) -> list[int]:
    raise NotImplementedError


def brute_dijkstra(n: int, adj: list[list[tuple[int, int]]], src: int) -> list[int]:
    """Oracle. Bellman-Ford: relax every edge n-1 times. No heap."""
    raise NotImplementedError


if __name__ == "__main__":
    cases = [
        (5, [[(1, 2), (2, 5)], [(2, 1), (3, 2)], [(3, 3)], [(4, 1)], []], 0,
         [0, 2, 3, 4, 5]),
        (2, [[], []], 0, [0, -1]),
        (1, [[]], 0, [0]),
    ]
    for n, adj, src, want in cases:
        got = dijkstra(n, adj, src)
        assert got == want == brute_dijkstra(n, adj, src), (n, adj, src, got, want)
    print("ok")
