import math
import numpy as np

# Horner's method for polynomial calculation
def horner_method(factors, x):
    value = factors[0]
    for i in range(1, len(factors)):
        value = factors[i] + value * x
    return value

# Linear function: y = 2x + 3
def local_linear(x):
    return 2 * x + 3

# Absolute value function: y = |x|
def local_abs(x):
    return abs(x)

# Polynomial function: y = x^3 - 2x^2 + 3x - 4
def local_polynomial(x):
    return horner_method([1, -2, 3, -4], x)

# Trigonometric function: y = sin(2x)
def local_trig(x):
    return math.sin(2 * x)

# Function selector
def select_function(func_id, x):
    functions = {
        1: local_linear,
        2: local_abs,
        3: local_polynomial,
        4: local_trig,
        5: lambda x: local_linear(local_polynomial(x)),
        6: lambda x: local_abs(local_trig(x)),
        7: lambda x: local_polynomial(local_linear(x)),
        8: lambda x: local_trig(local_abs(x)),
        9: lambda x: local_linear(local_trig(x)),
        10: lambda x: local_polynomial(local_abs(x))
    }
    return functions.get(func_id, lambda x: 0)(x)


# Newton's interpolation functions
def calculate_divided_differences(x_nodes, y_nodes):
    """Calculate the divided differences for Newton's interpolation."""
    n = len(x_nodes)
    F = np.zeros((n, n))
    F[:, 0] = y_nodes

    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x_nodes[i + j] - x_nodes[i])

    return F[0]  # Return the top row (coefficients)

def newton_evaluate(x, x_nodes, coeffs):
    """Evaluate the Newton interpolation polynomial at point x."""
    result = coeffs[0]
    for i in range(1, len(coeffs)):
        term = coeffs[i]
        for j in range(i):
            term *= (x - x_nodes[j])
        result += term
    return result