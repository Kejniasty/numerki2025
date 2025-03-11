### Created by
### Lech Czochra
### Aleksandra Jakóbik

# TODO: maybe implement mathematical functions as def functions

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