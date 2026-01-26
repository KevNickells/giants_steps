import array
import math

import pyaudio


class Sine:
    volume = 0.5
    sampling_rate = 44100

    def __init__(self, frequency, duration):
        self.frequency = frequency
        self.duration = duration
        self.num_samples = int(self.sampling_rate * self.duration)
        self.samples = self.get_samples()

    def get_samples(self):
        return [
            self.volume
            * math.sin(2 * math.pi * k * self.frequency / self.sampling_rate)
            for k in range(0, self.num_samples)
        ]


def mix_samples(sample_lists):
    num_samples = min(len(samples) for samples in sample_lists)
    mixed = [sum(samples[i] for samples in sample_lists) for i in range(num_samples)]

    max_amp = max(abs(sample) for sample in mixed)
    if max_amp > 1.0:
        mixed = [sample / max_amp for sample in mixed]
    return mixed


def play_samples(samples, sampling_rate=44100):
    audio_object = pyaudio.PyAudio()
    output_bytes = array.array("f", samples).tobytes()
    stream = audio_object.open(
        format=pyaudio.paFloat32, channels=1, rate=sampling_rate, output=True
    )
    stream.write(output_bytes)
    stream.stop_stream()
    stream.close()
    audio_object.terminate()
    print("terminated audio")


sine1 = Sine(frequency=440, duration=2.0)
sine2 = Sine(frequency=554.37, duration=2.0)
sine3 = Sine(frequency=790, duration=2.0)
mixed = mix_samples([sine1.samples, sine2.samples, sine3.samples])
play_samples(mixed)
