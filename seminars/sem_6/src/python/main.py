import math
import numpy as np
import matplotlib.pyplot as plt


def f(t, y):
    return 0.5 * math.e ** (t - y)


def y_solution(t):
    return math.log(0.5 * (math.e ** t - 1 + 2 * math.e))


def time_integrate(y_0, a, b, h):
    m = int((b - a) / h)
    y = np.zeros((m + 1,))
    t = np.linspace(a, b, m + 1)
    y[0] = y_0

    for i in range(m):
        t_i = a + i * h
        y[i + 1] = y[i] + h * f(t_i, y[i])

    return t, y


if __name__ == '__main__':
    y_0 = 1
    a = 0
    b = 1
    h = 0.5
    t_approx, y_approx = time_integrate(y_0, a, b, h)
    t = np.linspace(a, b, 200)
    fig, ax = plt.subplots(1, 1, figsize=(14, 6))
    y = [y_solution(i) for i in t]
    print(y_solution(1) - y_approx[2])
    ax.plot(t, y, '-', linewidth=2, label=r"$y(t)$")
    ax.plot(t_approx, y_approx, 'o--', linewidth=2, label=r"$w_i$")
    ax.set_xlabel(r'$t$', fontsize=16)
    ax.set_ylabel(r'$y$', fontsize=16)
    ax.grid()
    ax.legend(loc='lower right', fontsize=16)
    plt.show()
