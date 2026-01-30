from enum import Enum
from typing import List

import numpy as np


class Rank(Enum):
    Highest = "Highest"
    High = "High"
    Med = "Med"
    Low = "Low"
    Lowest = "Lowest"


def get_segments(lst: List):
    segments = np.array_split(lst, 3)
    return [list(seg) for seg in segments]


def get_rank(rank: Rank, lst: List):
    match rank:
        case Rank.Highest:
            return lst[-1]
        case Rank.High:
            return get_segments(lst)[2]
        case Rank.Med:
            return get_segments(lst)[1]
        case Rank.Low:
            return get_segments(lst)[0]
        case Rank.Lowest:
            return lst[0]


final_sequence = [
    # initial
    {"name": "B♮ MAJ_SEVEN", "inversion": 0, "dissonance_rank": Rank.Lowest},
    {"name": "D♮ SEVEN", "inversion": 0, "dissonance_rank": Rank.Lowest},
    {"name": "G♮ MAJ_SEVEN", "inversion": 0, "dissonance_rank": Rank.Lowest},
    {"name": "B♭ SEVEN", "inversion": 0, "dissonance_rank": Rank.Lowest},
    {"name": "E♭ MAJ_SEVEN", "inversion": 0, "dissonance_rank": Rank.Lowest},
    {"name": "E♭ MAJ_SEVEN", "inversion": 0, "dissonance_rank": Rank.Lowest},
    {"name": "A♮ MINOR_SEVEN", "inversion": 0, "dissonance_rank": Rank.Lowest},
    {"name": "D♮ SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    {"name": "G♮ MAJ_SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    {"name": "B♭ SEVEN", "inversion": 0, "dissonance_rank": Rank.Lowest},
    {"name": "E♭ MAJ_SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    {"name": "F♯ SEVEN", "inversion": 0, "dissonance_rank": Rank.Lowest},
    {"name": "B♮ MAJ_SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    {"name": "B♮ MAJ_SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    {"name": "F♮ MINOR_SEVEN", "inversion": 0, "dissonance_rank": Rank.Lowest},
    {"name": "B♭ SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    {"name": "E♭ MAJ_SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    {"name": "E♭ MAJ_SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    {"name": "A♮ MINOR_SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    {"name": "D♮ MINOR_SEVEN", "inversion": 0, "dissonance_rank": Rank.Lowest},
    {"name": "G♮ MAJ_SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    {"name": "G♮ MAJ_SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    {"name": "C♯ MINOR_SEVEN", "inversion": 0, "dissonance_rank": Rank.Lowest},
    {"name": "F♯ SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    {"name": "B♮ MAJ_SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    {"name": "B♮ MAJ_SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    {"name": "F♮ MINOR_SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    {"name": "B♭ SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    {"name": "E♭ MAJ_SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    {"name": "E♭ MAJ_SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    {"name": "C♯ MINOR_SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    {"name": "F♯ SEVEN", "inversion": 0, "dissonance_rank": Rank.Low},
    # first repeat
    {"name": "B♮ MAJ_SEVEN", "inversion": 1, "dissonance_rank": Rank.Lowest},
    {"name": "D♮ SEVEN", "inversion": 1, "dissonance_rank": Rank.Lowest},
    {"name": "G♮ MAJ_SEVEN", "inversion": 1, "dissonance_rank": Rank.Lowest},
    {"name": "B♭ SEVEN", "inversion": 1, "dissonance_rank": Rank.Lowest},
    {"name": "E♭ MAJ_SEVEN", "inversion": 1, "dissonance_rank": Rank.Lowest},
    {"name": "E♭ MAJ_SEVEN", "inversion": 1, "dissonance_rank": Rank.Lowest},
    {"name": "A♮ MINOR_SEVEN", "inversion": 1, "dissonance_rank": Rank.Highest},
    {"name": "D♮ SEVEN", "inversion": 1, "dissonance_rank": Rank.Highest},
    {"name": "G♮ MAJ_SEVEN", "inversion": 1, "dissonance_rank": Rank.High},
    {"name": "B♭ SEVEN", "inversion": 1, "dissonance_rank": Rank.High},
    {"name": "E♭ MAJ_SEVEN", "inversion": 1, "dissonance_rank": Rank.Med},
    {"name": "F♯ SEVEN", "inversion": 1, "dissonance_rank": Rank.Med},
    {"name": "B♮ MAJ_SEVEN", "inversion": 1, "dissonance_rank": Rank.Low},
    {"name": "B♮ MAJ_SEVEN", "inversion": 1, "dissonance_rank": Rank.Low},
    {"name": "F♮ MINOR_SEVEN", "inversion": 1, "dissonance_rank": Rank.Med},
    {"name": "B♭ SEVEN", "inversion": 1, "dissonance_rank": Rank.Med},
    {"name": "E♭ MAJ_SEVEN", "inversion": 1, "dissonance_rank": Rank.Low},
    {"name": "E♭ MAJ_SEVEN", "inversion": 1, "dissonance_rank": Rank.Low},
    {"name": "A♮ MINOR_SEVEN", "inversion": 1, "dissonance_rank": Rank.Lowest},
    {"name": "D♮ MINOR_SEVEN", "inversion": 1, "dissonance_rank": Rank.Lowest},
    {"name": "G♮ MAJ_SEVEN", "inversion": 1, "dissonance_rank": Rank.Med},
    {"name": "G♮ MAJ_SEVEN", "inversion": 1, "dissonance_rank": Rank.Med},
    {"name": "C♯ MINOR_SEVEN", "inversion": 1, "dissonance_rank": Rank.High},
    {"name": "F♯ SEVEN", "inversion": 1, "dissonance_rank": Rank.High},
    {"name": "B♮ MAJ_SEVEN", "inversion": 1, "dissonance_rank": Rank.Highest},
    {"name": "B♮ MAJ_SEVEN", "inversion": 1, "dissonance_rank": Rank.Highest},
    {"name": "F♮ MINOR_SEVEN", "inversion": 1, "dissonance_rank": Rank.Med},
    {"name": "B♭ SEVEN", "inversion": 1, "dissonance_rank": Rank.Med},
    {"name": "E♭ MAJ_SEVEN", "inversion": 1, "dissonance_rank": Rank.Low},
    {"name": "E♭ MAJ_SEVEN", "inversion": 1, "dissonance_rank": Rank.Low},
    {"name": "C♯ MINOR_SEVEN", "inversion": 1, "dissonance_rank": Rank.Lowest},
    {"name": "F♯ SEVEN", "inversion": 1, "dissonance_rank": Rank.Lowest},
    # second repeat
    {"name": "B♮ MAJ_SEVEN", "inversion": 2, "dissonance_rank": Rank.Highest},
    {"name": "D♮ SEVEN", "inversion": 2, "dissonance_rank": Rank.Highest},
    {"name": "G♮ MAJ_SEVEN", "inversion": 2, "dissonance_rank": Rank.Highest},
    {"name": "B♭ SEVEN", "inversion": 2, "dissonance_rank": Rank.Highest},
    {"name": "E♭ MAJ_SEVEN", "inversion": 2, "dissonance_rank": Rank.High},
    {"name": "E♭ MAJ_SEVEN", "inversion": 2, "dissonance_rank": Rank.High},
    {"name": "A♮ MINOR_SEVEN", "inversion": 2, "dissonance_rank": Rank.High},
    {"name": "D♮ SEVEN", "inversion": 2, "dissonance_rank": Rank.High},
    {"name": "G♮ MAJ_SEVEN", "inversion": 2, "dissonance_rank": Rank.Med},
    {"name": "B♭ SEVEN", "inversion": 2, "dissonance_rank": Rank.Med},
    {"name": "E♭ MAJ_SEVEN", "inversion": 2, "dissonance_rank": Rank.Med},
    {"name": "F♯ SEVEN", "inversion": 2, "dissonance_rank": Rank.Med},
    {"name": "B♮ MAJ_SEVEN", "inversion": 2, "dissonance_rank": Rank.High},
    {"name": "B♮ MAJ_SEVEN", "inversion": 2, "dissonance_rank": Rank.High},
    {"name": "F♮ MINOR_SEVEN", "inversion": 2, "dissonance_rank": Rank.High},
    {"name": "B♭ SEVEN", "inversion": 2, "dissonance_rank": Rank.High},
    {"name": "E♭ MAJ_SEVEN", "inversion": 2, "dissonance_rank": Rank.Med},
    {"name": "E♭ MAJ_SEVEN", "inversion": 2, "dissonance_rank": Rank.Med},
    {"name": "A♮ MINOR_SEVEN", "inversion": 2, "dissonance_rank": Rank.Med},
    {"name": "D♮ MINOR_SEVEN", "inversion": 2, "dissonance_rank": Rank.Med},
    {"name": "G♮ MAJ_SEVEN", "inversion": 2, "dissonance_rank": Rank.Low},
    {"name": "G♮ MAJ_SEVEN", "inversion": 2, "dissonance_rank": Rank.Low},
    {"name": "C♯ MINOR_SEVEN", "inversion": 2, "dissonance_rank": Rank.Low},
    {"name": "F♯ SEVEN", "inversion": 2, "dissonance_rank": Rank.Low},
    {"name": "B♮ MAJ_SEVEN", "inversion": 2, "dissonance_rank": Rank.Med},
    {"name": "B♮ MAJ_SEVEN", "inversion": 2, "dissonance_rank": Rank.Med},
    {"name": "F♮ MINOR_SEVEN", "inversion": 2, "dissonance_rank": Rank.Low},
    {"name": "B♭ SEVEN", "inversion": 2, "dissonance_rank": Rank.Low},
    {"name": "E♭ MAJ_SEVEN", "inversion": 2, "dissonance_rank": Rank.Lowest},
    {"name": "E♭ MAJ_SEVEN", "inversion": 2, "dissonance_rank": Rank.Lowest},
    {"name": "C♯ MINOR_SEVEN", "inversion": 2, "dissonance_rank": Rank.Lowest},
    {"name": "F♯ SEVEN", "inversion": 2, "dissonance_rank": Rank.Lowest},
    # third repeat
    {"name": "B♮ MAJ_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "D♮ SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "G♮ MAJ_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "B♭ SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "E♭ MAJ_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "E♭ MAJ_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "A♮ MINOR_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "D♮ SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "G♮ MAJ_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "B♭ SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "E♭ MAJ_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "F♯ SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "B♮ MAJ_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "B♮ MAJ_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "F♮ MINOR_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "B♭ SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "E♭ MAJ_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "E♭ MAJ_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "A♮ MINOR_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "D♮ MINOR_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "G♮ MAJ_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "G♮ MAJ_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "C♯ MINOR_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "F♯ SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "B♮ MAJ_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "B♮ MAJ_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "F♮ MINOR_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "B♭ SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "E♭ MAJ_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "E♭ MAJ_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "C♯ MINOR_SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
    {"name": "F♯ SEVEN", "inversion": 3, "dissonance_rank": Rank.Highest},
]
