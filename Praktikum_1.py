# # Aufgaben
# 
# 
#  - [Aufgabe 1](#Aufgabe1): Hallo Student!
#  - [Aufgabe 2](#Aufgabe2): Steuern und Trinkgelder.
#  - [Aufgabe 3](#Aufgabe3): Sortieren.
#  - [Aufgabe 4](#Aufgabe4): Zeitumrechnung.


# # Aufgabe 1 - Hallo Student! <a id='Aufgabe1'></a>
# Schreiben Sie ein Programm, dass eine Studentin / einen Student nacheinander nach dem Vor-, Nachnamen und der Matrikelnummer fragt und diese dann "ordentlich" formatiert direkt untereinander ausgibt. Das Ausgabeformat sollte dieser Vorgabe entsprechen 

#Abfragen der persönlichen Daten
nachname = input("Bitte geben Sie ihren Nachnamen ein: ")
vorname = input("Bitte geben Sie ihren Vornamen ein: ")
matrikelnummer = input("Bitte geben Sie ihren Matrikelnummer ein: ")

print("\n")

#Ausgabe der Daten nacheinander
print(nachname, vorname)
print("Matrikelnummer: " + matrikelnummer)


# # Aufgabe 2 - Steuern und Trinkgelder <a id='Aufgabe2'></a>
# 
# Entwickeln Sie ein Programm, dass zunächst die Kosten für ein Essen in einem Restaurant vom Benutzer einliest. Ihr Programm soll dann den Steuerbetrag und das Trinkgeld für das Gericht berechnen und ausgeben. Der Steuersatz beträgt $19\%$ und Sie berechnen das Trinkgeld als $23\%$ des Essensbetrags (ohne Steuer). Die Ausgabe Ihres Programms sollte dieser Vorgabe entsprechen
# Kosten für Gericht (inklusive Steuer): 25.29 Euro
# Steuer (19%): 4.81 Euro
# Trinkgeld (23%): 4.71 Euro
# Gesamtausgabe: 30.00 Euro
# Das erreichen Sie, indem Sie `:.2f` als Formatierungszeichen in `print` für die entsprechenden Variablen verwenden. 

# Lösen Sie Aufgabe 2 in dieser Zelle

#Eingabe der Kosten
gericht_kosten = float(input("Kosten: "))
print("\n")

#Berechnung von Steuern, Trinkgeld und der gesamten Ausgaben
steuern = (gericht_kosten/100)*19
trinkgeld = (((gericht_kosten-steuern)/100)*23)
gesamt_ausgaben = gericht_kosten+trinkgeld

#Ausgabe der Berechnungen und Formatierung auf zwei Nachkommastellen
print("Kosten für Gericht (inklusive Steuer): " +  "%.2f" % gericht_kosten + " Euro")
print("Steuer (19%): " + "%.2f" % steuern + " Euro")
print("Tringeld (23%): " + "%.2f" % trinkgeld + " Euro")
print("Gesamtausgabe: " + "%.2f" % gesamt_ausgaben + " Euro")


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


# # Aufgabe 4 - Zeitumrechnung <a id='Aufgabe4'></a>
# 
# Entwickeln Sie ein Programm, das vom Benutzer die Anzahl der Sekunden einliest und dann die Sekunden in folgendes Zeitformat umrechnet:
# 
# `D:HH:MM:SS`
# 
# `D`, `HH`, `MM`, `SS` stehen für Tage, Stunden, Minuten und Sekunden. Die Stunden, Minuten und Sekunden sollen in der Ausgabe so formatiert werden, dass sie genau zwei Zeichen einnehmen und mit einer `0` beginnen, falls das notwendig sein sollte. Nutzen Sie hierfür die Formatierung `{Variable:0N}` (`N` steht hier für die Anzahl der angezeigten Zeichen) bei der Verwendung von `print`. 
# 
# **Beispiel**
# 
# Benutzereingabe: 124564 (Sekunden)   
# Ausgabe des Programms: `1:10:36:04`
#

# Lösen Sie Aufgabe 4 in dieser Zelle
zeit = float(input("Benutzereingabe: "))

#Benutzereingaben umrechnen
tage = zeit // (24 * 3600)
zeit = zeit % (24 * 3600)
stunden = zeit // 3600
zeit %= 3600
minuten = zeit // 60
zeit %= 60
sekunden = zeit

#Ausgabe mit Formatierung
print("%d:%02d:%02d:%02d" % (tage, stunden, minuten, sekunden))