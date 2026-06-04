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
- Python tooling: **uv** (`uv add`, `uv run`). Each Python subproject gets its own `.venv` inside it.
- **Chaitanya writes all the code by hand** — this is a learning project. Claude explains, plans, reviews, harvests data; does NOT write the implementation unless asked.
- M1 corpus: one idea per physical line in `docs.txt`; load with strip + skip-blanks.
- M1 storage is in-memory on purpose; persistence is M5 (built by hand). Cache embeddings to a file only to avoid recompute — that's not "the database".
- DSA practice done in Python, drilled when a milestone surfaces the structure (heap@M1, graph@M3).
- Prefers concise / caveman-style replies; comment-out over delete; explain reasoning before workarounds.

## Current state (2026-06-04)
M1 in progress. `docs.txt` (70 lines) created. Next: embeddings + cosine + top-k (`sorted()` then `heapq`).
