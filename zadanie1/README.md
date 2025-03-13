<!-- TOC -->
* [Znajdowanie miejsca zerowego równań nieliniowych](#znajdowanie-miejsca-zerowego-równań-nieliniowych)
  * [Specyfikacja](#specyfikacja)
  * [Implementacja](#implementacja)
<!-- TOC -->

# Znajdowanie miejsca zerowego równań nieliniowych
autorstwa grupy w składzie:  
- Lech Czochra (aka **Kejniasty**)  
- Aleksanda Jakóbik
## Specyfikacja

*"Program ma mieć wbudowane kilka różnych funkcji nieliniowych: wielomian, trygonometryczną, wykładniczą i ich złożenia. Użytkownik wybiera jedną z funkcji, określa przedział na którym poszukiwane jest miejsce zerowe oraz wybiera kryterium zatrzymania algorytmu: a) spełnienie warunku nałożonego na dokładność albo b) osiągnięcie zadanej liczby iteracji. Następnie użytkownik wprowadza ε (w przypadku wybrania pierwszego kryterium) lub liczbę iteracji (w przypadku wyboru drugiego kryterium). Program wykonuje obliczenia przy użyciu obu metod (bisekcja oraz jeden z przydzielonych wariantów), wyświetla wyniki i rysuje wykres wybranej funkcji na zadanym przedziale, zaznaczając rozwiązania na wykresie. Program ma sprawdzać poprawność założenia o przeciwnych znakach funkcji na krańcach badanego przedziału. Nie trzeba sprawdzać prawdziwości założeń o stałym znaku pochodnych na przedziale. W przypadku metody stycznych dozwolone jest zakodowanie wartości pochodnej na sztywno, nie trzeba jej liczyć numerycznie."*
## Implementacja

