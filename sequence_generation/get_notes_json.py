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

with open("inv_2.json", "r") as f:
    inversion_2 = json.load(f)

with open("with_inversions.json", "r") as f:
    with_inversions = json.load(f)


next_thing = []


def get_ratios(intervals, root_frequency):
    third, fifth, seventh = intervals.split("|")
    third_ratio = next(ratio for ratio in all_ratios if ratio["name"] == third.strip())
    fifth_ratio = next(ratio for ratio in all_ratios if ratio["name"] == fifth.strip())
    seventh_ratio = next(
        ratio for ratio in all_ratios if ratio["name"] == seventh.strip()
    )
    third_frequency = root_frequency * third_ratio["ratio"]
    fifth_frequency = root_frequency * fifth_ratio["ratio"]
    seventh_frequency = root_frequency * seventh_ratio["ratio"]

    return third_frequency, fifth_frequency, seventh_frequency


for index, chord in enumerate(inversion_2):
    notes = chord["notes"]
    root_frequency = notes[3]["frequency"] / 2
    intervals = with_inversions[index + (len(inversion_2) - 1)]["intervals"]

    third, fifth, seventh = get_ratios(intervals, root_frequency)

    notes[0]["frequency"] = seventh
    notes[1]["frequency"] = root_frequency * 2
    notes[2]["frequency"] = third * 2
    notes[3]["frequency"] = fifth * 2

    # chord["notes"] = [notes[2], notes[3], notes[0], notes[1]]

    chord["inversion"] = 3

    next_thing.append(chord)

"""
Still need to go over this
I think in actual fact it works like
repeat inv 1 each time so the root freq stays the same; everything except the seven will be doubled
"""
# pprint(inversion_1[0])

with open("inv_4.json", "w") as f:
    json.dump(next_thing, f, indent=2)

nothing = {}
pprint(nothing)
