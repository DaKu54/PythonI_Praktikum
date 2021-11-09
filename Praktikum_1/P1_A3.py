# # Aufgabe 3 - Sortieren <a id='Aufgabe3'></a>
# Erstellen Sie ein Programm, dass vom Benutzer nacheinander 3 Integer-Zahlen entgegennimmt und diese dann in sortierter Reihenfolge (von der kleinsten zur größten Zahl) wieder ausgibt. Benutzen Sie **ausschließlich** die `min` und  `max` Funktion um die kleinste, größte und mittlere Zahl zu finden.
# **Beispiel**
#
# _Eingabe_
# Erste Zahl: 5
# Zweite Zahl: 8
# Dritte Zahl: 3

#Eingabe der Zahlen
erste_zahl = int(input("Erste Zahl: "))
zweite_zahl = int(input("Zweite Zahl: "))
dritte_zahl = int(input("Dritte Zahl: "))

#Ermitteln der kleinsten, größten und mittleren Zahl
min_zahl = min(erste_zahl, zweite_zahl, dritte_zahl)
max_zahl = max(erste_zahl, zweite_zahl, dritte_zahl)
mit_zahl = (erste_zahl + zweite_zahl + dritte_zahl) - min_zahl - max_zahl

print(min_zahl, mit_zahl, max_zahl)
