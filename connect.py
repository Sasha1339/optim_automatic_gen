import filter
import generator
import matplotlib.pyplot as plt

import optimization

sig1 = []
sig2 = []

g_shim = []
x = []

f_discret = 4000

def connect(f_discret):
    xx = []
    for i in range(2000):
        xx.append(i / (f_discret))
        sig1.append(generator.get_sin(5, 50, i, f_discret))
        sig2.append(generator.get_sin(5, 60, i, f_discret))
    draw(xx, sig1)
    return sig1, sig2




def shim(f_discret, sig1, sig2):
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
    draw(x, g_shim)
    filter.filter_ter(x, g_shim, f_discret, 1.1, 0.003, 3)



def draw(x, y):
    plt.plot(x, y)

    # Добавляем заголовок и подписи осей
    plt.title("Синусоидальная функция")
    plt.xlabel("x")
    plt.ylabel("y")

    # Отображаем график
    plt.show()






sig1, sig2 = connect(f_discret)
shim(f_discret, sig1, sig2)