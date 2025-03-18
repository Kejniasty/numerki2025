### Created by
### Lech Czochra
### Aleksandra Jakóbik

# TODO: review the complex function making solution

import math

# used for calculating the value of a polynomial
# takes an array of factors and an x value
# we treat their indexes as the place where they are in the polynomial
# factor with an index = n is the factor of x^m-n
# where m is the length of the factors array
# returns the value of a specified polynomial
def horner_method(factors, x):
    value = factors[0]
    for i in range(1, len(factors)):
        value = factors[i] + value * x
    return value

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
    return power(3, x) - 10

# def test(x):
#     return math.sin(2 * math.pow(3, x))
#
# def test_pochodna(x):
#     return 2 * math.pow(3, x) * math.log(3) * math.cos(2 * math.pow(3, x))

# polynomial function
# it is given by the formula y = 2x^3 - 4x^2 - 6x + 12
# to make its calculation time faster, we use Horner's method (O(n))
def local_polynomial(x):
    return horner_method([2, -4, -6, 12], x)

# # complex function composer
# def compose(f, g, x):
#     return f(g(x))
#
# # complex function derivative composer
# def compose_derivative(f, f_derivative, g, g_derivative, x):
#     return f_derivative(g(x)) * g_derivative(x)

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
    return horner_method([6, -8, -6], x)

# returns the value in x of a function specified by id
def nonlinear_function(func_id, x):
    match func_id:
        case 1:
            return local_polynomial(x)  # Example of a polynomial
        case 2:
            return local_sin(x)  # Example of a trigonometric function
        case 3:
            return local_exp(x)  # Example of an exponential function
        # case 4:
        #     return compose(local_sin, local_polynomial, x)
        # case 5:
        #     return compose(local_polynomial, local_sin, x)
        # case 6:
        #     return compose(local_exp, local_polynomial, x)
        # case 7:
        #     return compose(local_polynomial, local_exp, x)
        # case 8:
        #     return compose(local_exp, local_sin, x)
        # case 9:
        #     return compose(local_sin, local_exp, x)
        # case 10:
        #     return test(x)
        case _:
            raise ValueError("Invalid function identifier.")

# returns the value in x of a derivative of a function specified by id
def nonlinear_function_derivative(func_id, x):
    match func_id:
        case 1:
            return local_polynomial_derivative(x)  # Example of a polynomial
        case 2:
            return local_sin_derivative(x)  # Example of a trigonometric function
        case 3:
            return local_exp_derivative(x)  # Example of an exponential function
        # case 4:
        #     return compose_derivative(local_sin, local_sin_derivative, local_polynomial, local_polynomial_derivative, x)
        # case 5:
        #     return compose_derivative(local_polynomial, local_polynomial_derivative, local_sin, local_sin_derivative, x)
        # case 6:
        #     return compose_derivative(local_exp, local_exp_derivative, local_polynomial, local_polynomial_derivative, x)
        # case 7:
        #     return compose_derivative(local_polynomial, local_polynomial_derivative, local_exp, local_exp_derivative, x)
        # case 8:
        #     return compose_derivative(local_exp, local_exp_derivative, local_sin, local_sin_derivative, x)
        # case 9:
        #     return compose_derivative(local_sin, local_sin_derivative, local_exp, local_exp_derivative, x)
        # case 10:
        #     return test_pochodna(x)
        case _:
            raise ValueError("Invalid function identifier.")

# Bisection method
# Parameters:
## function - int, specifies what non-linear function will be used in the algorithm
## upper_bound, lower_bound - float, specifies the bounds of an interval, where we want to find the root of the function
## epsilon - float, used when criterion == 'a', stops the algorithm if abs(f(found_root)) < epsilon
# Return values:
## found_root - float, value of a root of the specified function in the chosen interval
## iteration - int, amount of loops done by the algorithm
def bisection_method_a(function, lower_bound, upper_bound, epsilon=0):
    if nonlinear_function(function, upper_bound) * nonlinear_function(function, lower_bound) >= 0:
        raise ValueError("Function must have opposite signs at the ends of the interval!")

    found_root = 0
    iteration = 0
    f_mid = float('inf')

    while abs(f_mid) > epsilon:
        iteration += 1
        found_root = (lower_bound + upper_bound) / 2.0
        f_mid = nonlinear_function(function, found_root)

        if nonlinear_function(function, lower_bound) * f_mid < 0:
            upper_bound = found_root
        else:
            lower_bound = found_root

    return found_root, iteration

# Bisection method
# Parameters:
## function - int, specifies what non-linear function will be used in the algorithm
## upper_bound, lower_bound - float, specifies the bounds of an interval, where we want to find the root of the function
## max_iterations - int, specifies how many times the algorithm loops before stopping
# Return values:
## found_root - float, value of a root of the specified function in the chosen interval
def bisection_method_b(function, lower_bound, upper_bound, max_iterations):
    if nonlinear_function(function, upper_bound) * nonlinear_function(function, lower_bound) >= 0:
        raise ValueError("Function must have opposite signs at the ends of the interval!")

    found_root = 0

    for i in range(max_iterations):
        found_root = (lower_bound + upper_bound) / 2.0
        f_mid = nonlinear_function(function, found_root)

        if nonlinear_function(function, lower_bound) * f_mid < 0:
            upper_bound = found_root
        else:
            lower_bound = found_root

    return found_root

# Newton's method
# Parameters:
## function - int, specifies what non-linear function will be used in the algorithm
## upper_bound, lower_bound - float, specifies the bounds of an interval, where we want to find the root of the function
## epsilon - float, stops the algorithm if abs(f(found_root)) < epsilon
# Return values:
## found_root - float, value of a root of the specified function in the chosen interval
## iteration - int, amount of loops done by the algorithm
def newton_method_a(function, lower_bound, upper_bound, epsilon=0):

    if nonlinear_function(function, upper_bound) * nonlinear_function(function, lower_bound) >= 0:
        raise ValueError("Function must have opposite signs at the ends of the interval!")

    found_root = 0.0
    iteration = 0
    f_mid = float('inf')

    while abs(f_mid) > epsilon:
        iteration += 1
        found_root = lower_bound - nonlinear_function(function, lower_bound) / nonlinear_function_derivative(function,
                                                                                                             lower_bound)
        lower_bound = found_root
        f_mid = nonlinear_function(function, lower_bound)
    return found_root, iteration

# Newton's method
# Parameters:
## function - int, specifies what non-linear function will be used in the algorithm
## upper_bound, lower_bound - float, specifies the bounds of an interval, where we want to find the root of the function
## max_iterations - int, specifies how many times the algorithm loops before stopping
# Return values:
## found_root - float, value of a root of the specified function in the chosen interval
def newton_method_b(function, lower_bound, upper_bound, max_iterations):
    if nonlinear_function(function, upper_bound) * nonlinear_function(function, lower_bound) >= 0:
        raise ValueError("Function must have opposite signs at the ends of the interval!")

    found_root = 0.0

    for i in range(max_iterations):
        found_root = lower_bound - nonlinear_function(function, lower_bound) / nonlinear_function_derivative(function,
                                                                                                             lower_bound)
        lower_bound = found_root
    return found_root
