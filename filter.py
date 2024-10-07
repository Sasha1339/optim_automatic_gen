from scipy.signal import butter, filtfilt, lfilter
from matplotlib import pyplot as plt
import math

def filter_ter(t, shim, f_discret, K, T, order):
    filtred = shim
    for i in range(order):
        filtred = filter_one(filtred, K, T, t, f_discret)
    return filtred

def h(K, T, t):
    return (K / T) * math.exp(-(t / T))

def filter_one(signal, K, T, t, f_discret):
    filtred = []
    for i in range(len(t)):
        sum = 0
        for k in range(len(t)):
            if 0 <= i - k < len(t):  # Проверка  индекса  для  корректной  свертки
                sum += signal[k] * h(K, T, t[i] - k / f_discret)
        filtred.append(sum)
    return filtred

# def h(K1, K2, T1, T2, t):
#     return K1*K2 * (1 - T1 /(T1 - T2)*math.exp(-t / T1) + T2 /(T1 - T2)*math.exp(-t / T2))
