import matplotlib.pyplot as plt
import numpy as np
import sys
import wave


def get_signal(spf):

    if spf.getnchannels() == 2:
        print("Just mono files")
        sys.exit(0)
    signal = spf.readframes(-1)
    signal = np.fromstring(signal, "Int16")
    return signal


def get_sample_rate(spf):
    global sample_rate
    sample_rate = spf.getframerate()


def make_timespace(signal):
    global t
    t = np.arange(0, len(signal) / sample_rate, 1 / sample_rate)


spf = wave.open("Impulse_mono.wav", "r")
signal = get_signal(spf)
get_sample_rate(spf)
make_timespace(signal)

plt.subplot(211)
plt.plot(t, signal)
plt.subplot(212)
plt.psd(signal, 512, sample_rate)
plt.show()
