import json

for thing in [
    "first_notes.json",
    "second_notes.json",
    "third_notes.json",
    "fourth_notes.json",
]:
    with open(thing, "r", encoding="utf-8") as f:
        out = []
        data = json.load(f)
        for notes in data:
            new = {}
            frequency = notes["frequency"] / 2
            image = list(notes["image"])
            if len(image) == 6:
                image[1] = str(int(image[1]) - 1)

            if len(image) == 7:
                image[2] = str(int(image[2]) - 1)

            new["full_chord"] = notes["full_chord"]
            new["frequency"] = frequency
            new["image"] = "".join(image)
            new["interval"] = notes["interval"]

            out.append(new)

        with open(f"_{thing}", "w") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
