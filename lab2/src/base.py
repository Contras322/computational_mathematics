"""
Base part of lab_2
"""
import numpy as np
import matplotlib.pyplot as plt


def diff_f(x):
    g = 10
    try:
        nom = 2 * np.cos(2 * x) * (1 - np.cos(2 * x) ** 2) - 4 * np.cos(2 * x) * np.sin(2 * x) ** 2
        dom = np.sqrt(2) * np.sqrt(g) * ((1 - np.cos(2 * x) ** 2) ** 2) * np.sqrt(np.sin(2 * x) / (1 - np.cos(2 * x) ** 2) + 1)
        f = nom / dom
        if f > 40 or f < -40:
            raise ValueError
    except ValueError:
        print("ERROR")
        return None

    return f


def get_real(a):
    g = 10
    C = 1.03439984
    T = 1.75418438

    return (T - a) * np.sqrt(2 * C / g)


def fun(t):
    g = 10
    C = 1.03439984

    return 1 / np.sqrt(2 * g) * np.sqrt((2 + 2 *\
            (np.sin(2 * t) / (1 - np.cos(2 * t))) ** 2) / (C * (1 - np.cos(2 * t)))) * C * (1 - np.cos(2 * t))


def composite_simpson(a, b, n, f):
    if n % 2 == 1:
        n -= 1
        f.pop(len(f) - 1)

    h = (b - a) / n
    len_f = len(f)
    odd_sum = 0
    even_sum = 0
    for i in range(1, len_f - 1):
        if (i + 1) % 2 == 0:
            even_sum += f[i]
        else:
            odd_sum += f[i]

    f_sim = (h / 3) * (f[0] + 2 * odd_sum + 4 * even_sum + f[len_f - 1])

    return f_sim


def composite_trapezoid(a, b, n, f):
    h = (b - a) / n
    len_f = len(f)
    sum = 0

    for i in range(2, len_f):
        sum += f[i]

    f_sim = (h / 2) * (f[0] + 2 * sum + f[len_f - 1])

    return f_sim


def create_f(a, b, n):
    h = (b - a) / n
    t = []
    for i in range(1, n + 2):
        t.append(a + (i - 1) * h)

    f = []
    for item in t:
        f.append(fun(item))

    return f


def log_log_plot():
    T = 1.75418438
    a = 1e-7
    b = T
    n = [i for i in range(3, 10000, 100)]
    f_real = get_real(a)

    for item in n:
        h = (b - a) / item
        y = abs(f_real - composite_simpson(a, b, item, create_f(a, b, item)))
        plt.scatter(h, y, color="darkturquoise", s=7, label="simpson")
        y = abs(f_real - composite_trapezoid(a, b, item, create_f(a, b, item)))
        plt.scatter(h, y, color="yellowgreen", s=7, label="trapezoid")

    plt.legend(['simpson', 'trapezoid'])
    plt.loglog()
    plt.grid(True)
    plt.show()



def plot_diff_f():
    x = np.linspace(-4, 4, 5000)
    y = []
    for item in x:
        y.append(diff_f(item))

    plt.plot(x, y, color="navy", label="diff f")
    plt.legend()
    plt.grid(True)
    plt.show()
