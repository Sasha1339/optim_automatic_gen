import control.matlab as matlab
import numpy as np
from matplotlib import pyplot as plt


def calculate_filter(pwm):
    R = 100
    C = 0.0001
    tau = R * C



    dt = 0.001

    t = np.arange(0, 0.499, dt)

    v_out = np.zeros(len(pwm))
    for i in range(1, len(pwm)):
        v_out[i] = v_out[i-1] * np.exp(-dt / tau) + (1 - np.exp(-dt / tau)) * pwm[i]

    q = len(v_out)
    a = len(t)

    plt.plot(t, v_out)

    # Добавляем заголовок и подписи осей
    plt.title("func функция")
    plt.xlabel("x")
    plt.ylabel("y")

    # Отображаем график
    plt.show()