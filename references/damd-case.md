# dAMD Case Details

## Disease And Assay Choice

Robin was applied to dry age-related macular degeneration (dAMD). The workflow:

- Reviewed 151 papers to propose 10 dAMD mechanisms/experimental strategies.
- Selected RPE phagocytosis enhancement as the assay direction.
- Suggested fluorescently labelled photoreceptor outer segments, but the lab used pHrodo beads due to availability.
- Used ARPE-19 cells for main phagocytosis assays.

## First Candidate Round

Robin reviewed about 400 papers on RPE phagocytosis and the dAMD therapeutic landscape, then proposed 30 existing drug candidates.

The lab tested the top five from the ranking:

- Exendin-4
- Fingolimod
- MFGE8
- Y-27632
- AICAR + TUDCA

Y-27632, a ROCK inhibitor, was the key first-round hit. The paper connects this to prior evidence that Y-27632 can restore RPE phagocytic efficiency through actin polymerization/cytoskeletal effects.

## Follow-Up RNA-seq

Robin recommended RNA-seq of Y-27632-treated RPE cells. Finch performed differential gene expression and GO enrichment analysis.

Reported findings:

- Y-27632 altered genes involved in actin filament organization.
- It affected small GTPase-mediated signal transduction.
- It affected autophagy-related pathways.
- The paper reports 3-fold upregulation of `ABCA1` with adjusted p-value `2.13e-83` in Y-27632-treated cells.
- `ABCA1` is framed as a lipid efflux pump and possible novel disease-relevant target.

Interpretation to preserve: Y-27632 may enhance initial phagocytic uptake through cytoskeletal rearrangement and promote clearance of internalized material through transcriptional regulation of autophagy. The paper states that further work is required to determine whether these changes are Y-27632-specific or general to phagocytosis-enhancing interventions.

## Iterated Candidate Round

Robin then generated another therapeutic-candidate round using experimental insights.

The paper says 10 drugs from the subsequent iteration were tested experimentally. Figure 4 lists:

- Ripasudil
- GW4064
- B-Ionone
- NECA
- Bay K8644
- KL001
- Rolipram
- Vorinostat
- Simvastatin
- Rapamycin
- Resveratrol

The displayed list has 11 labels, while the prose says 10 tested drugs. Preserve this discrepancy rather than silently resolving it.

## Ripasudil Results

Ripasudil is described as a ROCK inhibitor approved for glaucoma in Japan. The paper reports:

- Finch analysis: ripasudil increased RPE phagocytosis 7.5-fold compared with DMSO controls.
- Human analysis: 1.75-fold increase in Supplementary Figure S14.
- Supplementary Table 4 normalized MFI mean from the xlsx: Ripasudil 1.891, Y-27632 1.612, MFGE8 1.463, DMSO 1.0.
- Supplementary Table 5 normalized MFI mean: Ripasudil 1.537, MFGE8 1.516, Y-27632 1.268, DMSO 1.0.

Do not flatten these into a single effect size. The fold-change differs by analysis pipeline, cell/source context, and table.

## Experimental Materials Worth Preserving

Selected drug working concentrations from Supplementary Table 1:

- Y-27632: 20 uM
- AICAR: 1 mM
- TUDCA: 100 uM
- Exendin-4: 1 uM
- Fingolimod: 1 uM
- MFGE-8: 2.5 ug/mL
- Ripasudil: 100 uM
- Vorinostat: 5 uM
- Simvastatin: 1 uM
- KL001: 50 uM
- Rapamycin: 100 nM

Flow cytometry assay details:

- Drug pretreatment: 60 minutes.
- pHrodo beads added after pretreatment.
- Phagocytosis incubation: 3 hours.
- DAPI used to exclude dead cells.
- Attune NxT flow cytometer.
- MFI of pHrodo signal used as readout.

RNA-seq methods:

- Raw paired-end RNA-seq reads: 2 x 150 bp.
- Alignment: HISAT2 against GRCh38 / GENCODE v44.
- Gene counts: featureCounts.
- Differential expression: DESeq2 in R.
- Volcano plot thresholds in methods: `abs(log2FC) > 1` and adjusted p-value `< 0.05`.
