import numpy
import librosa

(audio_signal, sample_rate) = librosa.load("./sc_exercises/homework_3/wav/audio.wav", sr=None)

from matplotlib import pyplot
from matplotlib.pyplot import Axes

histogram_bin_edges = numpy.linspace(-0.4, 0.4, 801)

histogram: Axes = pyplot.axes()
histogram.hist(audio_signal, bins=histogram_bin_edges)
histogram.set_yscale("log")
histogram.set(xlabel="sound pressure", ylabel="absolute frequency of values", title="Histogram of Audio.wav")

pyplot.show()