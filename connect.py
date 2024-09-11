import filter
import generator
import matplotlib.pyplot as plt

import optimization

sig1 = []
sig2 = []

g_shim = []
x = []

def connect():
    xx = []
    for i in range(8000):
        xx.append(i)
        sig1.append(generator.get_sin(5, 50, i))
        sig2.append(generator.get_sin(5, 51, i))
    draw(xx, sig2)




def shim():
    g = 0
    for i in range(1, len(sig1), 1):
        x.append(i/4)
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
    filter.filter_ter(x, g_shim)



def draw(x, y):
    plt.plot(x, y)

    # Добавляем заголовок и подписи осей
    plt.title("Синусоидальная функция")
    plt.xlabel("x")
    plt.ylabel("y")

    # Отображаем график
    plt.show()






connect()
shim()