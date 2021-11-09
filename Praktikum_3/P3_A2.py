# Lösen Sie Aufgabe 2 in dieser Zelle
import re

rexes = ('[A-Z]', '[a-z]', '[0-9]')

boolcheck = False

def check_password(password):
    if (len(password) >= 8 and all(re.search(r, password) for r in rexes)):
        boolcheck = True
        return boolcheck
    else:
        boolcheck = False
        return boolcheck