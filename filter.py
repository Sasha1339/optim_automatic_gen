from scipy.signal import butter, filtfilt
from matplotlib import pyplot as plt

def filter_ter(t, shim):
    cutoff_freq = 8
    order = 4
    sampling = 4000

    b, a = butter(order, cutoff_freq / (0.5 * sampling), btype='lowpass')

    filtred = filtfilt(b, a, shim)

    plt.plot(t, filtred)
    plt.title("Синусоидальная функция")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()
