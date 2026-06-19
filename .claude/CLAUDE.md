# mission-upskilling

Chaitanya's job-hunt upskilling hub. Goal: grow **DSA + LLD + HLD** interview skills by **building**, not grinding LeetCode. Targeting JS-developer roles. Project may touch any language — Rust + AI by design.

## Flagship project: Vector Search Engine (from scratch)

Build a small semantic-search / embeddings DB. Rust core, thin JS/TS layer, AI via embeddings. Every interview pillar surfaces naturally while building.

**Full plan + reasoning lives in the Obsidian vault — do not duplicate here, read it:**
- Plan: `/Users/chaitanyasura/Documents/Second Brain/notes/Personal/Projects/Vector Search Engine - Upskill Project.md`
- Progress tracker (checkbox source of truth): `/Users/chaitanyasura/Documents/Second Brain/notes/Personal/Projects/Vector Search Engine - Progress.md`

Always read the Progress tracker first to see current milestone + ticked items.

### Milestones (summary — detail in vault)
- M1 Brute-force search in **Python** (in-memory) — heaps, cosine, top-k
- M2 Port core to **Rust** — ownership, criterion benchmarks
- M3 **HNSW** index — graphs, greedy search, priority queues (DSA centerpiece)
- M4 LLD pass — `Distance` / `Index` / `Store` traits, pluggable
- M5 Persistence — **build the DB by hand**: bincode + mmap + WAL (no Postgres/pgvector)
- M6 JS/TS layer — napi-rs or WASM + Next.js demo (job tie)
- M7 Docker — Dockerfile, multi-stage, compose, volumes
- M8 Scale story — sharding/replication/quantization design doc

## Repo layout (monorepo, single git repo at root)
```
mission-upskilling/
├── vsearch-py/      # M1 Python prototype (uv project)
│   └── docs.txt     # 70-line test corpus harvested from the vault
├── vsearch/         # M2+ Rust crate (later)
└── dsa-python/      # DSA side-track (later)
```

## Conventions / decisions
- Python tooling: **uv — always**. Every Python subproject (incl. `dsa-python/` and any drill/scratch dir) is created with `uv init` and run with `uv run` / `uv add`. Never hand-make a bare dir + `.py` files or use `python`/`pip` directly. Each subproject gets its own `.venv` inside it.
- **Chaitanya writes all the code by hand** — this is a learning project. Claude explains, plans, reviews, harvests data; does NOT write the implementation unless asked.
- M1 corpus: one idea per physical line in `docs.txt`; load with strip + skip-blanks.
- M1 storage is in-memory on purpose; persistence is M5 (built by hand). Cache embeddings to a file only to avoid recompute — that's not "the database".
- DSA practice done in Python, drilled when a milestone surfaces the structure (heap@M1, graph@M3).
- Prefers concise / caveman-style replies; comment-out over delete; explain reasoning before workarounds.
- **After finishing any task: update the Second Brain** — tick the Progress tracker, add a dated Log entry, and record relevant context/decisions (the *why*, gotchas, things learned) in the relevant vault note. Keep CLAUDE.md "Current state" in sync too.

