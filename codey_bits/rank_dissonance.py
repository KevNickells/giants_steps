import itertools
import math
from typing import Iterable, Tuple

from codey_bits.chords import CHORD_SEQUENCE
from codey_bits.maj_7_final_list import maj_7_final_list
from codey_bits.min_7_final_list import min_7_final_list
from codey_bits.seven_final_list import seven_final_list


def critical_bandwidth(f: float) -> float:
    return 1.72 * (f**0.65)


def roughness_pair(f1: float, f2: float, a: float = 3.5, b: float = 5.75) -> float:
    f_low = min(f1, f2)
    cbw = critical_bandwidth(f_low)

    x = abs(f1 - f2) / cbw
    return math.exp(-a * x) - math.exp(-b * x)


def harmonic_partials(
    f0: float, n_partials: int = 10, rolloff: float = 1.0
) -> Iterable[Tuple[float, float]]:
    for n in range(1, n_partials + 1):
        yield (n * f0, 1.0 / (n**rolloff))


def chord_roughness(
    frequencies: Iterable[float], n_partials: int = 10, rolloff: float = 1.0
) -> float:
    spectra = [list(harmonic_partials(f, n_partials, rolloff)) for f in frequencies]

    total = 0.0

    for i, j in itertools.combinations(range(len(spectra)), 2):
        for f1, a1 in spectra[i]:
            for f2, a2 in spectra[j]:
                total += a1 * a2 * roughness_pair(f1, f2)

    return total


A = 440
lsts = []
for lst in [seven_final_list, maj_7_final_list, min_7_final_list]:
    ranked = []
    for vals in lst:
        third, fifth, seventh = vals

        frequencies = (A, A * third["ratio"], A * fifth["ratio"], A * seventh["ratio"])

        ranked.append(
            {
                "ratios": (third["ratio"], fifth["ratio"], seventh["ratio"]),
                "name": f"{third['name']} | {fifth['name']} | {seventh['name']}",
                "frequencies": frequencies,
                "roughness": chord_roughness(frequencies, n_partials=12, rolloff=1.2),
            }
        )

    sorted_by_roughness = sorted(ranked, key=lambda item: item["roughness"])
    lsts.append(sorted_by_roughness)

sevens_ranked, maj_7s_ranked, min_7s_ranked = lsts

for chord in CHORD_SEQUENCE:
    print(f"{chord[0].value}{chord[1].value} {chord[2].name}")


# duration = 12.0
# a = 440


# for indx, tup in enumerate(sorted_by_roughness):
#    frequencies = tup["frequencies"]
#    print(
#        f"Index: {tup['index']}, Roughness: {tup['roughness_rank']:.6f}, Frequencies: {frequencies}"
#    )
#    mixed_list = []
#    for freq in frequencies:
#        tone = Sine(frequency=freq, duration=duration)
#        mixed_list.append(tone.samples)
#
#    mixed = mix_samples(mixed_list)
#    play_samples(mixed)
#    sleep(2)
