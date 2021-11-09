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