---
name: robin-scientist
description: Use this skill for Robin-style biomedical scientific discovery based on FutureHouse's Nature 2026 Robin paper and public implementation. Trigger when the user asks for Robin, AI Scientist for experimental biology, drug repurposing, therapeutic hypothesis generation, lab-in-the-loop discovery, Crow/Falcon/Finch workflows, LLM-judge tournament ranking, BTL ranking, or analysis of the Robin paper and its implementation details.
---

# Robin Scientist

This skill implements the Robin pattern for experimental biology and therapeutic discovery. Keep the scope biomedical unless the user explicitly asks for an abstraction to another field.

## First Move

1. Treat primary sources as authoritative: Nature article, arXiv preprint, Supplementary Information, Supplementary Tables, and the Future-House/robin repository.
2. Be explicit about dates: arXiv preprint was submitted on 2025-05-19; Nature article was published on 2026-05-19.
3. Do not present Robin as fully autonomous wet-lab science. Robin automates the intellectual loop; humans still run physical experiments and can choose which candidates to test.

## Core Workflow

Use this sequence for Robin-style work:

1. Disease input: accept only the disease name for manuscript-faithful runs.
2. Assay generation: use o4-mini to generate literature queries, Crow for concise reviews, then o4-mini to propose cell-culture assays.
3. Assay ranking: use Claude 3.7 Sonnet as LLM judge, pairwise comparisons, then BTL/choix strength scores.
4. Candidate generation: synthesize the selected assay into a drug-discovery goal, use Crow for therapeutic/background queries, o4-mini to propose single-agent candidates.
5. Candidate validation: use Falcon for detailed candidate reports, then LLM-judge tournament ranking.
6. Lab-in-the-loop: human scientists test selected candidates in vitro.
7. Data analysis: Finch analyzes raw or semi-processed flow-cytometry or RNA-seq data in a Jupyter/Docker environment, then a consensus/meta-analysis distills results.
8. Iteration: feed experimental insights back into candidate generation.

## Load References

- For hard facts, publication timeline, and verified source URLs: read `references/source-map.md`.
- For the system workflow, public repo entrypoints, and parameter defaults: read `references/workflow.md`.
- For the dAMD case, drug rounds, assay details, and quantitative outcomes: read `references/damd-case.md`.
- For LLM judge, BTL ranking, Finch, BixBench, and evaluation caveats: read `references/evaluation.md`.
- For prompts, rubrics, and implementation limits: read `references/prompts-and-limits.md`.

## Scripts

- `scripts/scaffold_robin_run.py`: creates a manuscript-faithful `run_robin.py` wrapper for the official Robin repo.
- `scripts/extract_robin_tables.py`: reads Nature Supplementary Tables xlsx and recomputes selected drug and BixBench metrics.
- `scripts/btl_rank.py`: fits a Bradley-Terry-Luce ranking from pairwise winner/loser CSV data.

Run syntax checks before trusting edits:

```bash
python3 -m py_compile scripts/*.py
```

## Guardrails

- Do not invent missing wet-lab results, clinical efficacy, safety claims, or regulatory readiness.
- Do not copy the official repository into a deliverable unless the user asks. Prefer scaffolding around the official repo.
- Do not overstate generality. The architecture may transfer; the demonstrated implementation is experimental biology and drug discovery.
- Distinguish manuscript claims from public-code behavior when they differ. Example: the paper discusses launching 10 Finch trajectories, one RNA-seq figure references eight trajectories, and the current public code uses `PARALLEL_ANALYSIS = 5`.
