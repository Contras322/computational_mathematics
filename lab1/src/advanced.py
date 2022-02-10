import numpy as np
from matplotlib import pyplot as plt
from base import qubic_spline_coeff, qubic_spline
from tools.tools import create_fault_i


def l_i(i, x, x_nodes):
    l_i = 1.0

    for j in range(0, len(x_nodes)):
        if i == j:
            continue

        l_i *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])

    return l_i


def L_i(x, x_nodes, y_nodes, nothing=None):
    L_i = 0.0

    for i in range(0, len(x_nodes)):
        L_i += y_nodes[i] * l_i(i, x, x_nodes)

    return L_i


def inaccuracy_x(x_nodes, y_nodes, interpolate, scale, vec_count, current_points):
    plot_x_nodes = np.linspace(0, 1, current_points)
    plot_y_nodes = []
    qs_coeff = []

    for i in range(0, vec_count):
        x_i = create_fault_i(x_nodes, len(x_nodes), scale)

        if interpolate == qubic_spline:
            qs_coeff, a = qubic_spline_coeff(x_i, y_nodes)

        plot_y_nodes.append(get_new_y_nodes(x_i, plot_x_nodes, current_points, y_nodes, interpolate, qs_coeff))

    return plot_x_nodes, plot_y_nodes


def inaccuracy_y(x_nodes, y_nodes, interpolate, scale, vec_count, current_points):
    plot_x_nodes = np.linspace(0, 1, current_points)
    qs_coeff = []
    plot_y_nodes = []

    for i in range(0, vec_count):
        y_i = create_fault_i(y_nodes, len(y_nodes), scale)

        if interpolate == qubic_spline:
            qs_coeff, a = qubic_spline_coeff(x_nodes, y_i)

        plot_y_nodes.append(get_new_y_nodes(x_nodes, plot_x_nodes, current_points, y_i, interpolate, qs_coeff))

    return plot_x_nodes, plot_y_nodes


def plot_thousand_splines(plot_x, plot_y, vec_count):
    for i in range(0, vec_count):
        plt.plot(plot_x, plot_y[i])

    plt.grid(True)
    plt.show()


def get_new_y_nodes(x, new_x_nodes, current_points, y_nodes, interpolate, qs_coeff):
    new_y_nodes = [interpolate(new_x_nodes[i], x, y_nodes, qs_coeff) for i in range(0, current_points)]

    return new_y_nodes


def confidence_interval(interval):
    interval = sorted(interval)
    av_num = interval[499]
    dov = []
    dov.append(interval[49])
    dov.append(interval[948])

    return dov[0], av_num, dov[1]


def plot_stat(x_nodes, y_nodes, x, y, current_points, vec_counts):
    new_y_1 = []
    new_y_2= []
    new_y_3 = []

    for i in range(0, current_points):
        _y = []
        for j in range(0, vec_counts):
           _y.append(y[j][i])

        y_1, y_2, y_3 = confidence_interval(_y)
        new_y_1.append(y_1)
        new_y_2.append(y_2)
        new_y_3.append(y_3)

    plt.plot(x, new_y_1, ':', color='red')
    plt.plot(x, new_y_2, color='green')
    plt.plot(x, new_y_3, ':', color='red')
    plt.plot(x_nodes, y_nodes, 'o', color='blue')
    plt.fill_between(x, new_y_1, new_y_3, color='yellow')
    plt.grid(True)
    plt.show()


