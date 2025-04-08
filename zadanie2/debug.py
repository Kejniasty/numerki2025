import math_functions as mf
import os
import numpy as np

def load_system_from_file(filename):
    """Wczytuje układ równań z pliku."""
    with open(filename, 'r') as f:
        lines = f.readlines()
        n = int(lines[0].strip())  # Pierwsza linia: liczba równań
        if n > 10:
            raise ValueError("Maksymalna liczba równań to 10!")

        A = np.zeros((n, n))
        b = np.zeros(n)

        # Wczytanie macierzy A
        for i in range(n):
            row = list(map(float, lines[i + 1].strip().split()))
            A[i] = row[:n]
            b[i] = row[n]  # Ostatnia liczba w wierszu to b[i]

        return A, b, n

try:
    print(mf.inverse_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
except:
    print("Couldn't calculate inversion")

jacobi_c = mf.calculate_jacobi_c([[0.5, -0.0625, 0.1875, 0.0625],
    [-0.0625, 0.5, 0, 0],
    [0.1875, 0, 0.375, 0.125],
    [0.0625, 0, 0.125, 0.25]])
print(jacobi_c)
print(mf.check_convergence(jacobi_c))

sciezka = './systems'
for nazwa_pliku in os.listdir(sciezka):
    pelna_sciezka = os.path.join(sciezka, nazwa_pliku)
    if os.path.isfile(pelna_sciezka):
        print(f'reading file {nazwa_pliku}')
        A, B, n = load_system_from_file(pelna_sciezka)
        try:
            print(mf.jacobi_method_a(A, B, n))
        except:
            print(f"Nieudana metoda Jacobi dla {nazwa_pliku}")
    print("\n")


