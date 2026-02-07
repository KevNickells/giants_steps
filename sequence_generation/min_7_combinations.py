from itertools import product

from sequence_generation.final_intervals import (
    preferred_fifths,
    preferred_minor_sevenths,
    preferred_minor_thirds,
)
from sequence_generation.generate_sine import Sine

all_combinations = list(
    product(preferred_minor_thirds, preferred_fifths, preferred_minor_sevenths)
)


root = 440
duration = 12.0
a = Sine(frequency=root, duration=duration)
# random.shuffle(all_combinations)
#
ignoring = [
    (
        "Eratosthenes' minor third",
        "vengeance subfifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "Eratosthenes' minor third",
        "undevicesimal meantone fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "Eratosthenes' minor third",
        "undevicesimal meantone fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "Eratosthenes' minor third",
        "undevicesimal meantone fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "Eratosthenes' minor third",
        "just perfect fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "Eratosthenes' minor third",
        "just perfect fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "Eratosthenes' minor third",
        "wide biyatismic fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "just minor third",
        "vengeance subfifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "just minor third",
        "undevicesimal meantone fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "just minor third",
        "undevicesimal meantone fifth",
        "harmonic/just minor seventh meantone",
    ),
    ("just minor third", "Kirnberger's fifth", "harmonic/just minor seventh meantone"),
    (
        "just minor third",
        "Kirnberger's fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "just minor third",
        "just perfect fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "just minor third",
        "wide biyatismic fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "just minor third",
        "wide biyatismic fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "just minor third",
        "undevicesimal acute fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "just minor third",
        "undevicesimal acute fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "keemic minor third",
        "vengeance subfifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "keemic minor third",
        "undevicesimal meantone fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "keemic minor third",
        "wide biyatismic fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "keemic minor third",
        "wide biyatismic fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "keemic minor third",
        "undevicesimal acute fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "Eratosthenes' minor third",
        "Kirnberger's fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "Eratosthenes' minor third",
        "Kirnberger's fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "Eratosthenes' minor third",
        "Kirnberger's fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "Eratosthenes' minor third",
        "wide biyatismic fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "Eratosthenes' minor third",
        "undevicesimal acute fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "Eratosthenes' minor third",
        "undevicesimal acute fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "just minor third",
        "wide biyatismic fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "keemic minor third",
        "vengeance subfifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "keemic minor third",
        "undevicesimal meantone fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "keemic minor third",
        "Kirnberger's fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "keemic minor third",
        "wide biyatismic fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "keemic minor third",
        "undevicesimal acute fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    (
        "Eratosthenes' minor third",
        "vengeance subfifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "Eratosthenes' minor third",
        "just perfect fifth",
        "harmonic/just minor seventh meantone",
    ),
    (
        "just minor third",
        "undevicesimal meantone fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
    (
        "just minor third",
        "Kirnberger's fifth",
        "subminor seventh, septimal minor seventh, harmonic seventh, natural seventh, octave-reduced 7th harmonic",
    ),
    ("just minor third", "just perfect fifth", "harmonic/just minor seventh meantone"),
    (
        "keemic minor third",
        "undevicesimal acute fifth",
        "quasi-tempered minor seventh, octave-reduced 57th harmonic",
    ),
]

final_list = []

for tup in all_combinations:
    three, five, seven = tup

    # third = Sine(frequency=root * three["ratio"], duration=duration)
    # fifth = Sine(frequency=root * five["ratio"], duration=duration)
    # seventh = Sine(frequency=root * seven["ratio"], duration=duration)

    if (three["name"], five["name"], seven["name"]) in ignoring:
        print("ignoring")
        continue

    final_list.append((three, five, seven))

    # mixed = mix_samples([a.samples, third.samples, fifth.samples, seventh.samples])
    # print("---------------------")
    # print(f"3rd: {three["name"]} + 5th: {five["name"]} + 7th: {seven["name"]}")
    # print("---------------------")
    # play_samples(mixed)
    # sleep(2)

print(final_list)
print(len(final_list))
