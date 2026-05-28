#!/usr/bin/env python3
"""Fit a simple Bradley-Terry-Luce ranking from pairwise winner/loser data."""

from __future__ import annotations

import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path


def _pick(row: dict[str, str], names: tuple[str, ...]) -> str | None:
    lower = {k.lower().strip(): v for k, v in row.items()}
    for name in names:
        if name.lower() in lower and lower[name.lower()] != "":
            return lower[name.lower()]
    return None


def read_games(path: Path) -> tuple[list[tuple[str, str]], dict[str, str]]:
    games: list[tuple[str, str]] = []
    labels: dict[str, str] = {}
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            winner = _pick(row, ("winner_id", "Winner ID", "winner"))
            loser = _pick(row, ("loser_id", "Loser ID", "loser"))
            if winner is None or loser is None:
                continue
            winner_id = winner.strip()
            loser_id = loser.strip()
            if not winner_id or not loser_id:
                continue
            games.append((winner_id, loser_id))
            winner_label = _pick(row, ("winner_name", "Winner"))
            loser_label = _pick(row, ("loser_name", "Loser"))
            if winner_label:
                labels.setdefault(winner_id, winner_label)
            if loser_label:
                labels.setdefault(loser_id, loser_label)
    return games, labels


def fit_btl(
    games: list[tuple[str, str]],
    alpha: float = 0.1,
    max_iter: int = 1000,
    tol: float = 1e-10,
) -> dict[str, float]:
    ids = sorted({i for game in games for i in game})
    if not ids:
        return {}
    index = {item_id: pos for pos, item_id in enumerate(ids)}
    wins = [alpha for _ in ids]
    comparisons: dict[int, list[int]] = defaultdict(list)
    for winner, loser in games:
        wi = index[winner]
        li = index[loser]
        wins[wi] += 1.0
        comparisons[wi].append(li)
        comparisons[li].append(wi)

    strengths = [1.0 for _ in ids]
    for _ in range(max_iter):
        updated = strengths[:]
        for i in range(len(ids)):
            denom = 0.0
            for j in comparisons[i]:
                denom += 1.0 / (strengths[i] + strengths[j])
            if denom > 0:
                updated[i] = wins[i] / denom
        scale = sum(updated) / len(updated)
        updated = [value / scale for value in updated]
        delta = max(abs(math.log(updated[i] / strengths[i])) for i in range(len(ids)))
        strengths = updated
        if delta < tol:
            break
    return {item_id: math.log(strengths[index[item_id]]) for item_id in ids}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--alpha", type=float, default=0.1)
    args = parser.parse_args()

    games, labels = read_games(args.csv_path)
    scores = fit_btl(games, alpha=args.alpha)
    rows = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
    writer = csv.writer(__import__("sys").stdout)
    writer.writerow(["rank", "id", "label", "strength_score"])
    for rank, (item_id, score) in enumerate(rows, 1):
        writer.writerow([rank, item_id, labels.get(item_id, ""), f"{score:.10f}"])


if __name__ == "__main__":
    main()
