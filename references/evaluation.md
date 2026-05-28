# Evaluation And Ranking

## LLM Judge

Robin uses Claude 3.7 Sonnet as the judge for pairwise comparisons. The judge is used for:

- Experimental assay ranking.
- Therapeutic candidate ranking.

Prompt generation is itself a design contribution:

1. Domain experts performed pairwise comparisons of Robin therapeutic candidate hypotheses.
2. Those expert evaluations were given to Gemini 2.5 Pro Preview.
3. Gemini generated the prompt intended to elicit judge behavior aligned with expert preferences.

Reported judge alignment:

- Average overlap: 7.25 of top 10 hypotheses matched experts' top 10.
- Intra-rater consistency: LLM judge 88% on repeated pairwise comparisons.
- Human expert repeated-choice consistency: 61%.

## BTL Ranking

Robin ranking uses pairwise comparison outcomes and Bradley-Terry-Luce strength parameters.

Official implementation details:

- If ranking 25 or fewer hypotheses, compare all unordered pairs.
- If more than 25 hypotheses, randomly sample 300 pairs.
- Public code uses `choix.ilsr_pairwise(..., alpha=0.1)`.
- Example full notebook with 10 assays produces 45 assay comparisons.
- Example full notebook with 30 therapeutic candidates produces 300 sampled comparisons.

Use `scripts/btl_rank.py` when a deterministic local BTL pass is needed without API calls.

## Finch

Finch is an autonomous, Jupyter-native data analysis agent introduced in BixBench and run through Aviary.

Important implementation details:

- Execution environment: pre-built Docker container `BixBench-env:v1.0`.
- Tools: `edit_cell` and `submit_answer`.
- Prompting: ReAct-style reasoning/action loop.
- Public Robin code runs data analysis through Edison platform task name `job-futurehouse-data-analysis-crow-high`.
- Public code constant: `PARALLEL_ANALYSIS = 5`.
- Paper text says Robin can launch 10 Finch analysis trajectories.
- Figure 3C says eight RNA-seq analysis trajectories.

Do not collapse these into a single universal trajectory count.

## BixBench-Style Supplementary Table

The Supplementary Tables workbook contains `Supp Table 10` with 170 rows. Recomputing mean accuracy from the `finch_accuracy` and `llm_accuracy` columns gives:

- Overall Finch mean accuracy: 0.2275.
- Overall LLM mean accuracy: 0.0156.
- Statistics category Finch mean: 0.4785.
- Bioinformatics category Finch mean: 0.1527.

These values match the rough public claim that Finch substantially outperforms a plain LLM baseline, but keep the exact computation tied to the table.

## Rubrics

Supplementary rubrics cover flow cytometry and RNA-seq.

Flow cytometry rubric checks:

- Main cell population gate.
- Singlet/doublet gate.
- DAPI live/dead gate.
- Quality of gating plots.
- Appropriate population delineation method.
- Debris/dead-cell removal.
- Plate normalization.
- MFI calculation per replicate.
- Mean and standard deviation.
- One-tailed tests when looking only for increases.
- Multiple testing correction if required.
- Comparison to vehicle control.
- Identification of significant enhancers.

RNA-seq rubric checks:

- Load differential-expression packages.
- Import and tidy raw counts, identify technical replicates.
- Use a count-aware model such as DESeq2 or edgeR.
- Use FDR-adjusted p-values.
- Report effect size, adjusted and unadjusted p-values, and model specification.
