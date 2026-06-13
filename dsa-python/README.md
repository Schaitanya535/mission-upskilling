# dsa-python

DSA side-track for mission-upskilling. Drilled when a milestone surfaces a structure.
You write all solutions by hand — Claude curates, explains, reviews.

## heapq cheat-sheet (Python)
- `heapq` is a **min-heap only**. Root = smallest.
- **Max-heap?** Negate on push, negate on pop (`heappush(h, -x)` → `-heappop(h)`).
- `heappush(h, item)` / `heappop(h)` — O(log n). `h[0]` peek — O(1).
- `heapify(list)` — O(n) in place. `heapreplace(h, x)` = pop-then-push (one sift).
- **Tie-break with tuples:** `(key, tiebreak, payload)`. Heap compares element-wise; make field 2 unique (an index/counter) so it never tries to compare the payload.

## heaps/ — problem set
Solve in order. Each file has the signature, constraints, and the heap insight to discover — no solution.

1. `kth_largest.py` — size-k min-heap (== your `heap_search`)
2. `top_k_frequent.py` — hashmap count + heap
3. `merge_k_sorted.py` — heap of list heads (→ M8 scatter-gather)
4. `median_stream.py` — two heaps, kept balanced
5. `task_scheduler.py` — greedy max-heap *(stretch)*

**Drill loop per problem:** read → brute-force first (state its Big-O) → spot why a heap wins → code heap version → test against the brute-force as oracle (same trick as M1).

## graph cheat-sheet (Python)
- **Index-based representation (M3 rule):** nodes = ints `0..n-1`, edges = adjacency list `adj: list[list[int]]` (or `list[list[(nbr, weight)]]` weighted). NEVER object refs/pointers — ints into a list port 1:1 to Rust's `Vec`/arena and let M5 mmap the graph. Build every drill this way.
- **BFS** = `collections.deque`, popleft, set `dist`/`visited` on ENQUEUE. Shortest hops on UNWEIGHTED graphs.
- **DFS** = recursion or explicit stack. Reachability / components / cycles. NOT shortest path.
- **Dijkstra** = min-heap of `(dist, node)`, lazy deletion (skip stale `d > dist[u]`). Shortest path, weights >= 0.
- **Bellman-Ford** = relax all edges n-1 times, no heap. Handles negatives; here it's Dijkstra's independent oracle.
- **Greedy/best-first search** = expand the closest frontier node (heap). The skeleton HNSW greedy search is built on.

## graphs/ — problem set (ladders straight into M3 HNSW)
Solve in order. Each file = signature + cases + brute/oracle stub + the insight to discover — no solution.

1. `connected_components.py` — adjacency-list flood fill (DFS/BFS). Oracle = union-find.
2. `bfs_shortest_hops.py` — BFS level order, why it's optimal unweighted. Oracle = iterative-deepening DFS.
3. `dijkstra.py` — min-heap best-first (the priority-queue core of HNSW search). Oracle = Bellman-Ford.
4. `greedy_nn_walk.py` — **mini-HNSW single layer**: greedy descent to a query; teaches local-minima → why layers exist. Oracle = brute NN.
5. `beam_search.py` — best-first with `ef` candidate set = HNSW `efSearch`; recall/latency dial *(stretch)*. Oracle = brute top-k.

**Why these 5:** 1-2 = graph traversal muscle (visited, queue/stack, adjacency lists). 3 = the priority-queue search HNSW runs. 4-5 = HNSW's actual search loop in miniature, ending at the recall/latency tradeoff you'll measure in M3 and tune in M8.
