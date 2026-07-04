import sounddevice as sd
import numpy as np
import time

# --- SETTINGS ---
SAMPLE_RATE = 44100
CHUNK_SIZE = 4410
THRESHOLD = 0.25

# Tracker variables
switch_on = False
last_clap_time = 0

print("🎙️ Microphone is LIVE! Listening for claps...")
print("💡 [SWITCH STATUS]: OFF")
print("------------------------------------------")


def audio_callback(indata, frames, time_info, status):
    global switch_on, last_clap_time

    current_time = time.time()

    peak_volume = np.max(np.abs(indata))

    if peak_volume > THRESHOLD and (current_time - last_clap_time) > 0.5:
        switch_on = not switch_on
        last_clap_time = current_time

        status_text = "💡 ON!" if switch_on else "🌑 OFF..."

        print(
            f"💥 Clap Detected! Volume: {peak_volume:.2f} -> "
            f"[SWITCH STATUS]: {status_text}"
        )


try:
    with sd.InputStream(
        callback=audio_callback,
        channels=1,
        samplerate=SAMPLE_RATE,
        blocksize=CHUNK_SIZE
    ):
        while True:
            time.sleep(1)

except KeyboardInterrupt:
    print("\n👋 Stopped listening.")