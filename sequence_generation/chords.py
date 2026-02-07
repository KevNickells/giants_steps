from sequence_generation.types import (
    Accidental,
    ChordInfo,
    ChordType,
    Notes,
)

CHORDS: list[ChordInfo] = [
    {
        "key": Notes.B,
        "accidental": Accidental.natural,
        "chord_type": ChordType.MAJ_SEVEN,
        "inversions": (
            (
                {"note": Notes.B, "accidental": Accidental.natural},
                {"note": Notes.D, "accidental": Accidental.sharp},
                {"note": Notes.F, "accidental": Accidental.sharp},
                {"note": Notes.A, "accidental": Accidental.sharp},
            ),
            (
                {"note": Notes.D, "accidental": Accidental.sharp},
                {"note": Notes.F, "accidental": Accidental.sharp},
                {"note": Notes.A, "accidental": Accidental.sharp},
                {"note": Notes.B, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.F, "accidental": Accidental.sharp},
                {"note": Notes.A, "accidental": Accidental.sharp},
                {"note": Notes.B, "accidental": Accidental.natural},
                {"note": Notes.D, "accidental": Accidental.sharp},
            ),
            (
                {"note": Notes.A, "accidental": Accidental.sharp},
                {"note": Notes.B, "accidental": Accidental.natural},
                {"note": Notes.D, "accidental": Accidental.sharp},
                {"note": Notes.F, "accidental": Accidental.sharp},
            ),
        ),
    },
    {
        "key": Notes.D,
        "accidental": Accidental.natural,
        "chord_type": ChordType.SEVEN,
        "inversions": (
            (
                {"note": Notes.D, "accidental": Accidental.natural},
                {"note": Notes.F, "accidental": Accidental.sharp},
                {"note": Notes.A, "accidental": Accidental.natural},
                {"note": Notes.C, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.F, "accidental": Accidental.sharp},
                {"note": Notes.A, "accidental": Accidental.natural},
                {"note": Notes.C, "accidental": Accidental.natural},
                {"note": Notes.D, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.A, "accidental": Accidental.natural},
                {"note": Notes.C, "accidental": Accidental.natural},
                {"note": Notes.D, "accidental": Accidental.natural},
                {"note": Notes.F, "accidental": Accidental.sharp},
            ),
            (
                {"note": Notes.C, "accidental": Accidental.natural},
                {"note": Notes.D, "accidental": Accidental.natural},
                {"note": Notes.F, "accidental": Accidental.sharp},
                {"note": Notes.A, "accidental": Accidental.natural},
            ),
        ),
    },
    {
        "key": Notes.G,
        "accidental": Accidental.natural,
        "chord_type": ChordType.MAJ_SEVEN,
        "inversions": (
            (
                {"note": Notes.G, "accidental": Accidental.natural},
                {"note": Notes.B, "accidental": Accidental.natural},
                {"note": Notes.D, "accidental": Accidental.natural},
                {"note": Notes.F, "accidental": Accidental.sharp},
            ),
            (
                {"note": Notes.B, "accidental": Accidental.natural},
                {"note": Notes.D, "accidental": Accidental.natural},
                {"note": Notes.F, "accidental": Accidental.sharp},
                {"note": Notes.G, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.D, "accidental": Accidental.natural},
                {"note": Notes.F, "accidental": Accidental.sharp},
                {"note": Notes.G, "accidental": Accidental.natural},
                {"note": Notes.B, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.F, "accidental": Accidental.sharp},
                {"note": Notes.G, "accidental": Accidental.natural},
                {"note": Notes.B, "accidental": Accidental.natural},
                {"note": Notes.D, "accidental": Accidental.natural},
            ),
        ),
    },
    {
        "key": Notes.B,
        "accidental": Accidental.flat,
        "chord_type": ChordType.SEVEN,
        "inversions": (
            (
                {"note": Notes.B, "accidental": Accidental.flat},
                {"note": Notes.D, "accidental": Accidental.natural},
                {"note": Notes.F, "accidental": Accidental.natural},
                {"note": Notes.A, "accidental": Accidental.flat},
            ),
            (
                {"note": Notes.D, "accidental": Accidental.natural},
                {"note": Notes.F, "accidental": Accidental.natural},
                {"note": Notes.A, "accidental": Accidental.flat},
                {"note": Notes.B, "accidental": Accidental.flat},
            ),
            (
                {"note": Notes.F, "accidental": Accidental.natural},
                {"note": Notes.A, "accidental": Accidental.flat},
                {"note": Notes.B, "accidental": Accidental.flat},
                {"note": Notes.D, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.A, "accidental": Accidental.flat},
                {"note": Notes.B, "accidental": Accidental.flat},
                {"note": Notes.D, "accidental": Accidental.natural},
                {"note": Notes.F, "accidental": Accidental.natural},
            ),
        ),
    },
    {
        "key": Notes.E,
        "accidental": Accidental.flat,
        "chord_type": ChordType.MAJ_SEVEN,
        "inversions": (
            (
                {"note": Notes.E, "accidental": Accidental.flat},
                {"note": Notes.G, "accidental": Accidental.natural},
                {"note": Notes.B, "accidental": Accidental.flat},
                {"note": Notes.D, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.G, "accidental": Accidental.natural},
                {"note": Notes.B, "accidental": Accidental.flat},
                {"note": Notes.D, "accidental": Accidental.natural},
                {"note": Notes.E, "accidental": Accidental.flat},
            ),
            (
                {"note": Notes.B, "accidental": Accidental.flat},
                {"note": Notes.D, "accidental": Accidental.natural},
                {"note": Notes.E, "accidental": Accidental.flat},
                {"note": Notes.G, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.D, "accidental": Accidental.natural},
                {"note": Notes.E, "accidental": Accidental.flat},
                {"note": Notes.G, "accidental": Accidental.natural},
                {"note": Notes.B, "accidental": Accidental.flat},
            ),
        ),
    },
    {
        "key": Notes.A,
        "accidental": Accidental.natural,
        "chord_type": ChordType.MINOR_SEVEN,
        "inversions": (
            (
                {"note": Notes.A, "accidental": Accidental.natural},
                {"note": Notes.C, "accidental": Accidental.natural},
                {"note": Notes.E, "accidental": Accidental.natural},
                {"note": Notes.G, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.C, "accidental": Accidental.natural},
                {"note": Notes.E, "accidental": Accidental.natural},
                {"note": Notes.G, "accidental": Accidental.natural},
                {"note": Notes.A, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.E, "accidental": Accidental.natural},
                {"note": Notes.G, "accidental": Accidental.natural},
                {"note": Notes.A, "accidental": Accidental.natural},
                {"note": Notes.C, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.G, "accidental": Accidental.natural},
                {"note": Notes.A, "accidental": Accidental.natural},
                {"note": Notes.C, "accidental": Accidental.natural},
                {"note": Notes.E, "accidental": Accidental.natural},
            ),
        ),
    },
    {
        "key": Notes.C,
        "accidental": Accidental.sharp,
        "chord_type": ChordType.MINOR_SEVEN,
        "inversions": (
            (
                {"note": Notes.C, "accidental": Accidental.sharp},
                {"note": Notes.E, "accidental": Accidental.natural},
                {"note": Notes.G, "accidental": Accidental.sharp},
                {"note": Notes.B, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.E, "accidental": Accidental.natural},
                {"note": Notes.G, "accidental": Accidental.sharp},
                {"note": Notes.B, "accidental": Accidental.natural},
                {"note": Notes.C, "accidental": Accidental.sharp},
            ),
            (
                {"note": Notes.G, "accidental": Accidental.sharp},
                {"note": Notes.B, "accidental": Accidental.natural},
                {"note": Notes.C, "accidental": Accidental.sharp},
                {"note": Notes.E, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.B, "accidental": Accidental.natural},
                {"note": Notes.C, "accidental": Accidental.sharp},
                {"note": Notes.E, "accidental": Accidental.natural},
                {"note": Notes.G, "accidental": Accidental.sharp},
            ),
        ),
    },
    {
        "key": Notes.D,
        "accidental": Accidental.natural,
        "chord_type": ChordType.MINOR_SEVEN,
        "inversions": (
            (
                {"note": Notes.D, "accidental": Accidental.natural},
                {"note": Notes.F, "accidental": Accidental.natural},
                {"note": Notes.A, "accidental": Accidental.natural},
                {"note": Notes.C, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.F, "accidental": Accidental.natural},
                {"note": Notes.A, "accidental": Accidental.natural},
                {"note": Notes.C, "accidental": Accidental.natural},
                {"note": Notes.D, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.A, "accidental": Accidental.natural},
                {"note": Notes.C, "accidental": Accidental.natural},
                {"note": Notes.D, "accidental": Accidental.natural},
                {"note": Notes.F, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.C, "accidental": Accidental.natural},
                {"note": Notes.D, "accidental": Accidental.natural},
                {"note": Notes.F, "accidental": Accidental.natural},
                {"note": Notes.A, "accidental": Accidental.natural},
            ),
        ),
    },
    {
        "key": Notes.F,
        "accidental": Accidental.sharp,
        "chord_type": ChordType.SEVEN,
        "inversions": (
            (
                {"note": Notes.F, "accidental": Accidental.sharp},
                {"note": Notes.A, "accidental": Accidental.sharp},
                {"note": Notes.C, "accidental": Accidental.sharp},
                {"note": Notes.E, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.A, "accidental": Accidental.sharp},
                {"note": Notes.C, "accidental": Accidental.sharp},
                {"note": Notes.E, "accidental": Accidental.natural},
                {"note": Notes.F, "accidental": Accidental.sharp},
            ),
            (
                {"note": Notes.C, "accidental": Accidental.sharp},
                {"note": Notes.E, "accidental": Accidental.natural},
                {"note": Notes.F, "accidental": Accidental.sharp},
                {"note": Notes.A, "accidental": Accidental.sharp},
            ),
            (
                {"note": Notes.E, "accidental": Accidental.natural},
                {"note": Notes.F, "accidental": Accidental.sharp},
                {"note": Notes.A, "accidental": Accidental.sharp},
                {"note": Notes.C, "accidental": Accidental.sharp},
            ),
        ),
    },
    {
        "key": Notes.F,
        "accidental": Accidental.natural,
        "chord_type": ChordType.SEVEN,
        "inversions": (
            (
                {"note": Notes.F, "accidental": Accidental.natural},
                {"note": Notes.A, "accidental": Accidental.natural},
                {"note": Notes.C, "accidental": Accidental.natural},
                {"note": Notes.E, "accidental": Accidental.flat},
            ),
            (
                {"note": Notes.A, "accidental": Accidental.flat},
                {"note": Notes.C, "accidental": Accidental.natural},
                {"note": Notes.E, "accidental": Accidental.flat},
                {"note": Notes.F, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.C, "accidental": Accidental.natural},
                {"note": Notes.E, "accidental": Accidental.flat},
                {"note": Notes.F, "accidental": Accidental.natural},
                {"note": Notes.A, "accidental": Accidental.flat},
            ),
            (
                {"note": Notes.E, "accidental": Accidental.flat},
                {"note": Notes.F, "accidental": Accidental.natural},
                {"note": Notes.A, "accidental": Accidental.flat},
                {"note": Notes.C, "accidental": Accidental.natural},
            ),
        ),
    },
    {
        "key": Notes.F,
        "accidental": Accidental.natural,
        "chord_type": ChordType.MINOR_SEVEN,
        "inversions": (
            (
                {"note": Notes.F, "accidental": Accidental.natural},
                {"note": Notes.A, "accidental": Accidental.flat},
                {"note": Notes.C, "accidental": Accidental.natural},
                {"note": Notes.E, "accidental": Accidental.flat},
            ),
            (
                {"note": Notes.A, "accidental": Accidental.flat},
                {"note": Notes.C, "accidental": Accidental.natural},
                {"note": Notes.E, "accidental": Accidental.flat},
                {"note": Notes.F, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.C, "accidental": Accidental.natural},
                {"note": Notes.E, "accidental": Accidental.flat},
                {"note": Notes.F, "accidental": Accidental.natural},
                {"note": Notes.A, "accidental": Accidental.flat},
            ),
            (
                {"note": Notes.E, "accidental": Accidental.flat},
                {"note": Notes.F, "accidental": Accidental.natural},
                {"note": Notes.A, "accidental": Accidental.flat},
                {"note": Notes.C, "accidental": Accidental.natural},
            ),
        ),
    },
    {
        "key": Notes.B,
        "accidental": Accidental.flat,
        "chord_type": ChordType.MAJ_SEVEN,
        "inversions": (
            (
                {"note": Notes.B, "accidental": Accidental.flat},
                {"note": Notes.D, "accidental": Accidental.natural},
                {"note": Notes.F, "accidental": Accidental.natural},
                {"note": Notes.A, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.D, "accidental": Accidental.natural},
                {"note": Notes.F, "accidental": Accidental.natural},
                {"note": Notes.A, "accidental": Accidental.natural},
                {"note": Notes.B, "accidental": Accidental.flat},
            ),
            (
                {"note": Notes.F, "accidental": Accidental.natural},
                {"note": Notes.A, "accidental": Accidental.natural},
                {"note": Notes.B, "accidental": Accidental.flat},
                {"note": Notes.D, "accidental": Accidental.natural},
            ),
            (
                {"note": Notes.A, "accidental": Accidental.natural},
                {"note": Notes.B, "accidental": Accidental.flat},
                {"note": Notes.D, "accidental": Accidental.natural},
                {"note": Notes.F, "accidental": Accidental.natural},
            ),
        ),
    },
]

