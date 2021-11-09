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