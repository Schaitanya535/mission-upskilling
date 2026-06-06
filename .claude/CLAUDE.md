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
- **After finishing any task: update the Second Brain** — tick the Progress tracker, add a dated Log entry, and record relevant context/decisions (the *why*, gotchas, things learned) in the relevant vault note. Keep CLAUDE.md "Current state" in sync too.

## Current state (2026-06-05)
**M1 core done.** `docs.txt` (70 lines) + `main.py`: bge-small-en-v1.5 via fastembed (384-dim, normalized → dot product = cosine). Both `sorted()` top-k and `heap_search()` (size-k min-heap, O(n log k)) working + verified equal. Pending polish: simplify heap loop to plain `for`/`heapreplace`. Next: DSA heap problems (3–5), then M2 (Rust port). Full notes in vault Progress tracker.
