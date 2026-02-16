import json
from pprint import pprint

from sequence_generation.final_intervals import (
    preferred_fifths,
    preferred_major_sevenths,
    preferred_minor_sevenths,
    preferred_minor_thirds,
    preferred_natural_thirds,
)

all_ratios = (
    preferred_minor_thirds
    + preferred_natural_thirds
    + preferred_fifths
    + preferred_minor_sevenths
    + preferred_major_sevenths
)


with open("inv_1.json", "r") as f:
    inversion_1 = json.load(f)

with open("with_inversions.json", "r") as f:
    with_inversions = json.load(f)

for index, chord in enumerate(inversion_1):
    notes = chord["notes"]
    root = notes[0]
    intervals = with_inversions[index + (len(inversion_1) - 1)]["intervals"]

    third, fifth, seventh = intervals.split("|")
    third_ratio = next(ratio for ratio in all_ratios if ratio["name"] == third.strip())
    fifth_ratio = next(ratio for ratio in all_ratios if ratio["name"] == fifth.strip())
    seventh_ratio = next(
        ratio for ratio in all_ratios if ratio["name"] == seventh.strip()
    )
    if not third_ratio:
        print("panic")
    if not fifth_ratio:
        print("panic")
    if not seventh_ratio:
        print("panic")
#
# for index, detail in enumerate(with_inversions):
#    intervals = detail["intervals"]
#
#    third, fifth, seventh = intervals.split("|")
#
#    third_ratio = next(ratio for ratio in all_ratios if ratio["name"] == third.strip())
#    fifth_ratio = next(ratio for ratio in all_ratios if ratio["name"] == fifth.strip())
#    seventh_ratio = next(
#        ratio for ratio in all_ratios if ratio["name"] == seventh.strip()
#    )


# pprint(inversion_1[0])


# with open("inv_1.json", "w") as f:
#    json.dump(inversion_1, f, indent=2)
"""
{'chord': 'B♮ MAJ_SEVEN',
 'inversion': 0,
 'notes': [{'frequency': 246.9417,
            'image': 'B_nat_low.png',
            'note': 'B♮',
            'scientific_name': 'B3'},
           {'frequency': 300.6246782608696,
            'image': 'D_sharp_med.png',
            'note': 'D♯',
            'scientific_name': 'D♯4'},
           {'frequency': 370.41255,
            'image': 'F_sharp_med.png',
            'note': 'F♯',
            'scientific_name': 'F♯4'},
           {'frequency': 470.3651428571428,
            'image': 'A_sharp_med.png',
            'note': 'A♯',
            'scientific_name': 'A♯4'}]}
            """

nothing = {}
pprint(nothing)
