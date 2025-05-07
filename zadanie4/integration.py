import numpy as np
import math

# Funkcje testowe (bez wagi e^(-x^2), która jest uwzględniona w kwadraturze Gaussa-Hermite'a)
def f1(x):
    """f(x) = x^2 + 3"""
    return x * x + 3

def f2(x):
    """f(x) = cos(2x)"""
    return np.cos(2 * x)

def f3(x):
    """f(x) = 8cos(x) - 2sin(x)"""
    return 8*np.cos(x)-2*np.sin(x)

def f4(x):
    """f(x) = e(x) + 9)"""
    return np.exp(x)+9

def f5(x):
    """f(x) = x^2 - 2x + 1 + 2cos(3x)"""
    return x*x-2*x+1+2*np.cos(3*x)

def f6(x):
    """f(x) = 1 (analityczna wartość całki: sqrt(pi) ≈ 1.7724538509)"""
    return 1.0

# Lista funkcji testowych i ich nazwy
functions = [f1, f2, f3, f4, f5, f6]
function_names = ["f(x)=x^2+3", "f(x)=cos(2x)", "f(x)=8cos(x)-2sin(x)", "f(x)=e(x)+9", "f(x)=x^2-2x+1+2cos(3x)", "f(x)=1"]

# Kwadratura Simpsona na przedziale [a, b] z n podprzedziałami
def simpson_rule(a, b, n, func, weight_func=lambda x: 1.0):
    """Oblicza całkę na przedziale [a, b] metodą Simpsona z n podprzedziałami."""
    if n % 2 != 0:
        n += 1  # Simpson wymaga parzystej liczby podprzedziałów
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x) * weight_func(x)
    result = y[0] + y[-1] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2])
    return result * h / 3

# Obliczanie granicy dla całki na przedziale (-∞, +∞) w metodzie Simpsona
def simpson_infinite(func, epsilon, n, delta=1.0, initial_a=5.0):
    """Oblicza całkę na (-∞, +∞) z wagą e^(-x^2) metodą Simpsona."""
    def weight_func(x):
        return np.exp(-x ** 2)

    result = 0.0

    # Całkowanie na przedziale [-initial_a, initial_a]
    result = simpson_rule(-initial_a, initial_a, n, func, weight_func)

    # Całkowanie w prawo: [initial_a, +∞)
    current = initial_a
    while True:
        integral = simpson_rule(current, current + delta, n, func, weight_func)
        result += integral
        if abs(integral) < epsilon:
            break
        current += delta

    # Całkowanie w lewo: (-∞, -initial_a]
    current = initial_a
    while True:
        integral = simpson_rule(-current - delta, -current, n, func, weight_func)
        result += integral
        if abs(integral) < epsilon:
            break
        current += delta

    return result

# Złożona kwadratura Simpsona z iteracyjnym zwiększaniem podprzedziałów
def composite_simpson(func, epsilon, delta=1.0, initial_a=5.0):
    """Iteracyjnie zwiększa liczbę podprzedziałów, aż osiągnięta zostanie dokładność epsilon.
    Zwraca krotkę (wynik, liczba podprzedziałów)."""
    n = 10  # Początkowa liczba podprzedziałów
    prev_result = simpson_infinite(func, epsilon=epsilon, n=n, delta=delta, initial_a=initial_a)

    while True:
        n *= 2  # Podwajanie liczby podprzedziałów
        current_result = simpson_infinite(func, epsilon=epsilon, n=n, delta=delta, initial_a=initial_a)
        if abs(current_result - prev_result) < epsilon:
            return current_result, n
        prev_result = current_result

# Tablicowane węzły i wagi dla kwadratury Gaussa-Hermite'a (probabilistyczne wielomiany Hermite'a)
GAUSS_HERMITE_DATA = {
    2: {
        'nodes': [-0.7071067811865475, 0.7071067811865475],
        'weights': [0.886226925452758, 0.886226925452758]
    },
    3: {
        'nodes': [-1.224744871391589, 0.0, 1.224744871391589],
        'weights': [0.29540897515091937, 1.1816359006036774, 0.29540897515091937]
    },
    4: {
        'nodes': [-1.650680123885785, -0.5246476232752903, 0.5246476232752903, 1.650680123885785],
        'weights': [0.08131283544724518, 0.8049140900055128, 0.8049140900055128, 0.08131283544724518]
    },
    5: {
        'nodes': [-2.020182870456086, -0.9585724646138185, 0.0, 0.9585724646138185, 2.020182870456086],
        'weights': [0.019953242059045913, 0.39361932315224113, 0.9453087204829419, 0.39361932315224113, 0.019953242059045913]
    }
}

# Kwadratura Gaussa-Hermite’a dla n węzłów
def gauss_hermite(func, n):
    """Oblicza całkę na (-∞, +∞) z wagą e^(-x^2) metodą Gaussa-Hermite'a."""
    if n not in GAUSS_HERMITE_DATA:
        raise ValueError(f"Liczba węzłów {n} nie jest wspierana. Wybierz 2, 3, 4 lub 5.")
    nodes = np.array(GAUSS_HERMITE_DATA[n]['nodes'])
    weights = np.array(GAUSS_HERMITE_DATA[n]['weights'])
    return sum(weights * func(nodes))