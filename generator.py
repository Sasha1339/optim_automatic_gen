import math


def get_sin(ampl, freq, t):
    return ampl*math.sin(2 * math.pi * freq * t / 4000)