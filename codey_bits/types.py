from enum import Enum
from typing import Dict, Literal, Tuple, TypedDict


class Accidental(Enum):
    natural = "♮"
    sharp = "♯"
    flat = "♭"


reference_tones: Dict[str, float] = {
    "A♮": 440,
    "B♭": 466.16,
    "B♮": 493.88,
    "C♯": 554.37,
    "D♮": 587.33,
    "E♭": 622.25,
    "F♮": 698.46,
    "F♯": 739.99,
    "G♮": 783.99,
}


class Notes(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"


class ChordInterval(TypedDict):
    interval: Literal[1, 3, 5, 7]
    accidental: Accidental


class ChordType(Enum):
    MAJ_SEVEN = [
        ChordInterval(interval=1, accidental=Accidental.natural),
        ChordInterval(interval=3, accidental=Accidental.natural),
        ChordInterval(interval=5, accidental=Accidental.natural),
        ChordInterval(interval=7, accidental=Accidental.natural),
    ]
    SEVEN = [
        ChordInterval(interval=1, accidental=Accidental.natural),
        ChordInterval(interval=3, accidental=Accidental.natural),
        ChordInterval(interval=5, accidental=Accidental.natural),
        ChordInterval(interval=7, accidental=Accidental.flat),
    ]
    MINOR_SEVEN = [
        ChordInterval(interval=1, accidental=Accidental.natural),
        ChordInterval(interval=3, accidental=Accidental.flat),
        ChordInterval(interval=5, accidental=Accidental.natural),
        ChordInterval(interval=7, accidental=Accidental.flat),
    ]


Inversion = Literal[0, 1, 2, 3]


class ChordNote(TypedDict):
    note: Notes
    accidental: Accidental


Chord = Tuple[ChordNote, ChordNote, ChordNote, ChordNote]


class ChordInfo(TypedDict):
    key: Notes
    accidental: Accidental
    chord_type: ChordType
    inversions: Tuple[
        Tuple[ChordNote, ChordNote, ChordNote, ChordNote],
        Tuple[ChordNote, ChordNote, ChordNote, ChordNote],
        Tuple[ChordNote, ChordNote, ChordNote, ChordNote],
        Tuple[ChordNote, ChordNote, ChordNote, ChordNote],
    ]


def inversion_intervals(inversion: Inversion):
    return [n % 4 for n in range(inversion, inversion + 4)]
