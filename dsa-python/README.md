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
