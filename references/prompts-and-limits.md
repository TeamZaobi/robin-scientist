# Prompts And Limits

## Prompt Inventory

The Supplementary Information and public `robin/prompts.py` expose the main prompt surfaces:

- Assay literature query generation.
- Assay proposal generation as strict JSON array.
- Crow assay hypothesis evaluation.
- Assay LLM judge prompt.
- Candidate-generation goal synthesis.
- Candidate literature query generation.
- Candidate proposal generation with explicit `<CANDIDATE START>` / `<CANDIDATE END>` blocks.
- Falcon candidate report generation.
- Finch flow cytometry analysis prompt.
- Candidate LLM judge prompt.
- Data interpretation prompt, returning four `<>`-separated fields.
- Follow-up assay suggestion prompt.

## Candidate Judge Criteria

Candidate ranking emphasizes:

- Strength and relevance of supporting evidence.
- Mechanism clarity, plausibility, and specificity.
- Safety, tolerability, and risk profile.
- Feasibility of experimental plan and drug delivery.
- Scientific novelty balanced against evidence and safety.

The judge is instructed to focus on implications for efficacy, safety, and translatability rather than excessive pharmacology detail unless that detail changes the decision.

## Current Limits In The Paper

The Discussion section lists implementation limits that should be retained:

- Robin generates experimental outlines, not precise executable protocols.
- Finch still depends heavily on domain-expert prompt engineering.
- Better alignment of hypothesis generation/evaluation with human judgment remains future work.
- Real therapeutic validation still requires preclinical and clinical testing.

## Use In A Skill

When using this skill, copy the structure and decision criteria, not long prompt text. If exact prompt reconstruction is needed, inspect:

- Official repo: `robin/prompts.py`
- Supplementary Information figures for prompt snapshots

Avoid loading all prompts into context unless the user is explicitly designing or auditing the prompt layer.
