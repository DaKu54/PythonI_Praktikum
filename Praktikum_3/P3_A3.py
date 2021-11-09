# Lösen Sie Aufgabe 3 in dieser Zelle
def ggt(m, n):
    if m==0:
        return n
    else:
        p = n % m
        return ggt(p, m)
