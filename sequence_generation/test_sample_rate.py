import pyaudio


def is_sample_rate_supported(rate):
    p = pyaudio.PyAudio()
    try:
        info = p.get_default_output_device_info()
        supported = p.is_format_supported(
            rate,
            output_device=info["index"],
            output_channels=1,
            output_format=pyaudio.paFloat32,
        )
        return supported
    except Exception as e:
        print(f"Sample rate {rate} not supported: {e}")
        return False
    finally:
        p.terminate()


for rate in [44100, 48000, 22050, 16000]:
    print(f"{rate} Hz: {is_sample_rate_supported(rate)}")
