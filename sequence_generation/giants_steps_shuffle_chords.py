from dataclasses import dataclass
from random import choice
from time import sleep

from codey_bits.chords import details
from codey_bits.final_intervals import (
    preferred_fifths,
    preferred_major_sevenths,
    preferred_minor_sevenths,
    preferred_minor_thirds,
    preferred_natural_thirds,
)
from codey_bits.generate_sine import Sine, mix_samples, play_samples
from codey_bits.types import reference_tones

samples = []

duration = 12.0

for detail in details:
    key = f"{detail['key'].value}{detail['accidental'].value}"
    root = reference_tones[key]

    @dataclass
    class accidental:
        third = detail["chord_type"].value[1]["accidental"].value
        seventh = (detail["chord_type"].value[3]["accidental"].value,)

    if accidental.third == "♮":
        third = choice(preferred_natural_thirds)
    else:
        third = choice(preferred_minor_thirds)

    fifth = choice(preferred_fifths)

    if accidental.seventh == "♮":
        seventh = choice(preferred_major_sevenths)
    else:
        seventh = choice(preferred_minor_sevenths)

    samples = mix_samples(
        [
            Sine(frequency=root, duration=duration).samples,
            Sine(frequency=root * third["ratio"], duration=duration).samples,
            Sine(frequency=root * fifth["ratio"], duration=duration).samples,
            Sine(frequency=root * seventh["ratio"], duration=duration).samples,
        ]
    )

    print("---------------------")
    print(
        f"1st: {key} 3rd: {third["name"]} + 5th: {fifth["name"]} + 7th: {seventh["name"]}"
    )
    print(f"{key}{detail["chord_type"].name}")
    print("---------------------")

    play_samples(samples)

    sleep(2)
