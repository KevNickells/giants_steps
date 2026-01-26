from itertools import product
from time import sleep

from codey_bits.final_intervals import (
    preferred_fifths,
    preferred_major_sevenths,
    preferred_natural_thirds,
)
from codey_bits.generate_sine import Sine, mix_samples, play_samples

all_combinations = list(
    product(preferred_natural_thirds, preferred_fifths, preferred_major_sevenths)
)


root = 440
duration = 12.0
a = Sine(frequency=root, duration=duration)

for tup in all_combinations:
    three, five, seven = tup

    third = Sine(frequency=root * three["ratio"], duration=duration)
    fifth = Sine(frequency=root * five["ratio"], duration=duration)
    seven = Sine(frequency=root * seven["ratio"], duration=duration)

    mixed = mix_samples([a.samples, third.samples, fifth.samples, seven.samples])
    # print("---------------------")
    # print(fifth["name"])
    # print(fifth["ratio"])
    # print("---------------------")
    play_samples(mixed)
    sleep(2)
