import numpy as np
import matplotlib.pyplot as plt
from tools.tools import create_A, create_b


def qubic_spline_coeff(x_nodes, y_nodes):
    n = len(x_nodes)
    h = np.array([(x_nodes[i + 1] - x_nodes[i]) for i in range(0, n - 1)])
    a = np.array(y_nodes)

    A = create_A(x_nodes, h)
    A_ob = np.linalg.inv(A)
    b = create_b(n, h, a)
    c = A_ob @ b

    b_i = lambda i: (a[i + 1] - a[i]) / h[i] - (h[i] / 3) * (c[i + 1] + 2 * c[i])
    d_i = lambda i: (c[i + 1] - c[i]) / (3 * h[i])

    b = np.array([b_i(i) for i in range(0, n - 1)])
    d = np.array([d_i(i) for i in range(0, n - 1)])

    c = np.delete(c, n - 1)

    return np.c_[b, c, d], a


def qubic_spline(x, x_nodes, a, qs_coeff):
    def get_i():
        n = len(x_nodes)
        for i in range(0, len(x_nodes) - 1):
            if x >= x_nodes[i] and x <= x_nodes[i + 1]:
                return i
        if x > x_nodes[n - 1]:
            return n - 2
        if x < x_nodes[0]:
            return 0

    current_i = get_i()
    current_x = x_nodes[current_i]
    S = a[current_i] + qs_coeff[current_i][0] * (x - current_x) \
        + qs_coeff[current_i][1] * (x - current_x) ** 2 + qs_coeff[current_i][2] * (x - current_x) ** 3

    return S


def d_qubic_spline(x, qs_coeff, x_nodes):
    def get_i():
        n = len(x_nodes)
        for i in range(0, len(x_nodes) - 1):
            if x >= x_nodes[i] and x <= x_nodes[i + 1]:
                return i
        if x > x_nodes[n - 1]:
            return n - 2
        if x < x_nodes[0]:
            return 0

    current_i = get_i()
    current_x = x_nodes[current_i]
    S_pr = qs_coeff[current_i][0] + 2 * qs_coeff[current_i][1] * (x - current_x)\
           + 3 * qs_coeff[current_i][2] * (x - current_x) ** 2

    return S_pr


def spline_plot(x_nodes, y_nodes, qs_coeff, interpolate):
    new_y_nodes = []
    qub_x_nodes = x_nodes
    n = len(x_nodes) - 1
    current_points = n * 100

    new_x_nodes = np.linspace(0, 1, current_points)

    for x in new_x_nodes:
        new_y_nodes.append(interpolate(x, qub_x_nodes, y_nodes, qs_coeff))

    plt.plot(new_x_nodes, new_y_nodes, color='green')
    plt.plot(x_nodes, y_nodes, 'o', color='blue')
    plt.grid(True)
    plt.show()