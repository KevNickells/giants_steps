from itertools import product
from time import sleep

from sequence_generation.final_intervals import (
    preferred_fifths,
    preferred_major_sevenths,
    preferred_natural_thirds,
)
from sequence_generation.generate_sine import Sine, mix_samples, play_samples

all_combinations = list(
    product(preferred_natural_thirds, preferred_fifths, preferred_major_sevenths)
)


root = 440
duration = 9.0
a = Sine(frequency=root, duration=duration)
# random.shuffle(all_combinations)

eliminated = [
    (
        "vicesimotertial neutral third",
        "vengeance subfifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    (
        "vicesimotertial neutral third",
        "vengeance subfifth",
        "undevicesimal major seventh, Boethius' major seventh",
    ),
    (
        "vicesimotertial neutral third",
        "undevicesimal meantone fifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    (
        "vicesimotertial neutral third",
        "undevicesimal meantone fifth",
        "undevicesimal major seventh, Boethius' major seventh",
    ),
    (
        "vicesimotertial neutral third",
        "Kirnberger's fifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    (
        "vicesimotertial neutral third",
        "Kirnberger's fifth",
        "septimal acute major seventh",
    ),
    (
        "vicesimotertial neutral third",
        "just perfect fifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    (
        "vicesimotertial neutral third",
        "just perfect fifth",
        "undevicesimal major seventh, Boethius' major seventh",
    ),
    (
        "vicesimotertial neutral third",
        "wide biyatismic fifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    (
        "vicesimotertial neutral third",
        "wide biyatismic fifth",
        "septimal acute major seventh",
    ),
    (
        "vicesimotertial neutral third",
        "undevicesimal acute fifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    (
        "vicesimotertial neutral third",
        "undevicesimal acute fifth",
        "undevicesimal major seventh, Boethius' major seventh",
    ),
    (
        "witchcraft major third",
        "vengeance subfifth",
        "undevicesimal major seventh, Boethius' major seventh",
    ),
    ("witchcraft major third", "vengeance subfifth", "septimal acute major seventh"),
    (
        "witchcraft major third",
        "undevicesimal meantone fifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    (
        "witchcraft major third",
        "undevicesimal meantone fifth",
        "undevicesimal major seventh, Boethius' major seventh",
    ),
    (
        "witchcraft major third",
        "Kirnberger's fifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    (
        "witchcraft major third",
        "Kirnberger's fifth",
        "undevicesimal major seventh, Boethius' major seventh",
    ),
    (
        "witchcraft major third",
        "just perfect fifth",
        "undevicesimal major seventh, Boethius' major seventh",
    ),
    ("witchcraft major third", "just perfect fifth", "septimal acute major seventh"),
    (
        "witchcraft major third",
        "wide biyatismic fifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    ("witchcraft major third", "wide biyatismic fifth", "septimal acute major seventh"),
    (
        "witchcraft major third",
        "undevicesimal acute fifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    (
        "witchcraft major third",
        "undevicesimal acute fifth",
        "undevicesimal major seventh, Boethius' major seventh",
    ),
    (
        "just/Pythagorean major third meantone",
        "vengeance subfifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    (
        "just/Pythagorean major third meantone",
        "vengeance subfifth",
        "septimal acute major seventh",
    ),
    (
        "just/Pythagorean major third meantone",
        "undevicesimal meantone fifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    (
        "just/Pythagorean major third meantone",
        "undevicesimal meantone fifth",
        "undevicesimal major seventh, Boethius' major seventh",
    ),
    (
        "just/Pythagorean major third meantone",
        "Kirnberger's fifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    (
        "just/Pythagorean major third meantone",
        "Kirnberger's fifth",
        "undevicesimal major seventh, Boethius' major seventh",
    ),
    (
        "just/Pythagorean major third meantone",
        "just perfect fifth",
        "undevicesimal major seventh, Boethius' major seventh",
    ),
    (
        "just/Pythagorean major third meantone",
        "just perfect fifth",
        "septimal acute major seventh",
    ),
    (
        "just/Pythagorean major third meantone",
        "wide biyatismic fifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    (
        "just/Pythagorean major third meantone",
        "wide biyatismic fifth",
        "septimal acute major seventh",
    ),
    (
        "just/Pythagorean major third meantone",
        "undevicesimal acute fifth",
        "undevicesimal major seventh, Boethius' major seventh",
    ),
    (
        "just/Pythagorean major third meantone",
        "undevicesimal acute fifth",
        "septimal acute major seventh",
    ),
    (
        "5/7-kleismic major third",
        "vengeance subfifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    (
        "5/7-kleismic major third",
        "vengeance subfifth",
        "undevicesimal major seventh, Boethius' major seventh",
    ),
    (
        "5/7-kleismic major third",
        "undevicesimal meantone fifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    (
        "5/7-kleismic major third",
        "undevicesimal meantone fifth",
        "septimal acute major seventh",
    ),
    (
        "5/7-kleismic major third",
        "Kirnberger's fifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    ("5/7-kleismic major third", "Kirnberger's fifth", "septimal acute major seventh"),
    (
        "5/7-kleismic major third",
        "just perfect fifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    ("5/7-kleismic major third", "just perfect fifth", "septimal acute major seventh"),
    (
        "5/7-kleismic major third",
        "wide biyatismic fifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    (
        "5/7-kleismic major third",
        "wide biyatismic fifth",
        "undevicesimal major seventh, Boethius' major seventh",
    ),
    (
        "5/7-kleismic major third",
        "undevicesimal acute fifth",
        "undecimal neutral seventh, 21/4-tone",
    ),
    (
        "5/7-kleismic major third",
        "undevicesimal acute fifth",
        "undevicesimal major seventh, Boethius' major seventh",
    ),
    (
        "vicesimotertial neutral third",
        "vengeance subfifth",
        "septimal acute major seventh",
    ),
    (
        "just/Pythagorean major third meantone",
        "undevicesimal meantone fifth",
        "septimal acute major seventh",
    ),
    (
        "5/7-kleismic major third",
        "Kirnberger's fifth",
        "undevicesimal major seventh, Boethius' major seventh",
    ),
    (
        "5/7-kleismic major third",
        "undevicesimal meantone fifth",
        "undevicesimal major seventh, Boethius' major seventh",
    ),
]

for tup in all_combinations:
    three, five, seven = tup
    name_tup = (three["name"], five["name"], seven["name"])

    if name_tup in eliminated:
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
