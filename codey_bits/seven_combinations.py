from itertools import product
from time import sleep

from codey_bits.final_intervals import (
    preferred_fifths,
    preferred_minor_sevenths,
    preferred_natural_thirds,
)
from codey_bits.generate_sine import Sine, mix_samples, play_samples

all_combinations = list(
    product(preferred_natural_thirds, preferred_fifths, preferred_minor_sevenths)
)


root = 440
duration = 12.0
a = Sine(frequency=root, duration=duration)
# random.shuffle(all_combinations)

ignore = [
    (
        "vicesimotertial neutral third",
        "vengeance subfifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "vicesimotertial neutral third",
        "vengeance subfifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "vicesimotertial neutral third",
        "undevicesimal meantone fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "vicesimotertial neutral third",
        "Kirnberger's fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "vicesimotertial neutral third",
        "just perfect fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "vicesimotertial neutral third",
        "just perfect fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "vicesimotertial neutral third",
        "wide biyatismic fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "vicesimotertial neutral third",
        "undevicesimal acute fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "vicesimotertial neutral third",
        "undevicesimal acute fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "witchcraft major third",
        "vengeance subfifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "witchcraft major third",
        "undevicesimal meantone fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "witchcraft major third",
        "Kirnberger's fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "witchcraft major third",
        "just perfect fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "witchcraft major third",
        "just perfect fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "witchcraft major third",
        "wide biyatismic fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "witchcraft major third",
        "wide biyatismic fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "witchcraft major third",
        "undevicesimal acute fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "just/Pythagorean major third meantone",
        "vengeance subfifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "just/Pythagorean major third meantone",
        "undevicesimal meantone fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "just/Pythagorean major third meantone",
        "Kirnberger's fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "just/Pythagorean major third meantone",
        "just perfect fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "just/Pythagorean major third meantone",
        "just perfect fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "just/Pythagorean major third meantone",
        "wide biyatismic fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "just/Pythagorean major third meantone",
        "wide biyatismic fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "5/7-kleismic major third",
        "vengeance subfifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "5/7-kleismic major third",
        "vengeance subfifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "5/7-kleismic major third",
        "vengeance subfifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "5/7-kleismic major third",
        "undevicesimal meantone fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "5/7-kleismic major third",
        "Kirnberger's fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "5/7-kleismic major third",
        "Kirnberger's fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "5/7-kleismic major third",
        "just perfect fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "5/7-kleismic major third",
        "wide biyatismic fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "5/7-kleismic major third",
        "wide biyatismic fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "5/7-kleismic major third",
        "undevicesimal acute fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "vicesimotertial neutral third",
        "vengeance subfifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "vicesimotertial neutral third",
        "undevicesimal meantone fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "vicesimotertial neutral third",
        "Kirnberger's fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "vicesimotertial neutral third",
        "wide biyatismic fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "witchcraft major third",
        "vengeance subfifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "witchcraft major third",
        "vengeance subfifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "witchcraft major third",
        "Kirnberger's fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "witchcraft major third",
        "undevicesimal acute fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "just/Pythagorean major third meantone",
        "vengeance subfifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "just/Pythagorean major third meantone",
        "vengeance subfifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "just/Pythagorean major third meantone",
        "Kirnberger's fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "just/Pythagorean major third meantone",
        "wide biyatismic fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "just/Pythagorean major third meantone",
        "undevicesimal acute fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "5/7-kleismic major third",
        "undevicesimal meantone fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "5/7-kleismic major third",
        "undevicesimal meantone fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "5/7-kleismic major third",
        "just perfect fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "5/7-kleismic major third",
        "undevicesimal acute fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "vicesimotertial neutral third",
        "undevicesimal meantone fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "vicesimotertial neutral third",
        "just perfect fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "witchcraft major third",
        "undevicesimal meantone fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
]

final = []
for tup in all_combinations:
    three, five, seven = tup

    if (three["name"], five["name"], seven["name"]) in ignore:
        print("ignoring")
        continue

    third = Sine(frequency=root * three["ratio"], duration=duration)
    fifth = Sine(frequency=root * five["ratio"], duration=duration)
    seventh = Sine(frequency=root * seven["ratio"], duration=duration)

    mixed = mix_samples([a.samples, third.samples, fifth.samples, seventh.samples])
    print("---------------------")
    print(f"3rd: {three["name"]} + 5th: {five["name"]} + 7th: {seven["name"]}")
    print("---------------------")
    play_samples(mixed)
    sleep(2)
