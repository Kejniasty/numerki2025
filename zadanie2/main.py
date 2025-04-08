import numpy as np
import math_functions as mf

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


if __name__ == "__main__":
    print("Metoda iteracyjna Jacobiego")
    print("Wprowadź nazwę pliku z danymi (np. 'systems/system.txt') lub 'exit' aby zakończyć:")

    while True:
        filename = input("> ")
        if filename.lower() == 'exit':
            break

        try:
            A, b, n = load_system_from_file(filename)
            print("Macierz A:")
            print(A)
            print("Wektor b:", b)

            # Wybór kryterium stopu
            criterion = input("Wybierz kryterium stopu:\n"
                              "a. Dokładność (|x^(k+1) - x^(k)| < ε)\n"
                              "b. Liczba iteracji\n"
                              "> ")

            if criterion not in {'a', 'b'}:
                print("Nieprawidłowy wybór kryterium! Wybierz 'a' lub 'b'.")
                continue

            if criterion == 'a':
                tol = float(input("Podaj dokładność (np. 0.000001): "))
                max_iter = 100
            else:
                max_iter = int(input("Podaj liczbę iteracji: "))
                tol = 1e-6
            # Opcjonalny wektor startowy
            x0_input = input("Podaj wektor startowy o długości równej ilości równań (np. '1 1 1' dla 3 równań) lub naciśnij Enter dla zerowego: ")
            if x0_input:
                x0_list = list(map(float, x0_input.split()))
                if len(x0_list) != n:
                    print(f"Błąd: Wektor startowy musi mieć {n} elementów, a podano {len(x0_list)}!")
                    x0 = None
                else:
                    x0 = np.array(x0_list)
            else:
                x0 = None

            if criterion == 'a':
                result = mf.jacobi_method_a(A, b, n, tolerance=tol, x0=x0)
            else:
                result = mf.jacobi_method_b(A, b, n, max_iterations=max_iter)

            if result is not None:
                print("Rozwiązanie:", np.round(result, 6))  # Zaokrąglenie do 6 miejsc po przecinku

        except FileNotFoundError:
            print("Plik nie znaleziony!")
        except ValueError as e:
            print(f"Błąd: {e}")
        except Exception as e:
            print(f"Wystąpił błąd: {e}")