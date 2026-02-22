import threading
import time

import aubio
import numpy as np
import pyaudio
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Audio config
RATE = 44100
CHUNK = 4096
FORMAT = pyaudio.paInt16

# Aubio pitch detection
pitch_o = aubio.pitch("yinfft", CHUNK, CHUNK, RATE)
pitch_o.set_unit("Hz")
pitch_o.set_silence(-40)


def find_usb_device(p):
    """Find the first available USB audio input device."""
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        if "usb" in info["name"].lower() and info["maxInputChannels"] > 0:
            print(f"Using device [{i}]: {info['name']}")
            return i
    print("No USB device found, falling back to default input")
    return None


def audio_stream():
    p = pyaudio.PyAudio()
    device_index = find_usb_device(p)

    stream = p.open(
        format=FORMAT,
        channels=1,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
        input_device_index=device_index,
    )

    print("Audio stream started")

    while True:
        try:
            data = stream.read(CHUNK, exception_on_overflow=False)
        except IOError:
            print("Input overflowed, skipping chunk")
            continue

        samples = np.frombuffer(data, dtype=np.int16).astype(np.float32)
        samples /= 32768.0

        freq = pitch_o(samples)[0]
        confidence = pitch_o.get_confidence()

        if 50 < freq < 1400:
            socketio.emit("frequency", {"frequency": round(float(freq), 2)})

        time.sleep(0.005)


@socketio.on("connect")
def handle_connect():
    print("Client connected")


@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")


if __name__ == "__main__":
    threading.Thread(target=audio_stream, daemon=True).start()
    socketio.run(app, host="0.0.0.0", port=5000)
