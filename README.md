# Robin Scientist Skill

Robin Scientist is an agent skill for Robin-style biomedical scientific discovery workflows, based on FutureHouse's Nature paper, arXiv preprint, supplementary materials, and public `Future-House/robin` implementation.

It helps an AI agent preserve the important details of the Robin system while using progressive disclosure: the main `SKILL.md` stays small, paper details live in `references/`, and deterministic helpers live in `scripts/`.

## Scope

Use this skill for:

- Robin paper analysis and implementation mapping
- biomedical therapeutic hypothesis generation
- drug repurposing workflows
- disease-to-assay-to-candidate discovery loops
- Crow / Falcon / Finch role decomposition
- lab-in-the-loop experimental iteration
- LLM-judge pairwise ranking and Bradley-Terry-Luce scoring
- dAMD / ripasudil / ROCK inhibition case analysis

Do not treat this as a general all-science automation framework without explicitly adapting the domain assumptions. The demonstrated Robin implementation is biomedical and therapeutic-discovery oriented.

## Source Grounding

Primary sources:

- Nature article: [A multi-agent system for automating scientific discovery](https://www.nature.com/articles/s41586-026-10652-y), published 2026-05-19
- arXiv preprint: [arXiv:2505.13400](https://arxiv.org/abs/2505.13400), submitted 2025-05-19
- Official implementation: [Future-House/robin](https://github.com/Future-House/robin)
- FutureHouse announcement: [Demonstrating end-to-end scientific discovery with Robin](https://www.futurehouse.org/research-announcements/demonstrating-end-to-end-scientific-discovery-with-robin-a-multi-agent-system)

This repository is not the official Robin implementation. It is a skill layer that helps an agent understand, reproduce, scaffold, and audit Robin-style workflows.

## What Robin Contributes

Robin connects four pieces into one discovery loop:

1. Literature-grounded hypothesis generation through Crow and Falcon.
2. Experimental assay and therapeutic candidate ranking through an LLM-judge tournament.
3. Finch-based analysis of experimental data such as flow cytometry and RNA-seq.
4. Iterative feedback from lab results into the next round of therapeutic hypotheses.

The key distinction is lab-in-the-loop: the AI system performs the intellectual work of proposing, ranking, interpreting, and refining hypotheses, while humans still execute physical wet-lab experiments.

## Repository Layout

```text
robin-scientist/
├── SKILL.md
├── README.md
├── LICENSE
├── references/
│   ├── source-map.md
│   ├── workflow.md
│   ├── damd-case.md
│   ├── evaluation.md
│   └── prompts-and-limits.md
└── scripts/
    ├── scaffold_robin_run.py
    ├── extract_robin_tables.py
    └── btl_rank.py
```

File roles:

- `SKILL.md`: trigger, scope, workflow, and guardrails for the agent.
- `references/source-map.md`: source URLs, publication dates, and verified corrections.
- `references/workflow.md`: public repo workflow, function entrypoints, parameters, and output structure.
- `references/damd-case.md`: dry AMD case details, candidate rounds, assay details, and quantitative results.
- `references/evaluation.md`: LLM judge, BTL ranking, Finch, BixBench-style metrics, and rubrics.
- `references/prompts-and-limits.md`: prompt surfaces, judging criteria, and implementation limits.
- `scripts/scaffold_robin_run.py`: create a small runner around the official Robin repo.
- `scripts/extract_robin_tables.py`: recompute selected metrics from the Nature supplementary tables workbook.
- `scripts/btl_rank.py`: fit a local Bradley-Terry-Luce ranking from pairwise winner/loser CSV data.

## Quick Start

Install or copy this folder into the skill directory used by your agent host. For a Codex-style setup:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/TeamZaobi/robin-scientist.git ~/.agents/skills/robin-scientist
```

Then start a fresh agent session so the host reloads available skills.

## Script Examples

Create a manuscript-style Robin runner:

```bash
python3 scripts/scaffold_robin_run.py \
  --out-dir /tmp/robin-run \
  --disease "dry age-related macular degeneration" \
  --paper-defaults
```

Recompute selected supplementary-table metrics:

```bash
python3 scripts/extract_robin_tables.py /path/to/41586_2026_10652_MOESM3_ESM.xlsx
```

Fit a BTL ranking from pairwise comparisons:

```bash
python3 scripts/btl_rank.py pairwise_results.csv
```

Expected CSV columns include either `winner_id` / `loser_id` or `Winner ID` / `Loser ID`.

## Validation

Check script syntax:

```bash
python3 - <<'PY'
from pathlib import Path
import ast

for path in Path("scripts").glob("*.py"):
    ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    print(f"OK {path.name}")
PY
```

Optional smoke test:

```bash
python3 scripts/scaffold_robin_run.py \
  --out-dir /tmp/robin-scaffold-test \
  --disease "dry age-related macular degeneration" \
  --paper-defaults
```

## Important Caveats

- Nature publication date and arXiv date differ: Nature is 2026-05-19; arXiv is 2025-05-19.
- The full DOI is `10.1038/s41586-026-10652-y`.
- Finch trajectory counts vary by source: paper text discusses 10 trajectories, one RNA-seq figure references eight, and the public code currently uses `PARALLEL_ANALYSIS = 5`.
- Do not collapse ripasudil effect sizes into one number. The paper text, human analysis, and supplementary tables report different values under different analysis contexts.
- Do not present unverified secondary-source claims as primary paper facts.
- This skill does not provide medical advice, clinical validation, or regulatory conclusions.

## Relationship To The Official Robin Repo

The official Robin implementation requires Python 3.12+, Edison platform access, LLM provider credentials, and often Docker/Jupyter. This skill does not vendor that code. It provides:

- workflow interpretation
- prompt and source routing
- local scaffolding around the official repo
- BTL and supplementary-table utilities
- agent guardrails for accurate Robin discussion

Use the official repository when you need to run Robin itself.

## License

Apache-2.0. This repository is an independent skill layer and does not claim affiliation with FutureHouse.
