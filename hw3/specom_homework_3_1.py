from numpy import *
import math
from scipy.signal import ShortTimeFFT, windows, chirp

from matplotlib import pyplot
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import librosa

import soundfile

def round_to_pow_of_2(number: float) -> int:

	return 1 << math.frexp(max(number - 0.125, 1))[1]

def normalized(signal: ndarray, peak_value: float) -> ndarray:

	return signal * (peak_value / max(abs(signal)))

class ChirpSignal:

	def __init__(self, sample_rate: float, filename: str):

		self.sample_rate = sample_rate
		self.sample_period = 1 / sample_rate
		self.times = arange(0, 6, step=self.sample_period)

		self.samples = chirp(self.times, 100, 6, 1000, method="linear")
		self.samples = normalized(self.samples, peak_value=0.99)
		self.duration = len(self.samples) / sample_rate

		self.filename = filename
		soundfile.write(filename, self.samples, self.sample_rate)

	def plot_spectrogram(self, time_step_seconds: float) -> tuple[Figure, Axes]:

		window_time_step = int(time_step_seconds * self.sample_rate)
		window_length = 2 * window_time_step

		# sym=... tells for a window whether the last sample should be at the edge of the time interval
		stft = ShortTimeFFT(
			win=windows.hann(window_length, sym=False),
			hop=window_time_step,
			fs=self.sample_rate,
			mfft=round_to_pow_of_2(window_length)
		)
		self.power_spectral_density = stft.spectrogram(self.samples)
		self.power_spectral_density_db = librosa.power_to_db(self.power_spectral_density)

		spectrogram: Axes
		figure, spectrogram = pyplot.subplots()
		# available cmaps: 'viridis', 'plasma', 'inferno', 'magma', 'cividis'
		image_quadmesh = spectrogram.imshow(self.power_spectral_density_db, origin="lower", cmap="viridis", aspect="auto", extent=stft.extent(len(self.samples)))
		
		spectrogram.set(xlabel="time [s]", ylabel="frequency [Hz]", title=f"Spectrogram {self.filename}")
		figure.colorbar(image_quadmesh, ax=spectrogram, format="%+2.f dB")  # "%+2.f" means "show 2 pre-decimals with explicit sign for non-negatives"

		return (figure, spectrogram)

chirp_signal_1 = ChirpSignal(10_000, "chirp1.wav")
chirp_signal_2 = ChirpSignal(1000, "chirp2.wav")

chirp_signal_1.plot_spectrogram(0.01)
chirp_signal_2.plot_spectrogram(0.01)

pyplot.show()