CHORD_SEQUENCE = [
    (Notes.B, Accidental.natural, ChordType.MAJ_SEVEN),
    (Notes.D, Accidental.natural, ChordType.SEVEN),
    (Notes.G, Accidental.natural, ChordType.MAJ_SEVEN),
    (Notes.B, Accidental.flat, ChordType.SEVEN),
    (Notes.E, Accidental.flat, ChordType.MAJ_SEVEN),
    (Notes.E, Accidental.flat, ChordType.MAJ_SEVEN),
    (Notes.A, Accidental.natural, ChordType.MINOR_SEVEN),
    (Notes.D, Accidental.natural, ChordType.SEVEN),
    (Notes.G, Accidental.natural, ChordType.MAJ_SEVEN),
    (Notes.B, Accidental.flat, ChordType.SEVEN),
    (Notes.E, Accidental.flat, ChordType.MAJ_SEVEN),
    (Notes.F, Accidental.sharp, ChordType.SEVEN),
    (Notes.B, Accidental.natural, ChordType.MAJ_SEVEN),
    (Notes.B, Accidental.natural, ChordType.MAJ_SEVEN),
    (Notes.F, Accidental.natural, ChordType.MINOR_SEVEN),
    (Notes.B, Accidental.flat, ChordType.SEVEN),
    (Notes.E, Accidental.flat, ChordType.MAJ_SEVEN),
    (Notes.E, Accidental.flat, ChordType.MAJ_SEVEN),
    (Notes.A, Accidental.natural, ChordType.MINOR_SEVEN),
    (Notes.D, Accidental.natural, ChordType.MINOR_SEVEN),
    (Notes.G, Accidental.natural, ChordType.MAJ_SEVEN),
    (Notes.G, Accidental.natural, ChordType.MAJ_SEVEN),
    (Notes.C, Accidental.sharp, ChordType.MINOR_SEVEN),
    (Notes.F, Accidental.sharp, ChordType.SEVEN),
    (Notes.B, Accidental.natural, ChordType.MAJ_SEVEN),
    (Notes.B, Accidental.natural, ChordType.MAJ_SEVEN),
    (Notes.F, Accidental.natural, ChordType.MINOR_SEVEN),
    (Notes.B, Accidental.flat, ChordType.SEVEN),
    (Notes.E, Accidental.flat, ChordType.MAJ_SEVEN),
    (Notes.E, Accidental.flat, ChordType.MAJ_SEVEN),
    (Notes.C, Accidental.sharp, ChordType.MINOR_SEVEN),
    (Notes.F, Accidental.sharp, ChordType.SEVEN),
]


def chord_details():
    full_names = []
    for chord in CHORD_SEQUENCE:
        key, accidental, chord_type = chord

        chord_name = next(
            (
                chord_name
                for chord_name in CHORDS
                if chord_name["key"] == key
                and chord_name["accidental"] == accidental
                and chord_name["chord_type"] == chord_type
            ),
            None,
        )
        if chord_name:
            full_names.append(chord_name)
        else:
            print(f"Chord not found: {key}{accidental}{chord_type}")

    return full_names


details = chord_details()
