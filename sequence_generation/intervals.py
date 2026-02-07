from typing import List, TypedDict


class Interval(TypedDict):
    name: str
    ratio: float


all_minor_thirds: List[Interval] = [
    {
        "ratio": 20 / 17,
        "name": "septendecimal augmented second, septendecimal minor third, diatismic minor third",
    },
    {"ratio": 13 / 11, "name": "tridecimal minor third"},
    {"ratio": 45 / 38, "name": "Eratosthenes' minor third"},
    {
        "ratio": 32 / 27,
        "name": "Pythagorean minor third",
    },
    {"ratio": 19 / 16, "name": "otonal minor third"},
    {"ratio": 289 / 243, "name": "semitonismic quasi-tempered minor third"},
    {"ratio": 25 / 21, "name": "quasi-tempered minor third"},
    {"ratio": 61 / 51, "name": "myna third"},
    {"ratio": 6 / 5, "name": "just minor third"},
    {"ratio": 77 / 64, "name": "keenanismic minor third"},
    {
        "ratio": 135 / 112,
        "name": "arge septimal minor third, marvelous minor third",
    },
    {"ratio": 35 / 29, "name": "doublewide minor third"},
    {"ratio": 23 / 19, "name": "vicesimotertial supraminor third"},
    {"ratio": 17 / 14, "name": "septendecimal supraminor third"},
    {"ratio": 175 / 144, "name": "keemic minor third"},
    {"ratio": 73 / 60, "name": "amity supraminor third"},
]

all_natural_thirds: List[Interval] = [
    {"ratio": 28 / 23, "name": "vicesimotertial neutral third"},  # ooh
    {"ratio": 39 / 32, "name": "lesser tridecimal neutral third"},
    {"ratio": 128 / 105, "name": "quasi-tempered 2/7-octave"},
    {"ratio": 625 / 512, "name": "5-limit neutral third"},  # a bit savage
    {"ratio": 11 / 9, "name": "undecimal neutral third"},
    {"ratio": 60 / 49, "name": "smaller septimal neutral third, (purple 3rd)"},  # ok
    {
        "ratio": 49 / 40,
        "name": "larger septimal neutral third, (purple 3rd)",
    },  # maybe better
    {"ratio": 27 / 22, "name": "rastmic neutral third"},  # dirt
    {
        "ratio": 16 / 13,
        "name": "greater tridecimal neutral third",  # dirtier
    },
    {"ratio": 21 / 17, "name": "septendecimal submajor third"},
    {"ratio": 26 / 21, "name": "tridecimal submajor third"},
    {"ratio": 51 / 41, "name": "mystery unnamed lad"},
    {"ratio": 56 / 45, "name": "narrow perde segah, marvelous major third"},  # fit
    {"ratio": 71 / 57, "name": "witchcraft major third"},  # fitter
    {"ratio": 76 / 61, "name": "magic major third"},
    {
        "ratio": 96 / 77,
        "name": "undecimal perde segah, keenanismic major third",
    },  # bright
    {
        "ratio": 5 / 4,
        "name": "classic major third, just major third",  # cute
    },
    {
        "ratio": 161 / 128,
        "name": "just/Pythagorean major third meantone",  # darker
    },
    {"ratio": 34 / 27, "name": "septendecimal quasi-tempered major third"},
    {"ratio": 63 / 50, "name": "quasi-tempered major third"},
    {"ratio": 24 / 19, "name": "Boethius' major third"},  # depthy
    {"ratio": 81 / 64, "name": "Pythagorean major third"},  # rough but nice
    {"ratio": 19 / 15, "name": "Eratosthenes' major third"},
    {"ratio": 33 / 26, "name": "tridecimal major third"},
    {"ratio": 80 / 63, "name": "5/7-kleismic major third"},  # frdige
    {
        "ratio": 14 / 11,
        "name": "undecimal major third, undecimal diminished fourth",
    },  # hot
]

all_fifths: List[Interval] = [
    {
        "ratio": 16 / 11,
        "name": "sub-fifth, paraminor fifth",
    },  # nice
    {"ratio": 35 / 24, "name": "septimal sub-fifth"},
    {"ratio": 19 / 13, "name": "undevicesimal sub-fifth"},  # ok
    {"ratio": 22 / 15, "name": "semidiminished fifth"},
    {"ratio": 72 / 49, "name": "septimal catafifth"},
    {"ratio": 25 / 17, "name": "vengeance subfifth"},  # yea
    {"ratio": 81 / 55, "name": "undecimal catafifth"},  # filthy
    {"ratio": 28 / 19, "name": "hendrix fifth"},
    {"ratio": 34 / 23, "name": "vicesimotertial grave fifth"},
    {"ratio": 262144 / 177147, "name": "Pythagorean wolf fifth"},  # heavy
    {"ratio": 40 / 27, "name": "grave fifth"},
    {"ratio": 95 / 64, "name": "undevicesimal harmonic fifth"},  # dirty
    {"ratio": 52 / 35, "name": "animist fifth"},  # big
    {"ratio": 180 / 121, "name": "narrow biyatismic fifth"},
    {"ratio": 112 / 75, "name": "marvelous fifth"},  # cheerful
    {"ratio": 121 / 81, "name": "Alpharabian narrow fifth"},
    {"ratio": 323 / 216, "name": "undevicesimal meantone fifth"},  # bright and dense
    {"ratio": 256 / 171, "name": "undevicesimal subharmonic fifth"},
    {"ratio": 16384 / 10935, "name": "Kirnberger's fifth"},  # rotating
    {
        "ratio": 3 / 2,
        "name": "just perfect fifth",  # great
    },
    {"ratio": 182 / 121, "name": "tridecimal gentle fifth"},
    {"ratio": 176 / 117, "name": "minthmic fifth"},
    {"ratio": 128 / 85, "name": "archagall fifth"},  # cute
    {"ratio": 121 / 80, "name": "wide biyatismic fifth"},  # ooh yeah
    {"ratio": 50 / 33, "name": "ptolemismic fifth"},
    {"ratio": 97 / 64, "name": "nonacesimoseptimal harmonic fifth"},
    {
        "ratio": 144 / 95,
        "name": "undevicesimal quasi-tempered 3/5-octave",  # something nastythere
    },
    {
        "ratio": 38 / 25,
        "name": "undevicesimal acute fifth",  # a bit evil
    },
    {"ratio": 32 / 21, "name": "super-fifth, wide fifth"},  # niiiice
    {"ratio": 26 / 17, "name": "septendecimal super-fifth"},
    {"ratio": 49 / 32, "name": "superduper fifth"},
]


