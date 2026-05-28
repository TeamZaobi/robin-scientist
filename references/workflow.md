# Robin Workflow

## Paper-Level Architecture

Robin combines:

- Crow: concise literature review agent, based on PaperQA2-style scientific retrieval and synthesis.
- Falcon: deep literature review agent for comprehensive therapeutic-candidate reports.
- Finch: Jupyter-native data analysis agent for flow cytometry and RNA-seq style workflows.
- LLM judge: Claude 3.7 Sonnet for pairwise comparisons.
- Prompt meta-design: human expert pairwise evaluations were given to Gemini 2.5 Pro Preview to generate the judge prompt.

## Public Repository Entry Points

Official package functions:

- `robin.assays.experimental_assay(configuration)`
- `robin.candidates.therapeutic_candidates(candidate_generation_goal, configuration, experimental_insights=None)`
- `robin.analyses.data_analysis(data_path, data_analysis_type, goal, configuration)`
- `robin.configuration.RobinConfiguration`

Manuscript-like full notebook configuration:

```python
config = RobinConfiguration(
    disease_name="dry age-related macular degeneration",
    num_queries=5,
    num_assays=10,
    num_candidates=30,
)
```

Repo demo defaults inside `RobinConfiguration` are smaller:

- `num_queries=3`
- `num_assays=3`
- `num_candidates=5`
- `llm_name="o4-mini"`

## Execution Steps

1. Generate assay literature queries with o4-mini.
2. Send query dictionary to Edison platform using Crow.
3. Generate assay proposals as strict JSON array: `strategy_name`, `reasoning`.
4. Ask Crow for detailed reports on each assay candidate.
5. Rank assay reports by LLM-judge tournament.
6. Synthesize the winning assay into a therapeutic candidate generation goal.
7. Generate two classes of candidate literature queries: therapeutic landscape and disease mechanism.
8. Use Crow for candidate literature review.
9. Generate candidate blocks with exact markers:
   - `<CANDIDATE START>`
   - `CANDIDATE:`
   - `HYPOTHESIS:`
   - `REASONING:`
   - `<CANDIDATE END>`
10. Ask Falcon for detailed reports with sections: overview, therapeutic history, mechanism of action, expected effect, overall evaluation.
11. Rank candidates by LLM-judge tournament and BTL strength score.
12. Human lab tests selected candidates.
13. Finch analyzes data, then Robin distills actionable insights and suggests follow-up assays.
14. Feed insights into another candidate generation round.

## Output Structure

Official repo outputs under `robin_output/<disease>_<timestamp>/`:

- `experimental_assay_literature_reviews/`
- `experimental_assay_detailed_hypotheses/`
- `experimental_assay_ranking_results.csv`
- `experimental_assay_summary.txt`
- `therapeutic_candidate_literature_reviews/`
- `therapeutic_candidate_detailed_hypotheses/`
- `therapeutic_candidate_ranking_results.csv`
- `ranked_therapeutic_candidates.csv`
- `therapeutic_candidates_summary.txt`
- optional `data_analysis/`
- optional `_experimental` suffixed candidate outputs after experimental insights are fed back.

## Environment

The official repo requires:

- Python 3.12+
- `EDISON_API_KEY` for Edison platform agents, including Crow/Falcon and data analysis features.
- An LLM provider key such as `OPENAI_API_KEY`.
- LiteLLM-compatible model config.
- Docker is recommended by the repo for a reproducible environment.
