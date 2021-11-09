# # Aufgabe 4 - Zufällige Bingo Karten <a id='Aufgabe4'></a>
#
# Eine [Bingokarte](https://de.m.wikipedia.org/wiki/Bingo) besteht aus 5 Spalten mit 5 Zahlen. Die Spalten sind mit den Buchstaben `B`, `I`, `N`, `G` und `O` beschriftet. Unter jedem Buchstaben können 15 Zahlen erscheinen. Insbesondere sind die Zahlen, die unter dem `B` erscheinen können, aus dem Ganzzahlbereich `1` bis `15`, die Zahlen, die unter dem `I` erscheinen können, aus dem Bereich `16` bis `30`, die Zahlen, die unter dem `N` erscheinen können, aus dem Bereich `31` bis `45`, und so weiter.
#
# Entwickeln Sie ein Programm, das eine zufällige Bingokarte erstellt und in einem `dictionary` speichert. Die
# Schlüssel sind die Buchstaben `B`, `I`, `N`, `G` und `O`. Die Werte sind die Listen (`list`), welche die 5 Zahlen enthalten, die unter jedem Buchstaben stehen. Ihr Programm soll dann die generierte Bingokarte mit den entsprechend beschrifteten Spalten anzeigen.
#
# Bei jedem Aufruf Ihres Programms soll eine neue, zufällig generierte Bingo-Karte angezeigt werden. Sie sollen zur Erzeugung der Zufallszahlen die Funktion `randrange` verwenden, die Sie vorher über den Aufruf `from random import randrange` importieren müssen. Die nächste Codezelle übernimmt diesen Import für Sie und zeigt Ihnen den sogenannten `Docstring` dieser Funktion an, der Ihnen bei der Verwendung dieser Funktion helfen sollte.
#
# Die Ausgabe einer zufällig generierten Bingo-Karte sollte so aussehen (nutzen Sie f-Strings und formatieren die Zahlen geeignet):
# ```
#  B  I  N  G  O
# 14 24 33 51 67
#  1 18 39 53 68
# 11 21 44 48 62
# 15 16 38 49 61
#  5 27 43 55 71
# ```

# In[2]:


from random import randrange

get_ipython().run_line_magic('pinfo', 'randrange')
# Testen Sie in dieser Codezelle anhand einiger Beispiele die Funktionsweise dieser Funktion,
# bevor Sie diese in der nächsten Codezelle in der Hauptlogik Ihres Programms einsetzen.
# Führen Sie z.B.
# randrange(1, 5) # (diese Zeile einfach auskommentieren)
# mehrfach aus und analysieren Sie den Output.


# In[3]:


# Lösen Sie Aufgabe 4 in dieser Zelle
from random import randrange

b_list = []
i_list = []
n_list = []
g_list = []
o_list = []

card = {"B": b_list, "I": i_list, "N": n_list, "G": g_list, "O": o_list, }

for i in range(0,5):
    n = str(randrange(0, 16, 1))
    b_list.append(n)

for i in range(0,5):
    n = str(randrange(15, 31, 1))
    i_list.append(n)

for i in range(0,5):
    n = str(randrange(30, 46, 1))
    n_list.append(n)

for i in range(0,5):
    n = str(randrange(45, 61, 1))
    g_list.append(n)

for i in range(0,5):
    n = str(randrange(60, 76, 1))
    o_list.append(n)

print(f'{"B":>4}' + f'{"I":>4}' + f'{"N":>4}' + f'{"G":>4}' + f'{"O":>4}')

print(f'{b_list[0]:>4}' + f'{i_list[0]:>4}' + f'{n_list[0]:>4}' + f'{g_list[0]:>4}' +f' {o_list[0]:>4}')
print(f'{b_list[1]:>4}' + f'{i_list[1]:>4}' + f'{n_list[1]:>4}' + f'{g_list[1]:>4}' +f' {o_list[1]:>4}')
print(f'{b_list[2]:>4}' + f'{i_list[2]:>4}' + f'{n_list[2]:>4}' + f'{g_list[2]:>4}' +f' {o_list[2]:>4}')
print(f'{b_list[3]:>4}' + f'{i_list[3]:>4}' + f'{n_list[3]:>4}' + f'{g_list[3]:>4}' +f' {o_list[3]:>4}')
print(f'{b_list[4]:>4}' + f'{i_list[4]:>4}' + f'{n_list[4]:>4}' + f'{g_list[4]:>4}' +f' {o_list[4]:>4}' + "\n")

for row in zip(*([key + " "] + (value) for key, value in card.items())):
    print(*row)
