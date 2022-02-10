import numpy as np
import matplotlib.pyplot as plt


def f_x(x):
    return 1 / (x + 3)


def a_0_opt(x):
    a = np.sum(x ** 2) * np.sum(f_x(x)) - (np.sum(x) * np.sum(x * f_x(x)))
    b = x.size * np.sum(x ** 2) - np.sum(x) ** 2
    return a / b


def a_1_opt(x):
    a = x.size * np.sum(x * f_x(x)) - (np.sum(x) * np.sum(f_x(x)))
    b = x.size * np.sum(x ** 2) - np.sum(x) ** 2
    return a / b


def f_x_approx(a_0, a_1, x):
    return a_0 + a_1 * x


def plot_fun():
    n_counts = [3, 30, 300]
    a = -1
    b = 1

    x_nodes = np.linspace(a, b, n_counts[len(n_counts) - 1])
    plt.plot(x_nodes, f_x(x_nodes), label="f(x)", color="red", linewidth=3)
    for n in n_counts:
        x_nodes = np.linspace(a, b, n)
        a_0 = a_0_opt(x_nodes)
        a_1 = a_1_opt(x_nodes)
        f_approx = [f_x_approx(a_0, a_1, x) for x in x_nodes]
        plt.plot(x_nodes, f_approx, label=f"f_approx(x) для n = {n}", linewidth=2)

    plt.grid(True)
    plt.legend(fontsize=8)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    plot_fun()
