from numpy import *
import math

from specom_assignment_1_lib import *

# declarations of user variables
audio_signal: ndarray
times: ndarray

window_times: ndarray
periodicities: ndarray
signal_energies: ndarray
zero_crossing_rates: ndarray
pitch_frequencies: ndarray

"""
Add your Code here
"""


"""
Plot the values
"""

from matplotlib import pyplot
from matplotlib.axes import Axes

signal_diagram: Axes
features_diagram: Axes
frequency_diagram: Axes
figure, (signal_diagram, features_diagram, frequency_diagram) = pyplot.subplots(3,1, sharex=True)

signal_diagram.plot(times, audio_signal)
signal_diagram.set(xlabel="Time [s]", ylabel="Amplitude", title="Speech")
signal_diagram.grid(True)

features_diagram.plot(window_times, periodicities)
features_diagram.plot(window_times, signal_energies)
features_diagram.plot(window_times, zero_crossing_rates)
features_diagram.set(xlabel="Time [s]", ylabel="pₓ, Eₓ, ZCRₓ", title="Features")
features_diagram.legend(["Periodicity", "Energy", "Zero-Crossing Rate"])
features_diagram.grid(True)

frequency_diagram.plot(window_times, pitch_frequencies, '-k')
frequency_diagram.set(xlabel="Time [s]", ylabel="Frequency [Hz]", title="Pitch Contour")
frequency_diagram.grid(True)

pyplot.show()