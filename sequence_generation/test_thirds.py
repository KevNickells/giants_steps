from time import sleep

from codey_bits.final_intervals import preferred_major_sevenths
from codey_bits.generate_sine import Sine, mix_samples, play_samples

root = 440
duration = 5.0

# for third in preferred_minor_thirds:
#    a = Sine(frequency=root, duration=duration)
#    interval = Sine(frequency=root * third["ratio"], duration=duration)
#
#    mixed = mix_samples([a.samples, interval.samples])
#    print("---------------------")
#    print(third["name"])
#    print(third["ratio"])
#    print("---------------------")
#
#    play_samples(mixed)
#    sleep(2)

for fifth in preferred_major_sevenths:
    a = Sine(frequency=root, duration=duration)
    interval = Sine(frequency=root * fifth["ratio"], duration=duration)

    mixed = mix_samples([a.samples, interval.samples])
    print("---------------------")
    print(fifth["name"])
    print(fifth["ratio"])
    print("---------------------")

    play_samples(mixed)
    sleep(2)
