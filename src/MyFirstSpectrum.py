import matplotlib.pyplot as plt
import numpy as np
import sys
import wave

spf = wave.open("Impulse_mono.wav", "r")
# If Stereo
if spf.getnchannels() == 2:
    print("Just mono files")
    sys.exit(0)
signal = spf.readframes(-1)
signal = np.fromstring(signal, "Int16")
sample_rate = spf.getframerate()
dt = 1 / sample_rate
t = np.arange(0, len(signal) / sample_rate, dt)

plt.subplot(211)
plt.plot(t, signal)
plt.subplot(212)
plt.psd(signal, 512, sample_rate)
plt.show()