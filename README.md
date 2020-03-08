# C4.5
An implementation of C4.5 machine learning algorithm in python, designed for DNA sequence classification.

https://en.wikipedia.org/wiki/C4.5_algorithm

# Projekt zrealizowany w ramach przedmiotu Podstawy sztucznej inteligencji, EiTI PW

1. Treść projektu
Klasyfikacja sekwencji DNA. Użycie własnej implementacji algorytmu C4.5.
Istnieją dwa rodzaje miejsc rozcięcia sekwencji kodującej białko: donory i akceptory. Ich
odnalezienie otwiera drogę do znalezienia eksonów, czyli sekwencji kodujących białka.
Zatem istnieją 2 rozłączne zadania:

1. rozróżnianie prawdziwych donorów od sekwencji je przypominających,
2. rozróżnianie prawdziwych akceptorów od sekwencji je przypominających.

Każdy z otrzymanych zbiorów danych należy rozdzielić na trenujący i testujący lub
zastosować walidację krzyżową.
W pliku spliceDTrainKIS znajdują się dane do problemu rozpoznawania donorów, a w pliku
spliceATrainKIS znajdują się dane do problemu rozpoznawania akceptorów. W pierwszej
linii każdego z nich napisano, na której pozycji (licząc litery od lewej strony) we
fragmentach sekwencji jest granica pomiędzy intronem a eksonem. Dana ta jest zbędna
dla klasyfikatora - może jednak pomóc badaczowi w interpretacji wyników. Dalej w pliku
występują parami: linia określająca czy jest to przykład pozytywny (1) czy negatywny (0)
oraz sam przykład czyli sekwencja DNA. Przykłady negatywne to takie, które częściowo
wyglądają jak miejsca rozcięcia ale nimi nie są.

2. Opis i analiza zbioru danych
Dostarczone dane:
• Ponad 5000-elementowy zbiór sekwencji DNA – 2 oddzielne zestawy danych dla
problemu klasyfikacji donorów i akceptorów,
• Zbiory nie mają brakujących wartości,
• Rozróżniamy 2 klasy: {0} - przykład negatywny, {1} - przykład pozytywny,
• Atrybuty to kolejne pozycje sekwencji,
• Dyskretne wartości atrybutów: G, C, T, N, A, S.
Do podziału danych na treningowe i testowe zastosowaliśmy k-krotną walidację krzyżową.

3. Wnioski
Algorytm C4.5 jest algorytmem zachłannym, dlatego słabo sobie radzi z danymi, w
których znaczna część atrybutów jest nieistotna - w przypadku donorów intron to 8
pozycji z 15, a w przypadku akceptorów, intron to aż 68 z 90 pozycji.
Aby zwiększyć jakość wyników, należałoby rozważyć atrybuty posiadające większą
korelację sąsiadujących ze sobą nukleotydów, np. atrybuty nadające klasę w
zależności od nukleotydu znajdującego się obok lub w danej odległości od
interesującej nas pozycji; atrybuty uwzględniające okresowość w pojawianiu się
danych nukleotydów; atrybuty uwzględniające część sekwencji znajdujących się po
obu stronach rozcięcia.
Atrybuty słabo różnią się między sobą zyskiem informacyjnym,
zatem stworzone drzewo decyzyjne daje niezadowalające wyniki.
