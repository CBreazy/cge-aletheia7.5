# rewrite.py

from dataclasses import dataclass
from typing import List, Tuple, Dict
import re

@dataclass
class RewriteCandidate:
    x: int
    y: int
    value: int
    label: str
    depth: int

def parse_rewrite_candidates(labels: List[str]) -> List[RewriteCandidate]:
    candidates = []
    for label in labels:
        match = re.match(r"\((\d+),(\d+)\)=(\d+)(_amp)*", label)
        if match:
            x, y, val = int(match.group(1)), int(match.group(2)), int(match.group(3))
            depth = label.count("_amp")
            candidates.append(RewriteCandidate(x, y, val, label, depth))
    return candidates

def group_candidates_by_depth(candidates: List[RewriteCandidate]) -> Dict[int, List[RewriteCandidate]]:
    depth_map = {}
    for c in candidates:
        depth_map.setdefault(c.depth, []).append(c)
    return depth_map

def resolve_grid_from_candidates(candidates: List[RewriteCandidate], width=10, height=10) -> List[List[int]]:
    grid = [[0 for _ in range(width)] for _ in range(height)]
    cell_map: Dict[Tuple[int, int], RewriteCandidate] = {}
    for c in candidates:
        key = (c.y, c.x)
        if key not in cell_map or c.depth > cell_map[key].depth:
            cell_map[key] = c
    for (y, x), candidate in cell_map.items():
        if 0 <= y < height and 0 <= x < width:
            grid[y][x] = candidate.value
    return grid
