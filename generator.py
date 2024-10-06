import math


def get_sin(ampl, freq, t, f_discret):
    return ampl*math.sin(2 * math.pi * freq * t / f_discret)