import numpy as np


def is_diagonally_dominant(A, n):
    """Sprawdza, czy macierz A jest diagonalnie dominująca."""
    for i in range(n):
        diag = abs(A[i, i])
        off_diag_sum = sum(abs(A[i, j]) for j in range(n) if j != i)
        if diag <= off_diag_sum:
            return False
    return True


def jacobi_method(A, b, n, criterion='a', max_iterations=100, tolerance=1e-6, x0=None):
    """Implementacja metody Jacobiego z wyborem kryterium stopu."""
    if not is_diagonally_dominant(A, n):
        print("Macierz nie jest diagonalnie dominująca - metoda może nie być zbieżna!")
        return None

    # Wektor początkowy (domyślnie zera, jeśli nie podano)
    x = np.zeros(n) if x0 is None else x0.copy()
    x_new = np.zeros(n)

    if criterion == 'a':  # Kryterium dokładności
        for iteration in range(max_iterations):
            for i in range(n):
                if A[i, i] == 0:
                    print("Zero na przekątnej - metoda nie może być zastosowana!")
                    return None
                # Obliczanie nowego przybliżenia
                sum_ax = sum(A[i, j] * x[j] for j in range(n) if j != i)
                x_new[i] = (b[i] - sum_ax) / A[i, i]

            # Sprawdzenie warunku stopu (dokładność)
            error = np.max(np.abs(x_new - x))
            if error < tolerance:
                print(f"Zbieżność osiągnięta po {iteration + 1} iteracjach.")
                return x_new

            # Aktualizacja wektora x
            x = x_new.copy()

        print(f"Nie osiągnięto zadanej dokładności po {max_iterations} iteracjach.")
        return x

    else:  # Kryterium liczby iteracji
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