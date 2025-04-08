import numpy as np
from matplotlib import pyplot as plt

import interpolation as ip

# Get user input
print("Available functions:")
print("1: Linear (2x + 3)")
print("2: Absolute value (|x|)")
print("3: Polynomial (x³ - 2x² + 3x - 4)")
print("4: Trigonometric (sin(2x))")
print("5: Linear(Polynomial)")
print("6: Abs(Trigonometric)")
print("7: Polynomial(Linear)")
print("8: Trig(Abs)")
print("9: Linear(Trig)")
print("10: Polynomial(Abs)")

func_id = int(input("Select function (1-10): "))
a = float(input("Enter start of interval: "))
b = float(input("Enter end of interval: "))
n = int(input("Enter number of nodes: "))

# Get unevenly spaced nodes from user
print(f"Enter {n} node positions between {a} and {b} (in ascending order):")
x_nodes = []
for i in range(n):
    while True:
        x = float(input(f"Node {i + 1}: "))
        if (a <= x <= b) and (not x_nodes or x > x_nodes[-1]):
            x_nodes.append(x)
            break
        print("Invalid input. Node must be within interval and greater than previous node.")

# Calculate function values at nodes
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
plt.plot(x_plot, y_original, '-', color='#1f9f8b', label='Original function')
plt.plot(x_plot, y_interpolated, '--', color = '#9BECBB', label='Interpolating polynomial')
plt.plot(x_nodes, y_nodes, 'D', color = '#ec9bcc', label='Interpolation nodes')
plt.grid(True)
plt.legend()
plt.title('Newton Interpolation (Uneven Nodes)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()