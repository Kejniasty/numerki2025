import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

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

def legendre_approximation(f, n, a=-1, b=1, num_points=1001):
    """
    Aproksymacja funkcji f za pomocą wielomianów Legendre'a do stopnia n
    na przedziale [a, b] z użyciem własnej kwadratury Simpsona.

    Parametry:
    - f: funkcja do aproksymacji
    - n: maksymalny stopień wielomianu Legendre'a
    - a, b: przedział aproksymacji
    - num_points: liczba punktów do całkowania (musi być nieparzysta)

    Zwraca:
    - x_vals: punkty w [a, b]
    - approx_vals: wartości funkcji aproksymowanej
    """
    if num_points % 2 == 0:
        raise ValueError("num_points musi być nieparzyste dla reguły Simpsona.")

    # Punkty w [-1, 1]
    t = np.linspace(-1, 1, num_points)
    x = 0.5 * (b - a) * t + 0.5 * (a + b)
    fx = f(x)
    coeffs = []

    for k in range(n + 1):
        Pk = sp.legendre(k)
        integrand = fx * Pk(t)
        ak = simpson_integrate(integrand, t)
        ak *= (2 * k + 1) / 2
        coeffs.append(ak)

    # Obliczanie wartości aproksymacji
    x_vals = np.linspace(a, b, num_points)
    t_vals = (2 * x_vals - (a + b)) / (b - a)
    approx_vals = np.zeros_like(t_vals)

    for k, ak in enumerate(coeffs):
        Pk = sp.legendre(k)
        approx_vals += ak * Pk(t_vals)

    return x_vals, approx_vals

# Przykład użycia
if __name__ == "__main__":
    f = lambda x: np.exp(x)
    n = 5
    a, b = 0, 5
    x_vals = np.linspace(a, b, 1000)
    true_vals = f(x_vals)

    x_approx, approx_vals = legendre_approximation(f, n, a, b)

    plt.plot(x_vals, true_vals, label='f(x) = exp(x)', linewidth=2)
    plt.plot(x_approx, approx_vals, '--', label=f'Legendre approx. (n={n})')
    plt.legend()
    plt.title(f"Aproksymacja Legendre'a na przedziale [{a}, {b}]")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

# TODO: Własna implementacja wielomianów LeGendre'a, zwracająca listę współczynników, wykorzystanych w Hornerze
# TODO: interakcja z użytkownikiem
# TODO: dodanie warunków stopu tzn. error lub stopień wielomianu LeGendre'a