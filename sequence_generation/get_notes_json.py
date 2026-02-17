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

    return (
        (third, third_frequency),
        (fifth, fifth_frequency),
        (seventh, seventh_frequency),
    )


def iterate_name(name):
    arr = list(name)

    if len(arr) == 3:
        arr[2] = str(int(arr[2]) + 1)
    else:
        arr[1] = str(int(arr[1]) + 1)

    return "".join(arr)


for index, chord in enumerate(inversion_1):
    notes = chord["notes"]

    root_frequency = notes[0]["frequency"]

    length = len(inversion_1) - 1

    intervals = with_inversions[index + length]["intervals"]

    third, fifth, seventh = get_ratios(intervals, root_frequency)

    notes[0]["frequency"] = root_frequency * 2
    notes[0]["scientific_name"] = iterate_name(notes[0]["scientific_name"])

    notes[1]["frequency"] = third[1] * 2
    notes[1]["interval name"] = third[0]
    notes[1]["scientific_name"] = iterate_name(notes[1]["scientific_name"])

    notes[2]["frequency"] = fifth[1] * 2
    notes[2]["interval name"] = fifth[0]
    notes[2]["scientific_name"] = iterate_name(notes[2]["scientific_name"])

    notes[3]["frequency"] = seventh[1]
    notes[3]["interval name"] = seventh[0]

    chord["notes"] = [notes[3], notes[0], notes[1], notes[2]]

    if index == 0:
        print(root_frequency)
        print(notes[0])

    chord["inversion"] = 3

    next_thing.append(chord)

# pprint(inversion_1[0])

with open("inv_4.json", "w") as f:
    json.dump(next_thing, f, ensure_ascii=False, indent=2)
#
# with open("inv_1.json", "r", encoding="utf-8") as f:
#    data = json.load(f)
#
# with open("inv_1.json", "w", encoding="utf-8") as f:
#    json.dump(data, f, ensure_ascii=False, indent=2)

nothing = {}
pprint(nothing)
