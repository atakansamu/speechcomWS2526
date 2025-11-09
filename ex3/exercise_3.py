import librosa
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib.pyplot as pyplot
import numpy
from scipy.fft import fft
import math


def round_to_pow_of_2(number: float) -> int:
	(fraction, exponent) = math.frexp(max(number, 1))
	return 1 << (exponent - (fraction == 0.5))

spectrogram: Axes
spectrogram_hann: Axes
figure, [spectrogram, spectrogram_hann] = pyplot.subplots(2,1)

class WindowSequence:

	def __init__(self, samples: numpy.ndarray, sample_rate: float, window_duration_seconds: float, window_step_ratio: float):
		"""
		Exercise 3.1. Windowing
		"""

		

	# we can define this function as a method of the returned object, so we don't need to repeat the parameter definitions
	def plot_spectrogram(self, figure: Figure, diagram: Axes):
		"""
		Exercise 3.2. Spectrogram
		"""

		"""
		3. compute the FFT of the signal using a power of 2 as FFT size
		"""
		

		"""
		4. Determine the times and frequencies for the spectrogram axes
		"""
		

		"""
		5. Reduce the number of rows to the number of plotted frequencies
		"""
		

		"""
		6. Compute power spectral density in dB
		"""
		


		diagram.set(ylabel="Frequency [Hz]", xlabel="Time [s]", title="Spectrogram")

		# use keyword argument `shading="gouraud"` for linearly interpolated colour
		color_mesh = diagram.pcolormesh(*numpy.meshgrid(times, frequencies), power_spectral_density_db)
		figure.colorbar(color_mesh)

"""
1. Read the WAV audio data from the folder
"""


"""
2. compute the windowed segments for the spectrogram
"""



windows.plot_spectrogram(figure, spectrogram)

"""
Exercise 3.3. Spectrogram with Hann Window
"""

def hann_window(window_size: int) -> numpy.ndarray:

	pass




# reuse the code from exercise 3.2
windows.plot_spectrogram(figure, spectrogram_hann)

spectrogram_hann.set_title("Spectrogram with Hann Window")

pyplot.show()
