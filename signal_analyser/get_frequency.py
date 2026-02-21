import numpy as np
import pyaudio

RATE = 44100
CHUNK = 4096
FORMAT = pyaudio.paInt16


def get_frequency_autocorr(data, rate):
    audio_data = np.frombuffer(data, dtype=np.int16).astype(np.float32)

    audio_data = (
        audio_data / np.max(np.abs(audio_data))
        if np.max(np.abs(audio_data)) > 0
        else audio_data
    )

    corr = np.correlate(audio_data, audio_data, mode="full")
    corr = corr[len(corr) // 2 :]

    min_period = int(rate / 1000)
    max_period = int(rate / 80)

    corr_crop = corr[min_period:max_period]
    if len(corr_crop) == 0:
        return 0

    peak = np.argmax(corr_crop) + min_period

    if peak == 0:
        return 0

    freq = rate / peak
    return freq


p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK
)

print("Listening for guitar input... (Ctrl+C to quit)")

try:
    while True:
        try:
            data = stream.read(CHUNK, exception_on_overflow=False)
        except IOError:
            print("Input overflowed, skipping this chunk")
            continue
        freq = get_frequency_autocorr(data, RATE)

        if freq > 50:
            print(f"{freq:.1f} Hz", end="\r")

except KeyboardInterrupt:
    print("\nStopped")

stream.stop_stream()
stream.close()
p.terminate()
