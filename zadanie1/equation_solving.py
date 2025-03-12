### Created by
### Lech Czochra
### Aleksandra Jakóbik

# TODO: maybe implement mathematical functions as def functions

import math

def nonlinear_function(func_id, x):
    if func_id == 1:
        return x**3 - 4*x - 9 # Example of a polynomial
    elif func_id == 2:
        return math.sin(x) - 0.5 # Example of a trigonometric function
    elif func_id == 3:
        return math.exp(x) - 3 # Example of an exponential function
    else:
        raise ValueError("Invalid function identifier.")

# Bisection method
# Parameters:
## function - int, specifies what non-linear function will be used in the algorithm
## upper_bound, lower_bound - float, specifies the bounds of an interval, where we want to find the root of the function
## criterion - char (a or b), specifies what kind of stop criterion should be used
## epsilon - float, used when criterion == 'a', stops the algorithm if abs(f(found_root)) < epsilon
# Return values:
## found_root - float, value of a root of the specified function in the chosen interval

# TODO: finish implementing the algorithm, still not recursive with 'a' criterion
def bisection_method(function, upper_bound, lower_bound, criterion='b', epsilon=0, max_iterations=100):

    if nonlinear_function(function, upper_bound) * nonlinear_function(function, lower_bound) >= 0:
        raise ValueError("Function must have opposite signs at the ends of the interval!")

    for iteration in range(max_iterations):
        found_root = (lower_bound + upper_bound) / 2.0
        f_mid = nonlinear_function(function, found_root)

        if criterion == 'a' and abs(f_mid) < epsilon:
            return found_root

        if criterion == 'b' and abs(upper_bound - lower_bound) < epsilon:
            return found_root

        if nonlinear_function(function, lower_bound) * f_mid < 0:
            upper_bound = found_root
        else:
            lower_bound = found_root

    return found_root

# Newton's method
# Parameters:
## function - int, specifies what non-linear function will be used in the algorithm
## upper_bound, lower_bound - float, specifies the bounds of an interval, where we want to find the root of the function
## criterion - char (a or b), specifies what kind of stop criterion should be used
## epsilon - float, used when criterion == 'a', stops the algorithm if abs(f(found_root)) < epsilon
# Return values:
## found_root - float, value of a root of the specified function in the chosen interval
def newton_method(function, upper_bound, lower_bound, criterion='b', epsilon=0):
    found_root = 0.0
    # TODO: implement the algorithm
    return found_root