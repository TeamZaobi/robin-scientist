#!/usr/bin/env python3
"""Create a small runner around the official FutureHouse Robin repository."""

from __future__ import annotations

import argparse
from pathlib import Path


RUNNER_TEMPLATE = '''\
import asyncio
import logging

from robin.analyses import data_analysis
from robin.assays import experimental_assay
from robin.candidates import therapeutic_candidates
from robin.configuration import RobinConfiguration


config = RobinConfiguration(
    disease_name={disease_name!r},
    num_queries={num_queries},
    num_assays={num_assays},
    num_candidates={num_candidates},
)

logger = logging.getLogger("robin")
logger.setLevel(logging.INFO)


async def main():
    candidate_generation_goal = await experimental_assay(configuration=config)
    await therapeutic_candidates(
        candidate_generation_goal=candidate_generation_goal,
        configuration=config,
    )

{data_block}


if __name__ == "__main__":
    asyncio.run(main())
'''


DATA_BLOCK = '''\
    experimental_insights = await data_analysis(
        data_path={data_path!r},
        data_analysis_type={data_analysis_type!r},
        goal=candidate_generation_goal,
        configuration=config,
    )
    await therapeutic_candidates(
        candidate_generation_goal=candidate_generation_goal,
        configuration=config,
        experimental_insights=experimental_insights,
    )
'''


NO_DATA_BLOCK = "    # Add data_analysis(...) here after lab data are available."


ENV_TEMPLATE = """\
# Fill these before running Robin.
EDISON_API_KEY=
OPENAI_API_KEY=
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", required=True, help="Directory to create.")
    parser.add_argument("--disease", required=True, help="Disease name only.")
    parser.add_argument(
        "--paper-defaults",
        action="store_true",
        help="Use manuscript-like 5 queries, 10 assays, 30 candidates.",
    )
    parser.add_argument("--num-queries", type=int, default=None)
    parser.add_argument("--num-assays", type=int, default=None)
    parser.add_argument("--num-candidates", type=int, default=None)
    parser.add_argument("--data-path", default=None)
    parser.add_argument(
        "--data-analysis-type",
        choices=["flow_cytometry", "RNA_seq"],
        default="flow_cytometry",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.paper_defaults:
        num_queries, num_assays, num_candidates = 5, 10, 30
    else:
        num_queries, num_assays, num_candidates = 3, 3, 5

    num_queries = args.num_queries or num_queries
    num_assays = args.num_assays or num_assays
    num_candidates = args.num_candidates or num_candidates

    data_block = (
        DATA_BLOCK.format(
            data_path=args.data_path,
            data_analysis_type=args.data_analysis_type,
        )
        if args.data_path
        else NO_DATA_BLOCK
    )

    (out_dir / "run_robin.py").write_text(
        RUNNER_TEMPLATE.format(
            disease_name=args.disease,
            num_queries=num_queries,
            num_assays=num_assays,
            num_candidates=num_candidates,
            data_block=data_block,
        ),
        encoding="utf-8",
    )
    (out_dir / ".env.example").write_text(ENV_TEMPLATE, encoding="utf-8")
    (out_dir / "README.txt").write_text(
        "Run inside a clone of https://github.com/Future-House/robin after installing "
        "the official package and setting API keys. For manuscript-faithful input, "
        "keep disease_name as a disease name only.\n",
        encoding="utf-8",
    )
    print(f"Created Robin runner in {out_dir}")


if __name__ == "__main__":
    main()
