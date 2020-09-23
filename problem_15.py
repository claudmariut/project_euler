"""How many such routes are there through a 20×20 grid?."""

import math


def lattice_paths(x_origin, y_origin, x_target, y_target):
    """Return number of lattice paths given origin and target"""
    vector = (math.fabs(x_target - x_origin), math.fabs(y_target - y_origin))
    # Binomial coefficient.
    n = vector[0] + vector[1]
    k = vector[0]
    paths = (math.factorial(n)/((math.factorial(k))*(math.factorial(n-k))))
    print(paths)


lattice_paths(0, 20, 20, 0)