## Open design notes
- **top-k vs threshold:** top-k = result cap, score threshold = relevance gate. Combine (take top-k, post-filter `score >= min_score`), don't replace. Fixed threshold (0.5) is a per-model/corpus heuristic, not absolute — cosine scores aren't calibrated. Smarter later = relative gap/elbow cutoff (the precision/recall dial; ties to recall@k M3, recall/latency M8). Planned M1.5: optional `min_score` param post-filtering heap output.
- **DECIDED (2026-06-06): M3 before M2.** Build HNSW in Python first (DSA is the #1 goal; full focus on the algorithm), then port to Rust. Conditions: (1) build the Python HNSW **index-based** (nodes in a list, neighbors as integer ids — NOT object refs) so it ports 1:1 to Rust's arena/`Vec` model and supports M5 mmap; (2) M2 keeps a small Rust on-ramp (port brute-force cosine first) before porting HNSW. Executed order: M1 → heap drills → M3(py) → M2(rust) → M4–M8. Numbers stay as labels.

## Current state (2026-06-19)
**Graph drills 2/5 done.** `bfs_shortest_hops` SOLVED — `dist[i]`=fewest edges src→i (`-1` if unreachable), BFS == independent oracle (DFS-with-relaxation). Key insight landed: **set distance on ENQUEUE not dequeue** (`result[nb]=result[front]+1` when queuing) — kills duplicate enqueues + removes need for layer markers; `dist` array doubles as visited (`-1` = unvisited AND the unreachable answer). Bugs caught: (1) marker-leak — `if front==marker and q:` lets the final marker fall through to `result[-1]=layer`, clobbering last node (unreachable island wrongly set); fix = marker branch `continue` unconditionally. (2) oracle `[0]*n` instead of `[-1]*n` → DFS guard always False → returns all zeros. Caveat: relaxation-DFS is exponential worst-case (fine as oracle, not O(n+E)). False-green trap revisited: commented assert + `print` → `ok` is meaningless. Next: drill 3 `dijkstra`.

## Current state (2026-06-19) — drill 1
**Graph drill 1/5 `connected_components` SOLVED.** Both methods agree on all cases (`ok`): flood fill (recursive DFS, `visited` bool array) + union-find oracle (recursive `find` w/ full path compression, `union` by rank, count = `len({find(parent,i) for i in range(n)})` — distinct *roots*, not `set(parent)`). Two non-bugs banked: flood-fill `fill` doesn't mark `start` on entry (fine for undirected via back-edge, fragile for directed); `len(set(parent))` overcounts (only `find`-touched nodes point at root). Teaching aid built: `dsa-python/graphs/union_find_visual.html` (interactive SVG, 4 variant toggles — naive/rank/compression/both, worst-case-chain demo) — **not committed**. Next: drill 2 `bfs_shortest_hops`.

## Current state (2026-06-13)
**Heap drills DONE 5/5.** task_scheduler shipped — greedy max-heap + min-heap cooldown queue `(ready_tick, count, task)`, `ready = tick + n` released on strict `<`. Closed-form oracle `max((maxf-1)*(n+1)+cnt_max, len(tasks))`. All 5 drills (kth-largest, top-k-frequent, merge-k-sorted, median-stream, task-scheduler) pass vs oracle.

**M3 started — graph drills scaffolded** in `dsa-python/graphs/` (5 stubs, heap-drill convention, not solved yet): `connected_components`, `bfs_shortest_hops`, `dijkstra`, `greedy_nn_walk` (mini-HNSW single layer), `beam_search` (= HNSW `efSearch`, stretch). All index-based (`adj: list[list[int]]`, nodes = int ids — the M3 rule). Laddered to land on HNSW: 1-2 traversal, 3 priority-queue search, 4-5 HNSW search loop in miniature + recall/latency.

Next: solve the 5 graph drills in order, then build **M3 HNSW proper** (Python, index-based). See vault Progress tracker.

<!-- prior state below -->
## Current state (2026-06-07)
**M1 DONE + committed. Working REPL demo live.** bge-small-en-v1.5 via fastembed (384-dim, normalized → dot product = cosine). `search.py`: `bruteforce_search` (sorted) + `heap_search` (size-k min-heap), `build_index()`/`query()` split (build-vs-query seam for API), `rel` threshold post-filter. `main.py`: infinite-loop REPL (exit/empty/Ctrl-C handled). Observed: fixed 0.5 threshold lets gibberish through → relative gap/elbow cutoff is the real fix (M1.5).

**Heap drills scaffolded (2026-06-07):** `dsa-python/` is a uv project; `heaps/` has 5 problem stubs (kth-largest, top-k-frequent, merge-k-sorted, median-stream, task-scheduler) — signatures + oracle stubs + insight only, **not solved yet**. Run with `uv run python heaps/<file>.py` → prints `ok` when impl + oracle pass.

Next: **solve the 5 heap drills**, then **M3 HNSW in Python** (index-based — see decided reorder), then M2 Rust port. Full notes in vault Progress tracker.
