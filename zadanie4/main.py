import integration as ig

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

def compare_methods(func_idx, epsilon, nodes_list, initial_a=5.0, delta=1.0):
    """Porównuje wyniki kwadratur Simpsona i Gaussa-Hermite'a."""
    func = ig.functions[func_idx]
    print(f"\nFunkcja: {ig.function_names[func_idx]}")
    print(f"Dokładność: {epsilon}")

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