# Source Map

## Primary Sources

- Nature article: `A multi-agent system for automating scientific discovery`, published 2026-05-19, DOI `10.1038/s41586-026-10652-y`.
- arXiv preprint: `arXiv:2505.13400`, submitted 2025-05-19.
- Official code: `https://github.com/Future-House/robin`, Apache-2.0.
- Supplementary Information: Nature MOESM1 PDF for prompts, figures, rubrics, and experimental materials.
- Supplementary Tables: Nature MOESM3 xlsx for drug MFI data, rankings, reference validation, and BixBench-style benchmark rows.

## Verified Corrections

- `s41586-026-10652-y` is the Nature article identifier inside the DOI, not by itself a DOI.
- The paper is Nature 2026, but the arXiv version is 2025.
- Robin is not a generic all-science skill in its current implementation. It is demonstrated for experimental biology and therapeutic discovery.
- The public repo defaults are small demo values, but the paper/full notebook uses `num_queries=5`, `num_assays=10`, `num_candidates=30`.
- Finch trajectory counts need nuance: the paper says Robin can launch 10 Finch trajectories; Figure 3C discusses eight RNA-seq trajectories; the public code constant is `PARALLEL_ANALYSIS = 5`.
- OpenAI Deep Research comparisons and `$10.76` style cost claims were not found in the primary paper text or official repo during this audit. Treat them as secondary-source claims unless separately verified.

## URLs To Prefer

- Nature: https://www.nature.com/articles/s41586-026-10652-y
- arXiv: https://arxiv.org/abs/2505.13400
- FutureHouse Robin repo: https://github.com/Future-House/robin
- FutureHouse Robin announcement: https://www.futurehouse.org/research-announcements/demonstrating-end-to-end-scientific-discovery-with-robin-a-multi-agent-system
- Nature press release covering Robin and Co-Scientist: https://www.natureasia.com/en/info/press-releases/detail/9330

## Local Audit Guidance

For future audits, refresh the official Robin repository and download the current Nature supplementary PDF/workbook before using local extracted data as evidence.
