import math
from argparse import ArgumentError

import numpy as np

def deep_copy(A):
    copy = []
    for row in A:
        copy.append(row.copy())
    return copy

def is_diagonally_dominant(A, n):
    """Sprawdza, czy macierz A jest diagonalnie dominująca."""
    for i in range(n):
        diag = abs(A[i, i])
        off_diag_sum = sum(abs(A[i, j]) for j in range(n) if j != i)
        if diag <= off_diag_sum:
            return False
    return True

def check_convergence(C):
    # Warunek 1 - maksymalna suma wyrazów w wierszach < 1
    sums = []
    for row in C:
        row_sum = 0
        for element in row:
            row_sum += element
        sums.append(row_sum)
    if max(sums) < 1:
        return True

    # Warunek 2 - maksymalna suma wyrazów w kolumnach < 1
    sums = []
    for column_index in range(len(C[0])):
        column_sum = 0
        for row_index in range(len(C)):
            column_sum += C[row_index][column_index]
        sums.append(column_sum)
    if max(sums) < 1:
        return True

    # Warunek 3 - pierwiastek sum kwadratów w całej macierzy < 1
    squares_sum = 0
    for row in C:
        for element in row:
            squares_sum += element * element
    if math.sqrt(squares_sum) < 1:
        return True

    return False


def inverse_matrix(A):
    if len(A) != len(A[0]):
        raise ArgumentError("Macierz nie jest kwadratowa!")
    A_extended = deep_copy(A)

    # tworzymy macierz rozszerzoną [A | I]
    for row_index in range(len(A)):
        for column_index in range(len(A[0])):
            if row_index == column_index:
                A_extended[row_index].append(1)
            else:
                A_extended[row_index].append(0)

    for i in range(len(A)):
        # Znajdź pivot (najlepiej niezerowy element na przekątnej)
        pivot = A_extended[i][i]
        if pivot == 0:
            # Jeśli pivot = 0, spróbuj zamienić wiersze
            for k in range(i + 1, len(A)):
                if A_extended[k][i] != 0:
                    A_extended[i], A_extended[k] = A_extended[k], A_extended[i]
                    pivot = A_extended[i][i]
                    break
            if pivot == 0:
                raise ValueError("Macierz nie ma odwrotności, wyznacznik = 0!")

        # Podziel wiersz przez pivot, aby na przekątnej była 1
        for j in range(2 * len(A)):
            A_extended[i][j] /= pivot

        # Wyzeruj kolumnę i w innych wierszach
        for k in range(len(A)):
            if k != i:
                factor = A_extended[k][i]
                for j in range(2 * len(A)):
                    A_extended[k][j] -= factor * A_extended[i][j]

    inverted = []
    for row in A_extended:
        inverted.append(row[len(A):])

    return inverted


def multiply_matrixes(A, B):
    C = []
    for row_index in range(len(A)):
        C.append([])
        for column_index in range(len(B[0])):
            sum = 0
            for n in range(len(B)):
                sum += A[row_index][n] * B[n][column_index]
            C[row_index].append(sum)
    return C

def calculate_jacobi_c(A):
    D = []
    for row_index in range(len(A)):
        D.append([])
        for column_index in range(len(A[0])):
            D[row_index].append(0)

    # Obliczenie macierzy L + U oraz D
    C = deep_copy(A)
    for index in range(len(A)):
        D[index][index] = C[index][index]
        C[index][index] = 0

    try:
        D_inverse = inverse_matrix(D)
        C = multiply_matrixes(D_inverse, C)
    except:
        raise ValueError("Macierz D nie ma odwrotności!")

    return C


def jacobi_method_a(A, b, n, tolerance=1e-6, x0=None):
    """Implementacja metody Jacobiego z warunkiem stopu - dokładność"""
    if not is_diagonally_dominant(A, n):
        print("Ostrzeżenie: Macierz nie jest diagonalnie dominująca, ale kontynuuję obliczenia.")

    # Wektor początkowy (domyślnie zera, jeśli nie podano)
    x = np.zeros(n) if x0 is None else x0.copy()
    x_new = np.zeros(n)
    error = float('inf')
    iteration = 0
    if not check_convergence(calculate_jacobi_c(A)):
        print("Macierz nie jest zbiezna - metoda nie może być zastosowana!")
        return None
        # Kryterium dokładności
    while error >= tolerance:
        iteration += 1
        for i in range(n):
            if A[i, i] == 0:
                print("Zero na przekątnej - metoda nie może być zastosowana!")
                return None
            # Obliczanie nowego przybliżenia
            sum_ax = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_ax) / A[i, i]

        # obliczenie dokładności
        error = np.max(np.abs(x_new - x))

        # Aktualizacja wektora x
        x = x_new.copy()


    print(f"Zbieżność osiągnięta po {iteration + 1} iteracjach.")
    return x


def jacobi_method_b(A, b, n, max_iterations=100, x0=None):
    """Implementacja metody Jacobiego z warunkiem stopu - liczba iteracji"""
    if not is_diagonally_dominant(A, n):
        print("Ostrzeżenie: Macierz nie jest diagonalnie dominująca, ale kontynuuję obliczenia.")

    # Wektor początkowy (domyślnie zera, jeśli nie podano)
    x = np.zeros(n) if x0 is None else x0.copy()
    x_new = np.zeros(n)
    if not check_convergence(calculate_jacobi_c(A)):
        print("Macierz nie jest zbiezna - metoda nie może być zastosowana!")
        return None

    for iteration in range(max_iterations):
        for i in range(n):
            if A[i, i] == 0:
                print("Zero na przekątnej - metoda nie może być zastosowana!")
                return None
            # Obliczanie nowego przybliżenia
            sum_ax = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_ax) / A[i, i]

        # Aktualizacja wektora x
        x = x_new.copy()

    print(f"Wykonano {max_iterations} iteracji.")
    return x