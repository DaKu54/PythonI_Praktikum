# Lösen Aufgabe 1 in dieser Zelle

def center(zeichenkette, abstand):
    zentriert = zeichenkette.center(abstand).rstrip()

    return zentriert

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

# Lösen Sie Aufgabe 3 in dieser Zelle
def ggt(m, n):
    if m==0:
        return n
    else:
        p = n % m
        return ggt(p, m)

# Lösen Sie Aufgabe 3 in dieser Zelle
L1 = ['P', 3, 'y', 't', 0.0, 'h', 1, 1, 1.0, 'o', 'n' ]

def cleaner(liste):
    bereinigt = []
    for x in liste:
        print(x)
        if isinstance(x, int) or isinstance(x, float):
            continue
        else:
            bereinigt.append(x)
    return bereinigt

def palindrom(liste):
    cleaner(liste)
    zusammen = ''.join(liste)
    return zusammen

palindrom(L1)