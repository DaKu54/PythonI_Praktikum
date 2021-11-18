# # Aufgabe 1 - Hallo Student! <a id='Aufgabe1'></a>
# Schreiben Sie ein Programm, dass eine Studentin / einen Student nacheinander nach dem Vor-, Nachnamen und der Matrikelnummer fragt und diese dann "ordentlich" formatiert direkt untereinander ausgibt. Das Ausgabeformat sollte dieser Vorgabe entsprechen

#Abfragen der persönlichen Daten mit input
nachname = input("Bitte geben Sie ihren Nachnamen ein: ")
vorname = input("Bitte geben Sie ihren Vornamen ein: ")
matrikelnummer = input("Bitte geben Sie ihren Matrikelnummer ein: ")

print("\n")

#Ausgabe der Daten nacheinander
print(nachname, vorname)
print("Matrikelnummer: " + matrikelnummer)