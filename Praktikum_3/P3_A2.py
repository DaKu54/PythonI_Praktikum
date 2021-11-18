# Lösen Sie Aufgabe 2 in dieser Zelle
import re

#Regular Expressions für die Überprüfung
rexes = ('[A-Z]', '[a-z]', '[0-9]')

#Standardwert für die Überprüfung
boolcheck = False

#Funktion anlegen mit dem Parameter
def check_password(password):
    #Länge überprüfen und mit einer for-schleife alle Regular Expressions prüfen
    if (len(password) >= 8 and all(re.search(r, password) for r in rexes)):
        boolcheck = True
        return boolcheck
    else:
        boolcheck = False
        return boolcheck