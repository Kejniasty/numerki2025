import numpy as np
from matplotlib import pyplot as plt

import interpolation as ip

FUNCTIONS = {
    1: "Funkcja liniowa",
    2: "Funkcja z wartością bezwzględną",
    3: "Funkcja wielomianowa",
    4: "Funkcja trygonometryczna",
    5: "Funkcja liniowa z funkcji wielomianowej",
    6: "Funkcja z wartością bezwzględną z trygonometrycznej",
    7: "Funkcja wielomianowa z funkcji liniowej",
    8: "Funkcja trygonometrzyczna z wartości bezwzględnej",
    9: "Funkcja liniowa z funkcji trygonometrycznej",
    10: "Funkcja wielomianowa z wartości bezwzględnej"
}

x_nodes = [-4, -2, -1, 1, 2, 4]
# Calculate function values at nodes
figure, axis = plt.subplots(3, 2)
for row in range(3):
    for col in range(2):
        selected_func = lambda x: ip.select_function(row * 2 + col + 1, x)
        y_nodes = [selected_func(x) for x in x_nodes]

        # Calculate interpolation coefficients
        coeffs = ip.calculate_divided_differences(x_nodes, y_nodes)

        # Generate points for plotting
        x_plot = np.linspace(-5, 5, 200)
        y_original = [selected_func(x) for x in x_plot]
        y_interpolated = [ip.newton_evaluate(x, x_nodes, coeffs) for x in x_plot]

        # Plotting
        axis[row][col].plot(x_plot, y_original, '-', color='#1f9f8b', label='Funkcja oryginalna')
        axis[row][col].plot(x_plot, y_interpolated, '--', color = '#9BECBB', label='Wielomian Interpolujący')
        axis[row][col].plot(x_nodes, y_nodes, 'D', color = '#ec9bcc', label='Węzły interpolacji')
        axis[row][col].grid(True)
        axis[row][col].legend()
        axis[row][col].set_title(FUNCTIONS[row * 2 + col + 1])

plt.show()