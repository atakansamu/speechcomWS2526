import numpy
import librosa

class WindowSequence:

	def __init__(self, samples: numpy.ndarray, sample_rate: float, window_duration_seconds: float, window_step_ratio: float):
		"""
		Splits a signal into multiple windowed segments `self.window_matrix` with window center times `self.window_times` based on the window parameters
		"""

		self.sample_rate = sample_rate

		self.window_size = int(window_duration_seconds * sample_rate)
		self.window_step = int(window_step_ratio * self.window_size)

		self.window_offsets = numpy.arange(stop= len(samples) - self.window_size +1, step= self.window_step)

		self.window_times = self.window_offsets / sample_rate + window_duration_seconds / 2

		window_sample_indices = numpy.add.outer(numpy.arange(self.window_size), self.window_offsets)
		self.window_matrix = samples[window_sample_indices]


def compute_zero_crossings(samples: numpy.ndarray) -> numpy.ndarray:

	return librosa.zero_crossings(samples, pad=False, zero_pos=False)