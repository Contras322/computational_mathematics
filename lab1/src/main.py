import numpy as np
from advanced import L_i, inaccuracy_x, inaccuracy_y, plot_thousand_splines, plot_stat
from base import qubic_spline_coeff, spline_plot, qubic_spline


if __name__ == '__main__':
    x_nodes = np.arange(0.0, 1.1, 0.1)
    y_nodes = [3.37, 3.95, 3.73, 3.59, 3.15, 3.15, 3.05, 3.86, 3.60, 3.70, 3.02]
    current_points = 1000
    vec_count = 1000
    scale = 0.01

    #qs_coeff, a = qubic_spline_coeff(x_nodes, y_nodes)
    #spline_plot(x_nodes, y_nodes, qs_coeff, qubic_spline)
    #spline_plot(x_nodes, y_nodes, qs_coeff, L_i)  # adv 3

    plot_x, plot_y = inaccuracy_x(x_nodes, y_nodes, L_i, scale, vec_count, current_points)
    #plot_x, plot_y = inaccuracy_x(x_nodes, y_nodes, qubic_spline, scale, vec_count, current_points)
    #plot_thousand_splines(plot_x, plot_y, vec_count)
    plot_stat(x_nodes, y_nodes, plot_x, plot_y, current_points, vec_count)

    #plot_x, plot_y = inaccuracy_y(x_nodes, y_nodes, L_i, scale, vec_count, current_points)
    #plot_x, plot_y = inaccuracy_y(x_nodes, y_nodes, qubic_spline, scale, vec_count, current_points)
    #plot_thousand_splines(plot_x, plot_y, vec_count)
    #plot_stat(x_nodes, y_nodes, plot_x, plot_y, current_points,vec_count)
