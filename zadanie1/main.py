### Created by
### Lech Czochra
### Aleksandra Jakóbik

import equation_solving as es
import matplotlib.pyplot as plt
import numpy as np

function_choice = int(input("Choose a function: \n "
               "1. Polynomial (y = 2x^3 - 4x^2 - 6x + 12) \n "
               "2. Trigonometric (y = sin(2x)) \n "
               "3. Exponential (y = 3^x - 10) \n "
               "4. Trigonometric + Polynomial \n "
               "5. Exponential + Polynomial \n "
               "6. Polynomial + Exponential \n "
               "7. Trigonometric + Exponential \n "))

lower_bound_choice = float(input("Choose a lower bound: \n "))

upper_bound_choice = float(input("Choose a upper bound: \n "))

criterion_choice = input("Choose the stop criterion: \n "
                         "a. |f(xi)| < ε \n "
                         "b. number of iterations \n ")

def plot_function_a (function_id, lower_bound, upper_bound, epsilon):
    # Tworzenie zakresu wartości X
    x = np.linspace(lower_bound, upper_bound, 400)
    y = [es.nonlinear_function(function_id, xi) for xi in x]

    # Rysowanie wykresu
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=f"Function ID {function_id}", color="#740c38")
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')

    root_bisection = es.bisection_method_a(function_id, lower_bound, upper_bound, epsilon)[0]
    root_newton = es.newton_method_a(function_id, lower_bound, upper_bound, epsilon)[0]

    iterations_bisection = es.bisection_method_a(function_id, lower_bound, upper_bound, epsilon)[1]
    iterations_newton = es.newton_method_a(function_id, lower_bound, upper_bound, epsilon)[1]

    print ("Bisection method - found root: ", root_bisection, "iterations: ", iterations_bisection)
    print ("Newton's method - found root: ", root_newton, "iterations: ", iterations_newton)

    plt.scatter(root_bisection, 0, color='#eb468b', label=f'Bisection (ε): x={root_bisection:.5f}', zorder=3, s=110)
    plt.scatter(root_newton, 0, color='#F7B6D1', label=f'Newton (ε): x={root_newton:.5f}', zorder=3, s=50)

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.title("Wykres funkcji z zaznaczonymi miejscami zerowymi")
    plt.show()

    if root_newton < root_bisection:
        x_closer = np.linspace(root_newton - abs(root_bisection - root_newton), root_bisection + abs(root_bisection - root_newton), 400)
    else:
        x_closer = np.linspace(root_bisection - abs(root_bisection - root_newton), root_newton + abs(root_bisection - root_newton), 400)
    y_closer = [es.nonlinear_function(function_id, xi) for xi in x_closer]

    plt.figure(figsize=(8, 5))
    plt.plot(x_closer, y_closer, label=f"Function ID {function_id}", color="#740c38")
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.scatter(root_bisection, 0, color='#eb468b', label=f'Bisection (ε): x={root_bisection:.5f}', zorder=3, s=110)
    plt.scatter(root_newton, 0, color='#F7B6D1', label=f'Newton (ε): x={root_newton:.5f}', zorder=3, s=50)

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.title("Wykres funkcji z zaznaczonymi miejscami zerowymi (mniejsza skala)")
    plt.show()

def plot_function_b (function_id, lower_bound, upper_bound, iterations):
    # Tworzenie zakresu wartości X
    x = np.linspace(lower_bound, upper_bound, 400)
    y = [es.nonlinear_function(function_id, xi) for xi in x]

    # Rysowanie wykresu
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=f"Function ID {function_id}", color="#740c38")
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')

    root_bisection = es.bisection_method_b(function_id, lower_bound, upper_bound, iterations)
    root_newton = es.newton_method_b(function_id, lower_bound, upper_bound, iterations)

    print("Bisection method - found root: ", root_bisection)
    print("Newton's method - found root: ", root_newton)

    plt.scatter(root_bisection, 0, color='#eb468b', label=f'Bisection (ε): x={root_bisection:.5f}', zorder=3, s=110)
    plt.scatter(root_newton, 0, color='#F7B6D1', label=f'Newton (ε): x={root_newton:.5f}', zorder=3, s=50)

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.title("Wykres funkcji z zaznaczonymi miejscami zerowymi")
    plt.show()

    if root_newton < root_bisection:
        x_closer = np.linspace(root_newton - abs(root_bisection - root_newton), root_bisection + abs(root_bisection - root_newton), 400)
    else:
        x_closer = np.linspace(root_bisection - abs(root_bisection - root_newton), root_newton + abs(root_bisection - root_newton), 400)
    y_closer = [es.nonlinear_function(function_id, xi) for xi in x_closer]

    plt.figure(figsize=(8, 5))
    plt.plot(x_closer, y_closer, label=f"Function ID {function_id}", color="#740c38")
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.scatter(root_bisection, 0, color='#eb468b', label=f'Bisection (ε): x={root_bisection:.5f}', zorder=3, s=110)
    plt.scatter(root_newton, 0, color='#F7B6D1', label=f'Newton (ε): x={root_newton:.5f}', zorder=3, s=50)

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.title("Wykres funkcji z zaznaczonymi miejscami zerowymi (mniejsza skala)")
    plt.show()

if criterion_choice == 'a':
    epsilon_choice = float(input("choose epsilon:  \n "))
    plot_function_a(function_choice, lower_bound_choice, upper_bound_choice, epsilon_choice)

else:
    iterations_choice = int(input("choose the number of iterations: \n "))
    plot_function_b(function_choice, lower_bound_choice, upper_bound_choice, iterations_choice)


