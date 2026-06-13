import heapq

"""
Problem 5 (stretch) — Best-first beam search on a proximity graph.  *** HNSW efSearch ***

Problem 4 with beam width 1 gets stuck in local minima. Widen the beam: keep
the `ef` best candidates seen so far and always expand the closest UNvisited
one. Return the top-`k` nearest found. This is literally HNSW's search-layer
routine and the `ef` (efSearch) knob: bigger ef -> higher recall, slower.

    beam_search(points, adj, entry=0, query=q, k=1, ef=4) -> [true_nn_id]

Two heaps, the classic HNSW pair (mirror of your median_stream two-heap trick):
- candidates: MIN-heap by distance -> pop the closest frontier node to expand.
- results:    MAX-heap by distance (size <= ef) -> root = the worst kept; a new
              node beats it only if closer, then heapreplace. (Negate, or use
              3.14 `*_max` like you did in median_stream / task_scheduler.)

Insight to discover:
- Stop when the closest candidate is farther than the worst result AND results
  is full — nothing left can improve the set. Why is that the correct cutoff?
- ef >= number of points degenerates to brute force (visits everything).
  ef = 1 degenerates to Problem 4's greedy walk. ef is the recall/latency dial
  (ties to M8). Sweep ef on a graph where greedy failed and watch recall climb.

Oracle (write it, different method): brute force top-k — sort all points by
squared distance to query, take first k. With ef large enough on these graphs,
beam_search must match it exactly.

Target: visits O(ef * avg_degree) nodes, not all n.
"""


def beam_search(
    points: list[tuple[float, float]],
    adj: list[list[int]],
    entry: int,
    query: tuple[float, float],
    k: int,
    ef: int,
) -> list[int]:
    raise NotImplementedError


def brute_top_k(
    points: list[tuple[float, float]], query: tuple[float, float], k: int
) -> list[int]:
    """Oracle. Sort all points by squared distance, return first k ids."""
    raise NotImplementedError


if __name__ == "__main__":
    line = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
    chain = [[1], [0, 2], [1, 3], [2, 4], [3]]
    cases = [
        (line, chain, 0, (3.4, 0), 1, 4, [3]),
        (line, chain, 0, (3.4, 0), 2, 4, [3, 4]),
        (line, chain, 0, (0.1, 0), 3, 5, [0, 1, 2]),
    ]
    for points, adj, entry, query, k, ef, want in cases:
        got = beam_search(points, adj, entry, query, k, ef)
        assert sorted(got) == sorted(want) == sorted(brute_top_k(points, query, k)), (
            query, k, ef, got, want,
        )
    print("ok")
