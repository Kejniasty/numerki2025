### Created by
### Lech Czochra
### Aleksandra Jakóbik

import math

# more optimal power function, it operates on O(log n) computing time
# when exponent is odd, we multiply the result by the base,
# then we multiply base by itself, and lastly we take half of the exponent away
def power(base, exponent):
    result = 1.0
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent = exponent // 2
    return result

# sinus function
# it is given by the formula y = sin(2x)
def local_sin(x):
    return math.sin(2 * x)

# exponential function
# it is given by the formula y = 3^x
def local_exp(x):
    return power(3, x)

# polynomial function
# it is given by the formula y = 2x^3 - 4x^2 - 6x + 12
# to make its calculation time faster, we use Horner's method (O(n))
def local_polynomial(x):
    return x * (x * (2 * x - 4) - 6) + 12

# sinus' derivative
# (sin(2x))' = 2cos(2x)
def local_sin_derivative(x):
    return 2 * math.cos(2 * x)

# exponential function's derivative
# (3^x)' = 3^x * ln(3)
def local_exp_derivative(x):
    return power(3, x) * math.log(3)

# polynomial's derivative
# (2x^3 - 4x^2 - 6x + 12)' = 6x^2 - 8x - 6
# also calculated with Horner's method
def local_polynomial_derivative(x):
    return x * (6 * x - 8) - 6


# Bisection method
# Parameters:
## function - int, specifies what non-linear function will be used in the algorithm
## upper_bound, lower_bound - float, specifies the bounds of an interval, where we want to find the root of the function
## criterion - char (a or b), specifies what kind of stop criterion should be used
## epsilon - float, used when criterion == 'a', stops the algorithm if abs(f(found_root)) < epsilon
# Return values:
## found_root - float, value of a root of the specified function in the chosen interval
def bisection_method(function, upper_bound, lower_bound, criterion='b', epsilon=0):
    found_root = upper_bound + lower_bound / 2
    # TODO: implement the algorithm, should be recursive with the 'a' criterion?
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