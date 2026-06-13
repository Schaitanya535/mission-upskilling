"""
Problem 1 — Count connected components in an undirected graph.

Graph is INDEX-BASED: n nodes labelled 0..n-1, edges as an adjacency list
`adj[i]` = list of neighbour ids. (Same shape HNSW uses — neighbours are int
ids, never object refs — so this ports 1:1 to Rust later.)

    count_components(n=5, adj=[[1],[0],[3],[2],[]]) -> 3
        # {0,1}  {2,3}  {4}
    count_components(n=3, adj=[[1,2],[0,2],[0,1]]) -> 1

Constraints: 0 <= n. adj has length n. Undirected (edges appear both ways).

Brute force / first solution: flood fill. Walk every node; if unvisited,
start a DFS/BFS that marks its whole component, then +1. State the Big-O
(hint: each node + edge touched once).

Insight to discover:
- A `visited` array (bool, indexed by node id) is your whole state. No object
  graph — just ids into a list. This is the representation M3 demands.
- DFS (recursion or explicit stack) vs BFS (queue) — same answer here, pick one.

Oracle (write it, different method): union-find / DSU. `find`+`union` every
edge, then count distinct roots. Two unrelated methods agreeing = real
confidence (the median_stream lesson).

Target: O(n + E) time.
"""


def count_components(n: int, adj: list[list[int]]) -> int:
    raise NotImplementedError


def brute_count_components(n: int, adj: list[list[int]]) -> int:
    """Oracle. Union-find: union every edge, count distinct roots."""
    raise NotImplementedError


if __name__ == "__main__":
    cases = [
        (5, [[1], [0], [3], [2], []], 3),
        (3, [[1, 2], [0, 2], [0, 1]], 1),
        (4, [[], [], [], []], 4),
        (1, [[]], 1),
    ]
    for n, adj, want in cases:
        got = count_components(n, adj)
        assert got == want == brute_count_components(n, adj), (n, adj, got, want)
    print("ok")
