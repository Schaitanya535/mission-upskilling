"""
Problem 4 — Greedy nearest-neighbour walk on a proximity graph.  *** mini-HNSW ***

This is M3 in miniature: ONE layer of an HNSW. You have points (2-D for easy
intuition), a graph over them (each node linked to a few near neighbours), an
entry node, and a query point. Walk the graph GREEDILY toward the query.

    points = [(0,0),(1,0),(2,0),(3,0),(4,0)]   # a line
    adj    = [[1],[0,2],[1,3],[2,4],[3]]        # chain
    greedy_nn_walk(points, adj, entry=0, query=(3.4, 0)) -> 3
        # 0 -> 1 -> 2 -> 3, neighbour 4 is farther than 3 -> stop

Rule each step: among CURRENT node + its neighbours, move to whichever is
closest to query. Stop when no neighbour is closer than where you stand
(a local minimum). Return that node id. Use squared Euclidean distance
(no sqrt needed — monotonic, cheaper; the M1 "dot-not-cosine" trick again).

Insight to discover:
- Greedy hill-descent. The min-heap/priority-queue of Problem 3 collapses to
  "pick the single best neighbour" — beam width 1.
- THE BIG LESSON (recall): greedy can get STUCK in a local minimum and return
  the WRONG nearest neighbour if the graph is poorly connected. That gap is
  exactly why HNSW stacks LAYERS (long hops up top to skip across the space)
  and widens the beam (`ef`, Problem 5). Greedy == brute only when the graph
  is navigable. Find a graph where they DISAGREE and write it in a comment.

Oracle (write it, different method): brute force — linear scan all points,
return the id with min squared distance to query. The "true" answer greedy
is trying to approximate. The test graphs below are connected enough that
greedy reaches it; that equality is NOT guaranteed in general (the recall@k
you'll measure in M3).

Target: O(hops * avg_degree) — independent of total point count (the whole
point of an index).
"""

import heapq


type Point = tuple[float, float]


def get_euclidian_dist(p1: Point, p2: Point) -> float:
    x1, y1 = p1
    x2, y2 = p2
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def bestfit_nn_walk(
    points: list[tuple[float, float]],
    adj: list[list[int]],
    entry: int,
    query: tuple[float, float],
) -> int:
    src_point = points[entry]
    dist_from_src = get_euclidian_dist(query, src_point)
    visited = [False] * len(points)
    min_dist_node: tuple[float, int] = (float("inf"), -1)
    heap: list[tuple[float, int]] = [(dist_from_src, entry)]
    visited[entry] = True
    while heap:
        dist, node = heapq.heappop(heap)
        if dist < min_dist_node[0]:
            min_dist_node = (dist, node)
        for adj_node in adj[node]:
            adj_dist = get_euclidian_dist(query, points[adj_node])
            if adj_dist <= dist and (not visited[adj_node]):
                heapq.heappush(heap, (adj_dist, adj_node))

    return min_dist_node[1]


def greedy_nn_walk(
    points: list[tuple[float, float]],
    adj: list[list[int]],
    entry: int,
    query: tuple[float, float],
) -> int:
    raise NotImplemented


def brute_nn(points: list[tuple[float, float]], query: tuple[float, float]) -> int:
    """Oracle. Linear scan, min squared distance. The true nearest neighbour."""
    raise NotImplementedError


if __name__ == "__main__":
    line = [(0.0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
    chain = [[1], [0, 2], [1, 3], [2, 4], [3]]
    cases = [
        (line, chain, 0, (3.4, 0), 3),
        (line, chain, 0, (0.1, 0), 0),
        (line, chain, 4, (1.9, 0), 2),
    ]
    for points, adj, entry, query, want in cases:
        got = greedy_nn_walk(points, adj, entry, query)
        print(got)
        # assert got == want == brute_nn(points, query), (entry, query, got, want)
    print("ok")
