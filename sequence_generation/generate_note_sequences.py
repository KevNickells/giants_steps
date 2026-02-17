import json

with open("inv_1.json", "r") as f:
    inversion_1 = json.load(f)

first_note = []
second_note = []
third_note = []
fourth_note = []

for chord in inversion_1:
    chord_name = chord["chord"]
    notes = chord["notes"]
    first, second, third, fourth = notes

    first_note.append(
        {
            "full_chord": chord_name,
            "frequency": first["frequency"],
            "image": f"{first["scientific_name"]}.png",
            "interval": "first",
        }
    )

    second_note.append(
        {
            "full_chord": chord_name,
            "frequency": second["frequency"],
            "image": f"{second["scientific_name"]}.png",
            "interval": "third",
        }
    )

    third_note.append(
        {
            "full_chord": chord_name,
            "frequency": third["frequency"],
            "image": f"{third["scientific_name"]}.png",
            "interval": "fifth",
        }
    )

    fourth_note.append(
        {
            "full_chord": chord_name,
            "frequency": fourth["frequency"],
            "image": f"{fourth["scientific_name"]}.png",
            "interval": "seventh",
        }
    )

with open("first_notes.json", "w") as f:
    json.dump(first_note, f, ensure_ascii=False, indent=2)

with open("second_notes.json", "w") as f:
    json.dump(second_note, f, ensure_ascii=False, indent=2)
with open("third_notes.json", "w") as f:
    json.dump(third_note, f, ensure_ascii=False, indent=2)
with open("fourth_notes.json", "w") as f:
    json.dump(fourth_note, f, ensure_ascii=False, indent=2)
