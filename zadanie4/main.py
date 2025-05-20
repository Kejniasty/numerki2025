import integration as ig
import numpy as np
import matplotlib.pyplot as plt


def print_menu():
    """Wyświetla menu wyboru funkcji testowych."""
    print("\n=== Kalkulator całkowania numerycznego ===")
    print("Dostępne funkcje testowe:")
    for i, name in enumerate(ig.function_names, 1):
        print(f"{i}. {name}")
    print("\nOpcje:")
    print("0. Zakończ program")
    print("Wybierz numer funkcji (1-6) lub 0, aby zakończyć:")


def get_valid_input(prompt, valid_range=None, is_float=False):
    """Pobiera poprawną wartość od użytkownika."""
    while True:
        try:
            value = input(prompt)
            if is_float:
                value = float(value)
                if value <= 0:
                    print("Wartość musi być dodatnia!")
                    continue
            else:
                value = int(value)
                if valid_range and value not in valid_range:
                    print(f"Wybierz wartość z zakresu {valid_range}!")
                    continue
            return value
        except ValueError:
            print("Podaj poprawną wartość!")


def get_nodes_list():
    """Pobiera listę liczby węzłów od użytkownika."""
    while True:
        try:
            nodes_input = input("Podaj liczby węzłów (np. 2,3,4,5, oddzielone przecinkami): ")
            nodes_list = [int(n) for n in nodes_input.split(",") if int(n) in [2, 3, 4, 5]]
            if not nodes_list:
                print("Nie podano poprawnych liczb węzłów! Używam domyślnych: 2,3,4,5")
                return [2, 3, 4, 5]
            return nodes_list
        except ValueError:
            print("Podaj poprawne liczby węzłów (np. 2,3,4,5)!")


def plot_function(func, func_name, a=5.0, n=1000, nodes_list=[2, 3, 4, 5]):
    """Generuje wykres funkcji f(x), pole pod f(x)*e^(-x^2) oraz węzły Gaussa-Hermite’a."""
    # Generowanie punktów dla wykresu
    x = np.linspace(-a, a, 1000)
    y = func(x)  # Wartości funkcji f(x)
    if isinstance(y, float):
        y = []
        for element in x:
            y.append(func(element))
        y = np.array(y)

    weight = np.exp(-x ** 2)  # Waga e^(-x^2)
    y_weighted = y * weight  # f(x) * e^(-x^2)

    # Obliczanie pola pod krzywą f(x)*e^(-x^2) na przedziale [-a, a] metodą Simpsona
    area = ig.simpson_rule(-a, a, n, func, weight_func=lambda x: np.exp(-x ** 2))

    # Tworzenie wykresu
    plt.figure(figsize=(10, 6))

    # Wykres funkcji f(x)
    plt.plot(x, y, label=f'{func_name}', color='blue')

    # Pole pod krzywą f(x)*e^(-x^2)
    plt.fill_between(x, 0, y_weighted, alpha=0.3, color='orange', label=f'Pole pod f(x)⋅e⁻ˣ² ≈ {area:.6f}')

    # Rysowanie węzłów Gaussa-Hermite’a
    colors = ['red', 'green', 'purple', 'black']  # Kolory dla różnych liczb węzłów
    for idx, n in enumerate(nodes_list):
        if n in ig.GAUSS_HERMITE_DATA:
            nodes = np.array(ig.GAUSS_HERMITE_DATA[n]['nodes'])
            y_nodes = func(nodes)  # Wartości funkcji w węzłach
            plt.scatter(nodes, y_nodes, color=colors[idx % len(colors)], label=f'Węzły GH (n={n})', s=50, marker='o')

    # Linia y=0
    plt.axhline(0, color='black', linewidth=0.5)

    # Ustawienia wykresu
    plt.title(f'Wykres funkcji {func_name}, pole i węzły Gaussa-Hermite’a')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()

    # Wyświetlenie wykresu
    plt.show()

    return area


def compare_methods(func_idx, epsilon, nodes_list, initial_a=5.0, delta=1.0):
    """Porównuje wyniki kwadratur Simpsona i Gaussa-Hermite'a oraz generuje wykres."""
    func = ig.functions[func_idx]
    func_name = ig.function_names[func_idx]
    print(f"\nFunkcja: {func_name}")
    print(f"Dokładność: {epsilon}")

    # Generowanie wykresu i obliczanie pola
    print("Generowanie wykresu funkcji...")
    area = plot_function(func, func_name, a=initial_a, nodes_list=nodes_list)
    print(f"Pole pod krzywą f(x)⋅e⁻ˣ² na przedziale [-{initial_a}, {initial_a}]: {area:.10f}")

    # Kwadratura Simpsona
    try:
        simpson_result, n_subintervals = ig.composite_simpson(func, epsilon, delta=delta, initial_a=initial_a)
        print(f"Złożona kwadratura Newtona-Cotesa: {simpson_result:.10f}")
        print(f"Liczba podprzedziałów: {n_subintervals}")
    except Exception as e:
        print(f"Błąd w kwadraturze Simpsona: {e}")

    # Kwadratura Gaussa-Hermite’a
    for n in nodes_list:
        try:
            gauss_result = ig.gauss_hermite(func, n)
            print(f"Gauss-Hermite (n={n}): {gauss_result:.10f}")
        except Exception as e:
            print(f"Błąd w kwadraturze Gaussa-Hermite’a (n={n}): {e}")


def main():
    """Główna funkcja programu."""
    while True:
        print_menu()
        choice = get_valid_input("Twój wybór: ", valid_range=[0] + list(range(1, len(ig.function_names) + 1)))

        if choice == 0:
            print("Zakończono program.")
            break

        func_idx = choice - 1
        epsilon = get_valid_input("Podaj dokładność (epsilon, np. 1e-6): ", is_float=True)
        nodes_list = get_nodes_list()

        compare_methods(func_idx, epsilon, nodes_list)


if __name__ == "__main__":
    main()