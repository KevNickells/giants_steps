import random
from itertools import product
from time import sleep

from codey_bits.final_intervals import (
    preferred_fifths,
    preferred_minor_sevenths,
    preferred_minor_thirds,
)
from codey_bits.generate_sine import Sine, mix_samples, play_samples

all_combinations = list(
    product(preferred_minor_thirds, preferred_fifths, preferred_minor_sevenths)
)


root = 440
duration = 12.0
a = Sine(frequency=root, duration=duration)
random.shuffle(all_combinations)

for tup in all_combinations:
    three, five, seven = tup

    third = Sine(frequency=root * three["ratio"], duration=duration)
    fifth = Sine(frequency=root * five["ratio"], duration=duration)
    seventh = Sine(frequency=root * seven["ratio"], duration=duration)

    mixed = mix_samples([a.samples, third.samples, fifth.samples, seventh.samples])
    print("---------------------")
    print(f"3rd: {three["name"]} + 5th: {five["name"]} + 7th: {seven["name"]}")
    print("---------------------")
    play_samples(mixed)
    sleep(2)
