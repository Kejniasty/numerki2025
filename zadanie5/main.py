import numpy as np
import matplotlib.pyplot as plt


def horner_method(factors, x):
    value = factors[0]
    for i in range(1, len(factors)):
        value = factors[i] + value * x
    return value


def simpson_integrate(y, x):
    """
    Własna implementacja kwadratury Simpsona.
    - y: wartości funkcji w punktach x (musi mieć nieparzystą liczbę punktów)
    - x: punkty (równomiernie rozłożone)
    """
    n = len(x)
    if n % 2 == 0:
        raise ValueError("Liczba punktów musi być nieparzysta (parzysta liczba przedziałów).")

    h = (x[-1] - x[0]) / (n - 1)
    S = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2])
    return h * S / 3


def legendre_polynomial(n, x):
    """
    Własna implementacja wielomianów Legendre'a P_n(x)
    - n: stopień
    - x: punkt(y), może być skalar lub tablica numpy
    """
    if n == 0:
        return np.ones_like(x)
    elif n == 1:
        return x
    else:
        P0 = np.ones_like(x)
        P1 = x
        for k in range(2, n + 1):
            Pk = ((2 * k - 1) * x * P1 - (k - 1) * P0) / k
            P0, P1 = P1, Pk
        return Pk


def legendre_approximation(f, n, a=-1.0, b=1.0, num_points=1001):
    """
    Aproksymacja funkcji f za pomocą wielomianów Legendre'a do stopnia n
    na przedziale [a, b] z użyciem własnej kwadratury Simpsona.
    """
    if num_points % 2 == 0:
        raise ValueError("num_points musi być nieparzyste dla reguły Simpsona.")

    # Punkty w [-1, 1]
    t = np.linspace(-1, 1, num_points)
    x = 0.5 * (b - a) * t + 0.5 * (a + b)
    fx = f(x)
    coeffs = []

    for k in range(n + 1):
        Pk_t = legendre_polynomial(k, t)
        integrand = fx * Pk_t
        ak = simpson_integrate(integrand, t)
        ak *= (2 * k + 1) / 2
        coeffs.append(ak)

    # Obliczanie wartości aproksymacji
    x_vals = np.linspace(a, b, num_points)
    t_vals = (2 * x_vals - (a + b)) / (b - a)
    approx_vals = np.zeros_like(t_vals)

    for k, ak in enumerate(coeffs):
        Pk = legendre_polynomial(k, t_vals)
        approx_vals += ak * Pk

    return x_vals, approx_vals


if __name__ == "__main__":
    import sys

    # Dostępne funkcje
    functions = {
        "1": ("sin(x)", lambda x: np.sin(x)),
        "2": ("|x|", lambda x: abs(x)),
        "3": ("x^4+3x^2-1", lambda x: horner_method([1, 0, 3, 0, -1], x)),
        "4": ("x+5", lambda x: x + 5),
        "5": ("sin(x^4+3x^2-1)", lambda x: np.sin(horner_method([1, 0, 3, 0, -1], x))),
        "6": ("|x^4+3x^2-1|", lambda x: abs(horner_method([1, 0, 3, 0, -1], x))),
        "7": ("sin|x|", lambda x: np.sin(abs(x))),
    }

    # Wybór funkcji
    print("Wybierz funkcję do aproksymacji:")
    for key, (name, _) in functions.items():
        print(f"{key}. {name}")
    func_choice = input("Twój wybór [1-7]: ").strip()
    if func_choice not in functions:
        print("Niepoprawny wybór funkcji.")
        sys.exit(1)

    func_name, f = functions[func_choice]

    # Wybór przedziału aproksymacji
    try:
        a = float(input("\nPodaj początek przedziału aproksymacji (a): "))
        b = float(input("Podaj koniec przedziału aproksymacji (b): "))
        if a >= b:
            raise ValueError
    except ValueError:
        print("Niepoprawny przedział. Musi być a < b.")
        sys.exit(1)

    num_points = 1001  # nieparzysta liczba punktów

    try:
        n = int(input("Podaj maksymalny stopień wielomianu: "))
    except ValueError:
        print("Niepoprawna wartość stopnia.")
        sys.exit(1)
    x_approx, approx_vals = legendre_approximation(f, n, a=a, b=b, num_points=num_points)
    n_info = f"n={n}"

    # Rysowanie wykresu
    x_vals = np.linspace(a, b, 1000)
    true_vals = f(x_vals)

    plt.plot(x_vals, true_vals, label=f'f(x) = {func_name}', linewidth=2)
    plt.plot(x_approx, approx_vals, '--', label=f'Legendre approx. ({n_info})')
    plt.legend()
    plt.title(f"Aproksymacja Legendre'a na przedziale [{a}, {b}]")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


