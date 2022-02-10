import numpy as np
import scipy.stats as sps


def create_A(x_nodes, h):
    n = len(x_nodes)


    def central_diag(n):
        central = np.zeros(n)
        central[0] = 1
        for i in range(1, n - 1):
            central[i] = 2 * (h[i] + h[i - 1])

        central[n - 1] = 1

        return central


    def right_diag(n):
        right = np.zeros(n - 1)
        for i in range(1, n - 1):
            right[i] = h[i]

        return right


    def left_diag(n):
        left = np.zeros(n - 1)
        for i in range(0, n - 2):
            left[i] = h[i - 1]

        return left

    A = np.diag(left_diag(n), k=-1) \
        + np.diag(right_diag(n), k=1) \
        + np.diag(central_diag(n), k=0)

    return A


def create_b(n, h, a):
    def fill_b(n, h, a):
        B = []

        B.append(0)
        for i in range(1, n - 1):
            B.append((3 / h[i] * (a[i + 1] - a[i]) - (3 / h[i - 1] * (a[i] - a[i - 1]))))

        B.append(0)

        return B

    return np.array([i for i in fill_b(n, h, a)])


def create_fault_i(f, n, scale):
    f_i = []
    Z = sps.norm(loc=0, scale=scale).rvs(size=n)

    for i in range(0, n):
        f_i.append(f[i] + Z[i])

    return f_i