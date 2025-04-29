import math

import numpy as np
from matplotlib import pyplot as plt

import interpolation as ip

FUNCTIONS = {
    1: "Funkcja liniowa",
    2: "Funkcja z wartością bezwzględną",
    3: "Funkcja wielomianowa",
    4: "Funkcja trygonometryczna",
    5: "Funkcja liniowa z f. wielomianowej",
    6: "Funkcja z wartością bezwzględną z f. trygonometrycznej",
    7: "Funkcja wielomianowa z f. liniowej",
    8: "Funkcja trygonometrzyczna z wartości bezwzględnej",
    9: "Funkcja liniowa z f. trygonometrycznej",
    10: "Funkcja wielomianowa z wartości bezwzględnej"
}

def create_plot(a, b, x_nodes, func_id):
    selected_func = lambda x: ip.select_function(func_id, x)
    y_nodes = [selected_func(x) for x in x_nodes]

    # Calculate interpolation coefficients
    coeffs = ip.calculate_divided_differences(x_nodes, y_nodes)

    # Generate points for plotting
    x_plot = np.linspace(a, b, 200)
    y_original = [selected_func(x) for x in x_plot]
    y_interpolated = [ip.newton_evaluate(x, x_nodes, coeffs) for x in x_plot]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(x_plot, y_original, '-', color='#1f9f8b', label='Pierwotna funkcja')
    plt.plot(x_plot, y_interpolated, '--', color='#9BECBB', label='Wielomian Interpolujący')
    plt.plot(x_nodes, y_nodes, 'D', color='#ec9bcc', label='Węzły interpolacji')
    plt.grid(True)
    plt.legend()
    plt.title(FUNCTIONS[func_id])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def create_subplots(columns, rows, a, b, x_nodes, functions):
    figure, axis = plt.subplots(rows, columns)
    for row in range(rows):
        for col in range(columns):
            selected_func = lambda x: ip.select_function(functions[row * columns + col], x)
            # Calculate function values at nodes
            y_nodes = [selected_func(x) for x in x_nodes]

            # Calculate interpolation coefficients
            coeffs = ip.calculate_divided_differences(x_nodes, y_nodes)

            # Generate points for plotting
            x_plot = np.linspace(a, b, 200)
            y_original = [selected_func(x) for x in x_plot]
            y_interpolated = [ip.newton_evaluate(x, x_nodes, coeffs) for x in x_plot]

            # Plotting
            axis[row][col].plot(x_plot, y_original, '-', color='#1f9f8b', label='Funkcja oryginalna')
            axis[row][col].plot(x_plot, y_interpolated, '--', color='#9BECBB', label='Wielomian Interpolujący')
            axis[row][col].plot(x_nodes, y_nodes, 'D', color='#ec9bcc', label='Węzły interpolacji')
            axis[row][col].grid(True)
            axis[row][col].legend()
            axis[row][col].set_title(FUNCTIONS[functions[row * columns + col]])

    plt.show()

def create_special_subplots(intervals, x_nodes_list, functions):
    figure, axis = plt.subplots(1, 2)
    for col in range(2):
        selected_func = lambda x: ip.select_function(functions[col], x)
        # Calculate function values at nodes
        y_nodes = [selected_func(x) for x in x_nodes_list[col]]

        # Calculate interpolation coefficients
        coeffs = ip.calculate_divided_differences(x_nodes_list[col], y_nodes)

        # Generate points for plotting
        x_plot = np.linspace(intervals[col][0], intervals[col][1], 200)
        y_original = [selected_func(x) for x in x_plot]
        y_interpolated = [ip.newton_evaluate(x, x_nodes_list[col], coeffs) for x in x_plot]

        # Plotting
        axis[col].plot(x_plot, y_original, '-', color='#1f9f8b', label='Funkcja oryginalna')
        axis[col].plot(x_plot, y_interpolated, '--', color='#9BECBB', label='Wielomian Interpolujący')
        axis[col].plot(x_nodes_list[col], y_nodes, 'D', color='#ec9bcc', label='Węzły interpolacji')
        axis[col].grid(True)
        axis[col].legend()
        axis[col].set_title(FUNCTIONS[functions[col]])

    plt.show()

if __name__ == '__main__':

    # bigger amount of nodes
    interval = (-5, 5)
    nodes = [-4, -2, -1, 1, 2, 4]

    create_subplots(2, 3, interval[0], interval[1], nodes, [1, 2, 3, 5, 7, 10])
    create_subplots(2, 2, interval[0], interval[1], nodes, [4, 6, 8, 9])

    # smaller amount of nodes
    nodes = [-4, 2, 4]
    create_subplots(2, 3, interval[0], interval[1], nodes, [1, 2, 3, 5, 7, 10])
    create_subplots(2, 2, interval[0], interval[1], nodes, [4, 6, 8, 9])

    # when the polynomial function has a direct interpolation
    create_special_subplots( [(-5, 5), (-5, 5)], [[2, 0, 4], [2, 0, 3, 4]], [3, 3])

    # zeros and extreme values of the trigonometric function
    create_special_subplots([(-1, 4), (-1, 4)], [[0, math.pi / 2, math.pi], [math.pi / 4, 3 * math.pi / 4, 5 * math.pi / 4]], [4, 4])

