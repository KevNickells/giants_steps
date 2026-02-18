import threading
import time

import numpy as np
import pyaudio
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

RATE = 44100
CHUNK = 10000
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


def audio_stream():
    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK
    )
    while True:
        data = stream.read(CHUNK)
        freq = get_frequency_autocorr(data, RATE)
        if freq > 50:
            socketio.emit("frequency", {"frequency": freq})
        time.sleep(0.05)  # avoid flooding


@socketio.on("connect")
def handle_connect():
    print("Client connected")


if __name__ == "__main__":
    threading.Thread(target=audio_stream, daemon=True).start()
    socketio.run(app, host="0.0.0.0", port=5000)
