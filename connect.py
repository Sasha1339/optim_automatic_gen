import filter
import generator
import matplotlib.pyplot as plt
import shim_ideal

import optimization






delta_K = 0.00001
delta_T = 0.00001

f1 = 50
f2 = 51

f_discret = 4000

def connect(f_discret, f1, f2):
    sig1 = []
    sig2 = []
    xx = []
    for i in range(f_discret): #количество точек
        xx.append(i / (f_discret))
        sig1.append(generator.get_sin(5, f1, i, f_discret))
        sig2.append(generator.get_sin(5, f2, i, f_discret))
    # draw(xx, sig1)
    return sig1, sig2




def shim(f_discret, sig1, sig2, K, T, print=False):
    g_shim = []
    x = []
    g = 0
    for i in range(1, len(sig1), 1):
        x.append(i/f_discret)
        nullable1 = False
        nullable2 = False
        if sig1[i] * sig1[i-1] <= 0:
            nullable1 = True
        if sig2[i] * sig2[i-1] <= 0:
            nullable2 = True

        if (nullable1 and not nullable2) or (nullable2 and not nullable1):
            if g == 0:
                g = 1
            else:
                g = 0
        g_shim.append(g)
    if print:
        return filter.filter_ter(x, g_shim, f_discret, K, T, 2), x
    return g_shim, x



def draw(x, y):
    plt.plot(x, y)

    # Добавляем заголовок и подписи осей
    plt.title("Синусоидальная функция")
    plt.xlabel("x")
    plt.ylabel("y")

    # Отображаем график
    plt.show()






# sig1, sig2 = connect(f_discret, f1, f2)
# shim_i = shim_ideal.generate(f_discret, f1, f2, sig1, sig2)
#
# shim(f_discret, sig1, sig2)
# draw(x, shim_i)