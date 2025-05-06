import numpy as np
from scipy.special import roots_hermite
import math


# Funkcje testowe (bez wagi e^(-x^2), która jest uwzględniona w kwadraturze Gaussa-Hermite'a)
def f1(x):
    return 1.0  # Stała funkcja


def f2(x):
    return x ** 2  # Parabola


def f3(x):
    return np.sin(x)  # Sinus


def f4(x):
    return x ** 4  # Wielomian 4. stopnia


# Lista funkcji testowych
functions = [f1, f2, f3, f4]
function_names = ["f(x)=1", "f(x)=x^2", "f(x)=sin(x)", "f(x)=x^4"]


# Kwadratura Simpsona na przedziale [a, b] z n podprzedziałami
def simpson_rule(a, b, n, func, weight_func=lambda x: 1.0):
    if n % 2 != 0:
        n += 1  # Simpson wymaga parzystej liczby podprzedziałów
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x) * weight_func(x)
    result = y[0] + y[-1] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2])
    return result * h / 3


# Obliczanie granicy dla całki na przedziale (-∞, +∞) w metodzie Simpsona
def simpson_infinite(func, epsilon, delta=1.0, initial_a=5.0):
    def weight_func(x):
        return np.exp(-x ** 2)

    result = 0.0
    a = initial_a

    # Całkowanie w prawo: [0, +∞)
    current = 0.0
    while True:
        integral = simpson_rule(current, current + delta, 100, func, weight_func)
        result += integral
        if abs(integral) < epsilon:
            break
        current += delta

    # Całkowanie w lewo: (-∞, 0]
    current = 0.0
    while True:
        integral = simpson_rule(-current - delta, -current, 100, func, weight_func)
        result += integral
        if abs(integral) < epsilon:
            break
        current += delta

    return result


# Złożona kwadratura Simpsona z iteracyjnym zwiększaniem podprzedziałów
def composite_simpson(func, epsilon):
    n = 10  # Początkowa liczba podprzedziałów
    prev_result = simpson_infinite(func, epsilon=epsilon)

    while True:
        n *= 2  # Podwajanie liczby podprzedziałów
        current_result = simpson_infinite(func, epsilon=epsilon)
        if abs(current_result - prev_result) < epsilon:
            return current_result
        prev_result = current_result


# Kwadratura Gaussa-Hermite’a dla n węzłów
def gauss_hermite(func, n):
    x, w = roots_hermite(n)  # Węzły i wagi Hermite’a
    return sum(w * func(x))


# Główna funkcja do porównania metod
def compare_methods(epsilon):
    print(f"Dokładność: {epsilon}")
    for idx, func in enumerate(functions):
        print(f"\nFunkcja: {function_names[idx]}")

        # Kwadratura Simpsona
        simpson_result = composite_simpson(func, epsilon)
        print(f"Złożona kwadratura Simpsona: {simpson_result:.10f}")

        # Kwadratura Gaussa-Hermite’a dla 2, 3, 4, 5 węzłów
        for n in range(2, 6):
            gauss_result = gauss_hermite(func, n)
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