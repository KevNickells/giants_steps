from typing import List

from sequence_generation.intervals import Interval

preferred_minor_thirds: List[Interval] = [
    {"ratio": 45 / 38, "name": "Eratosthenes' minor third"},
    {"ratio": 6 / 5, "name": "just minor third"},
    {"ratio": 175 / 144, "name": "keemic minor third"},
]

preferred_natural_thirds: List[Interval] = [
    {"ratio": 28 / 23, "name": "vicesimotertial neutral third"},  # ooh yeah
    {"ratio": 71 / 57, "name": "witchcraft major third"},  # fitter
    {
        "ratio": 161 / 128,
        "name": "just/Pythagorean major third meantone",  # darker
    },
    {"ratio": 80 / 63, "name": "5/7-kleismic major third"},  # frdige
]


preferred_fifths: List[Interval] = [
    {"ratio": 25 / 17, "name": "vengeance subfifth"},
    {"ratio": 323 / 216, "name": "undevicesimal meantone fifth"},
    {"ratio": 16384 / 10935, "name": "Kirnberger's fifth"},
    {
        "ratio": 3 / 2,
        "name": "just perfect fifth",
    },
    {"ratio": 121 / 80, "name": "wide biyatismic fifth"},
    {
        "ratio": 38 / 25,
        "name": "undevicesimal acute fifth",
    },
]

preferred_minor_sevenths: List[Interval] = [
    {
        "ratio": 7 / 4,
        "name": "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    },  # ooh yes yes
    {"ratio": 71 / 40, "name": "harmonic/just minor seventh meantone"},  # woof
    {
        "ratio": 57 / 32,
        "name": "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    },  # bit of dirt
]

preferred_major_sevenths: List[Interval] = [
    {"ratio": 11 / 6, "name": "undecimal neutral seventh, 21/4-tone"},  # hnnng hnng
    {
        "ratio": 36 / 19,
        "name": "undevicesimal major seventh, Boethius' major seventh",
    },  # naughty
    {"ratio": 40 / 21, "name": "septimal acute major seventh"},  # ear damage YES
]
