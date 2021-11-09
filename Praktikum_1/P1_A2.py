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
