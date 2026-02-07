from enum import Enum
from pprint import pprint
from random import choices
from typing import List

import numpy as np

from codey_bits.maj_7_final_list import maj_7_final_list as maj7
from codey_bits.min_7_final_list import min_7_final_list as min7
from codey_bits.seven_final_list import seven_final_list as dom7
from codey_bits.types import reference_tones


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


final_sequence: List = [
    # initial
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Lowest, maj7),
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "D♮ SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Lowest, dom7),
        "root_freq": reference_tones["D♮"],
    },
    {
        "name": "G♮ MAJ_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, maj7)[3],
        "root_freq": reference_tones["G♮"],
    },
    {
        "name": "B♭ SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, dom7)[5],
        "root_freq": reference_tones["B♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Lowest, maj7),
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Lowest, maj7),
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "A♮ MINOR_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Lowest, min7),
        "root_freq": reference_tones["A♮"],
    },
    {
        "name": "D♮ SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, dom7)[1],
        "root_freq": reference_tones["D♮"],
    },
    {
        "name": "G♮ MAJ_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, maj7)[4],
        "root_freq": reference_tones["G♮"],
    },
    {
        "name": "B♭ SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, dom7)[1],
        "root_freq": reference_tones["B♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, maj7)[1],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "F♯ SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Lowest, dom7),
        "root_freq": reference_tones["F♯"],
    },
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, maj7)[1],
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, maj7)[1],
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "F♮ MINOR_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, min7)[1],
        "root_freq": reference_tones["F♮"],
    },
    {
        "name": "B♭ SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, dom7)[2],
        "root_freq": reference_tones["B♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, maj7)[2],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, maj7)[2],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "A♮ MINOR_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, min7)[1],
        "root_freq": reference_tones["A♮"],
    },
    {
        "name": "D♮ MINOR_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Lowest, min7),
        "root_freq": reference_tones["D♮"],
    },
    {
        "name": "G♮ MAJ_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Med, maj7)[0],
        "root_freq": reference_tones["G♮"],
    },
    {
        "name": "G♮ MAJ_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Med, maj7)[0],
        "root_freq": reference_tones["G♮"],
    },
    {
        "name": "C♯ MINOR_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Lowest, min7),
        "root_freq": reference_tones["C♯"],
    },
    {
        "name": "F♯ SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, dom7)[2],
        "root_freq": reference_tones["F♯"],
    },
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, maj7)[2],
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, maj7)[2],
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "F♮ MINOR_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, min7)[2],
        "root_freq": reference_tones["F♮"],
    },
    {
        "name": "B♭ SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, dom7)[3],
        "root_freq": reference_tones["B♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, maj7)[3],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, maj7)[3],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "C♯ MINOR_SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, min7)[1],
        "root_freq": reference_tones["C♯"],
    },
    {
        "name": "F♯ SEVEN",
        "inversion": 0,
        "chord_details": get_rank(Rank.Low, dom7)[1],
        "root_freq": reference_tones["F♯"],
    },
    # first repeat
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Low, maj7)[-1],
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "D♮ SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Low, dom7)[2],
        "root_freq": reference_tones["D♮"],
    },
    {
        "name": "G♮ MAJ_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Med, maj7)[2],
        "root_freq": reference_tones["G♮"],
    },
    {
        "name": "B♭ SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Med, dom7)[0],
        "root_freq": reference_tones["B♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Low, maj7)[4],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Low, maj7)[4],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "A♮ MINOR_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Highest, min7),
        "root_freq": reference_tones["A♮"],
    },
    {
        "name": "D♮ SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.High, dom7)[0],
        "root_freq": reference_tones["D♮"],
    },
    {
        "name": "G♮ MAJ_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.High, maj7)[0],
        "root_freq": reference_tones["G♮"],
    },
    {
        "name": "B♭ SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.High, dom7)[0],
        "root_freq": reference_tones["B♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Med, maj7)[1],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "F♯ SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Med, dom7)[-1],
        "root_freq": reference_tones["F♯"],
    },
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Med, maj7)[0],
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Med, maj7)[0],
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "F♮ MINOR_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Med, min7)[0],
        "root_freq": reference_tones["F♮"],
    },
    {
        "name": "B♭ SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Med, dom7)[2],
        "root_freq": reference_tones["B♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Med, maj7)[2],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Med, maj7)[2],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "A♮ MINOR_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Low, min7)[2],
        "root_freq": reference_tones["A♮"],
    },
    {
        "name": "D♮ MINOR_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Lowest, min7),
        "root_freq": reference_tones["D♮"],
    },
    {
        "name": "G♮ MAJ_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Med, maj7)[4],
        "root_freq": reference_tones["G♮"],
    },
    {
        "name": "G♮ MAJ_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Med, maj7)[5],
        "root_freq": reference_tones["G♮"],
    },
    {
        "name": "C♯ MINOR_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.High, min7)[0],
        "root_freq": reference_tones["C♯"],
    },
    {
        "name": "F♯ SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.High, dom7)[0],
        "root_freq": reference_tones["F♯"],
    },
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Highest, maj7),
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Highest, maj7),
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "F♮ MINOR_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Med, min7)[-1],
        "root_freq": reference_tones["F♮"],
    },
    {
        "name": "B♭ SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Med, dom7)[3],
        "root_freq": reference_tones["B♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Med, maj7)[3],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Med, maj7)[3],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "C♯ MINOR_SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Lowest, min7),
        "root_freq": reference_tones["C♯"],
    },
    {
        "name": "F♯ SEVEN",
        "inversion": 1,
        "chord_details": get_rank(Rank.Low, dom7)[-1],
        "root_freq": reference_tones["F♯"],
    },
    # second repeat
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.Highest, maj7),
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "D♮ SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.High, dom7)[-2],
        "root_freq": reference_tones["D♮"],
    },
    {
        "name": "G♮ MAJ_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.Med, maj7)[6],
        "root_freq": reference_tones["G♮"],
    },
    {
        "name": "B♭ SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.High, dom7)[4],
        "root_freq": reference_tones["B♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.High, maj7)[0],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.High, maj7)[0],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "A♮ MINOR_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.High, min7)[-2],
        "root_freq": reference_tones["A♮"],
    },
    {
        "name": "D♮ SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.High, dom7)[-3],
        "root_freq": reference_tones["D♮"],
    },
    {
        "name": "G♮ MAJ_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.Med, maj7)[6],
        "root_freq": reference_tones["G♮"],
    },
    {
        "name": "B♭ SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.Med, dom7)[5],
        "root_freq": reference_tones["B♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.High, maj7)[1],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "F♯ SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.Med, dom7)[-2],
        "root_freq": reference_tones["F♯"],
    },
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.High, maj7)[0],
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.High, maj7)[0],
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "F♮ MINOR_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.High, min7)[0],
        "root_freq": reference_tones["F♮"],
    },
    {
        "name": "B♭ SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.High, dom7)[2],
        "root_freq": reference_tones["B♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.High, maj7)[2],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.High, maj7)[2],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "A♮ MINOR_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.Med, min7)[-2],
        "root_freq": reference_tones["A♮"],
    },
    {
        "name": "D♮ MINOR_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.Med, min7)[-2],
        "root_freq": reference_tones["D♮"],
    },
    {
        "name": "G♮ MAJ_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.Low, maj7)[-1],
        "root_freq": reference_tones["G♮"],
    },
    {
        "name": "G♮ MAJ_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.Low, maj7)[-1],
        "root_freq": reference_tones["G♮"],
    },
    {
        "name": "C♯ MINOR_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.Low, min7)[-2],
        "root_freq": reference_tones["C♯"],
    },
    {
        "name": "F♯ SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.Low, dom7)[-2],
        "root_freq": reference_tones["F♯"],
    },
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.Med, maj7)[0],
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.Med, maj7)[0],
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "F♮ MINOR_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.Low, min7)[-1],
        "root_freq": reference_tones["F♮"],
    },
    {
        "name": "B♭ SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.Low, dom7)[5],
        "root_freq": reference_tones["B♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.High, maj7)[3],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.High, maj7)[3],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "C♯ MINOR_SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.Lowest, min7),
        "root_freq": reference_tones["C♯"],
    },
    {
        "name": "F♯ SEVEN",
        "inversion": 2,
        "chord_details": get_rank(Rank.Med, dom7)[-1],
        "root_freq": reference_tones["F♯"],
    },
    # third repeat
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, maj7),
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "D♮ SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.High, dom7)[-4],
        "root_freq": reference_tones["D♮"],
    },
    {
        "name": "G♮ MAJ_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, maj7),
        "root_freq": reference_tones["G♮"],
    },
    {
        "name": "B♭ SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, dom7),
        "root_freq": reference_tones["B♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, maj7),
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, maj7),
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "A♮ MINOR_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.High, min7)[-1],
        "root_freq": reference_tones["A♮"],
    },
    {
        "name": "D♮ SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, dom7),
        "root_freq": reference_tones["D♮"],
    },
    {
        "name": "G♮ MAJ_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, maj7),
        "root_freq": reference_tones["G♮"],
    },
    {
        "name": "B♭ SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, dom7),
        "root_freq": reference_tones["B♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.High, maj7)[4],
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "F♯ SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.High, dom7)[-2],
        "root_freq": reference_tones["F♯"],
    },
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, maj7),
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, maj7),
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "F♮ MINOR_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, min7),
        "root_freq": reference_tones["F♮"],
    },
    {
        "name": "B♭ SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.High, dom7)[-3],
        "root_freq": reference_tones["B♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, maj7),
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, maj7),
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "A♮ MINOR_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.High, min7)[-2],
        "root_freq": reference_tones["A♮"],
    },
    {
        "name": "D♮ MINOR_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, min7),
        "root_freq": reference_tones["D♮"],
    },
    {
        "name": "G♮ MAJ_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, maj7),
        "root_freq": reference_tones["G♮"],
    },
    {
        "name": "G♮ MAJ_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, maj7),
        "root_freq": reference_tones["G♮"],
    },
    {
        "name": "C♯ MINOR_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, min7),
        "root_freq": reference_tones["C♯"],
    },
    {
        "name": "F♯ SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.High, dom7)[-1],
        "root_freq": reference_tones["F♯"],
    },
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, maj7),
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "B♮ MAJ_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, maj7),
        "root_freq": reference_tones["B♮"],
    },
    {
        "name": "F♮ MINOR_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, min7),
        "root_freq": reference_tones["F♮"],
    },
    {
        "name": "B♭ SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.High, dom7)[4],
        "root_freq": reference_tones["B♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, maj7),
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "E♭ MAJ_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, maj7),
        "root_freq": reference_tones["E♭"],
    },
    {
        "name": "C♯ MINOR_SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, min7),
        "root_freq": reference_tones["C♯"],
    },
    {
        "name": "F♯ SEVEN",
        "inversion": 3,
        "chord_details": get_rank(Rank.Highest, dom7),
        "root_freq": reference_tones["F♯"],
    },
]

seen = []
duplicates = []

for indx, seq in enumerate(final_sequence):
    if str(seq) in seen:
        if str(seq) != str(final_sequence[indx - 1]):
            duplicates.append((str(seq)))
    else:
        seen.append(str(seq))

list_again = []


again = []

chord_details = [str(x["chord_details"]) for x in final_sequence]

unused = []
for chord in maj7 + min7 + dom7:
    if str(chord) not in chord_details:
        unused.append(chord)

for seq in final_sequence:
    if str(seq) in duplicates:
        seq["chord_details"] = choices(unused)

    list_again.append(seq)

# pprint(list_again)


duplicates2 = []
seen2 = []

for indx, seq in enumerate(list_again):
    if str(seq) in seen2:
        if str(seq) != str(list_again[indx - 1]):
            duplicates2.append((str(seq)))
    else:
        seen2.append(str(seq))

if len(duplicates2) == 0:
    print("asdf")
    pprint(list_again)