minor_seventh: List[Interval] = [
    {
        "ratio": 7 / 4,
        "name": "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    },  # ooh
    {
        "ratio": 225 / 128,
        "name": "marvel five-limit harmonic seventh, octave-reduced 225th harmonic ([-7, 2, 2⟩)",
    },
    {
        "ratio": 44 / 25,
        "name": "ptolemismic minor seventh, undecimal grave minor seventh",
    },
    {"ratio": 30 / 17, "name": "septendecimal minor seventh"},  # brightish
    {"ratio": 23 / 13, "name": "vicesimotertial minor seventh"},
    {"ratio": 71 / 40, "name": "harmonic/just minor seventh meantone"},  # woof
    {
        "ratio": 16 / 9,
        "name": "Pythagorean minor seventh, small minor seventh, octave-reduced 9th subharmonic",
    },
    {
        "ratio": 57 / 32,
        "name": "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    },  # bit of dirt
    {"ratio": 25 / 14, "name": "middle minor seventh"},
    {"ratio": 34 / 19, "name": "quasi-meantone minor seventh"},
    {"ratio": 9 / 5, "name": "classic minor seventh, large minor seventh"},  # naughty
    {"ratio": 38 / 21, "name": "minor neutral undevicesimal seventh"},
    {
        "ratio": 29 / 16,
        "name": "vicesimononal supraminor seventh, octave-reduced 29th harmonic",
    },
    {
        "ratio": 20 / 11,
        "name": "undecimal supraminor seventh, small undecimal neutral seventh",
    },
]

major_seventh: List[Interval] = [
    {"ratio": 42 / 23, "name": "small vicesimotertial neutral seventh"},
    {"ratio": 64 / 35, "name": "septimal neutral seventh"},
    {"ratio": 11 / 6, "name": "undecimal neutral seventh, 21/4-tone"},  # hnnng
    {"ratio": 46 / 25, "name": "large vicesimotertial neutral seventh"},  # also cute
    {"ratio": 24 / 13, "name": "tridecimal neutral seventh"},
    {"ratio": 50 / 27, "name": "grave major seventh"},  # yeah
    {"ratio": 13 / 7, "name": "tridecimal submajor seventh, 16/3-tone"},
    {
        "ratio": 28 / 15,
        "name": "grave major seventh, octave minus a ruyo aug unison",
    },  # dirty
    {
        "ratio": 15 / 8,
        "name": "classic major seventh, just major seventh, octave-reduced 15th harmonic",
    },  # space
    {
        "ratio": 32 / 17,
        "name": "septendecimal major seventh (FJS), septendecimal diminished octave (HEJI), octave-reduced 17th subharmonic",  # strange
    },
    {
        "ratio": 17 / 9,
        "name": "septendecimal major seventh (HEJI), septendecimal diminished octave (FJS)",
    },
    {
        "ratio": 36 / 19,
        "name": "undevicesimal major seventh, Boethius' major seventh",
    },  # naughty
    {
        "ratio": 243 / 128,
        "name": "Pythagorean major seventh, octave-reduced 243rd harmonic",
    },
    {
        "ratio": 19 / 10,
        "name": "undevicesimal diminished octave, Eratosthenes' major seventh",
    },  # lopsideded
    {"ratio": 40 / 21, "name": "septimal acute major seventh"},  # ear damage
    {"ratio": 61 / 32, "name": "octave-reduced 61st harmonic"},
    {
        "ratio": 21 / 11,
        "name": "large undecimal diminished octave, undecimal major seventh",
    },
    {"ratio": 44 / 23, "name": "small vicesimotertial major seventh"},
    {"ratio": 23 / 12, "name": "large vicesimotertial major seventh"},  # yeah
    {"ratio": 48 / 25, "name": "classic diminished octave"},
    {"ratio": 25 / 13, "name": "lesser tridecimal diminished octave"},  # ina=sane
    {
        "ratio": 27 / 14,
        "name": "supermajor seventh, septimal major seventh",
    },  # oh better
    {
        "ratio": 31 / 16,
        "name": "tricesimoprimal ultramajor seventh (FJS), tricesimoprimal semidiminished octave (HEJI), octave-reduced 31st harmonic",
    },
]
