import numpy as np
import integration as ig


# Lista funkcji testowych
functions = [ig.f1, ig.f2, ig.f3, ig.f4]
function_names = ["f(x)=1", "f(x)=x^2", "f(x)=sin(x)", "f(x)=x^4"]

# Główna funkcja do porównania metod
def compare_methods(epsilon):
    print(f"Dokładność: {epsilon}")
    for idx, func in enumerate(functions):
        print(f"\nFunkcja: {function_names[idx]}")

        # Kwadratura Simpsona
        simpson_result = ig.composite_simpson(func, epsilon)
        print(f"Złożona kwadratura Simpsona: {simpson_result:.10f}")

        # Kwadratura Gaussa-Hermite’a dla 2, 3, 4, 5 węzłów
        for n in range(2, 6):
            gauss_result = ig.gauss_hermite(func, n)
            print(f"Gauss-Hermite (n={n}): {gauss_result:.10f}")


# Uruchomienie programu
if __name__ == "__main__":
    while True:
        try:
            epsilon = float(input("Podaj dokładność (epsilon, np. 1e-6): "))
            if epsilon <= 0:
                print("Dokładność musi być dodatnia!")
                continue
            break
        except ValueError:
            print("Podaj poprawną liczbę!")
    compare_methods(epsilon=epsilon)