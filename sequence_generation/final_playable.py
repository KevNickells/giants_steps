# from time import sleep


#
from sequence_generation.final_sequence import with_inversions

#
duration = 9.375
all_samples = []
#
#
# def generate_silence(sampling_rate=48000):
#    num_samples = int(sampling_rate * 0.2)
#    return [0.0] * num_samples


for index, chord_detail in enumerate(with_inversions):
    print(
        f"{index + 1}. Chord: {chord_detail['chord']}; {chord_detail["intervals"]}; {chord_detail['frequencies']}"
    )
#    sines = [
#        Sine(
#            frequency=freq,
#            duration=duration,
#        )
#        for freq in chord_detail["frequencies"]
#    ]
#
#    mixed = mix_samples([sine.samples for sine in sines])
#
#    play_samples(mixed)
#    all_samples.extend(mixed)
#    all_samples.extend(generate_silence())
#    sleep(0.2)

# save_samples_to_wav(all_samples, "giants_steps_prototype_long.wav")


# with wave.open("giants_steps_prototype_long.wav", "wb") as wf:
#    wf.setnchannels(1)
#    wf.setsampwidth(2)  # 16-bit audio
#    wf.setframerate(48000)
#
#    for chord_detail in with_inversions:
#        sines = [
#            Sine(frequency=freq, duration=duration)
#            for freq in chord_detail["frequencies"]
#        ]
#        mixed = mix_samples([sine.samples for sine in sines])
#
#        int_samples = (np.array(mixed) * 32767).astype(np.int16)
#        wf.writeframes(int_samples.tobytes())
#
#        silence = np.zeros(int(48000 * 0.5), dtype=np.int16)
#        wf.writeframes(silence.tobytes())
