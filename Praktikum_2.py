#!/usr/bin/env python
# coding: utf-8

# # Vorlesung Programmieren I (mit Python)
# 
# ## 2. Praktikum (Ausgabedatum: 25.10.2021)
# 
# **Abgabe**
# 
#  - KI, Gruppe 1: (Busse), dienstags, 14:30 - 17:40, ungerade Wochen, Raum K0 16 
#  - KI, Gruppe 2: (Busse), dienstags, 14:30 - 17:40, gerade Wochen, Raum K0 16 
#  - WIF, Gruppe 2: (Lehner), dienstags, 14:30 - 17:40, gerade Wochen, Raum K0 10 
#  - WIF, Gruppe 3: (Franzke), mittwochs, 10:30 - 14:20, gerade Wochen, Raum K0 16  
#  - WIF, Gruppe 4: (Hilpoltsteiner), dienstags, 08:45 - 12:00, gerade Wochen, Raum K0 16
# 
# **Wintersemester 2021/2022**  

# # Aufgaben
# 
# 
#  - [Aufgabe 1](#Aufgabe1): Summe einzigartiger Ziffern.
#  - [Aufgabe 2](#Aufgabe2): Konzertbesucher. 
#  - [Aufgabe 3](#Aufgabe3): Anagramme.
#  - [Aufgabe 4](#Aufgabe4): Zufällige Bingo Karten.
#  - [Bonusaufgabe 5](#Aufgabe5): Teillisten von Listen.

# # Hinweise zum Praktikum
# 
#  - Sie dürfen die Aufgaben **alleine** oder zu **zweit** bearbeiten und abgeben
#  - Sie dürfen die Aufgaben selbstverständlich auch mit ihren Kommilitonen diskutieren und Ideen austauschen
#      - es ist aber nicht erwünscht, dass Code bzw. Ihre Lösung kopiert oder weitergegeben wird
#      - Programmieren ist wie Radfahren: Sie lernen es nicht vom Zuschauen sondern nur indem Sie es selbst tun
#  - Ihre Lösungen müssen Sie **persönlich** in der Ihnen zugewiesenen Gruppe vorzeigen, d.h. die Lösungen können nicht per E-Mail vorgelegt werden
#  - die Praktikumsaufgaben sollten bis zum Ende der jeweiligen Übungsstunde fertig bearbeitet und abgegeben sein
#  - Sie müssen **5 der 6** Praktika bestehen 
#  - **Kommentieren** Sie Ihren Code 
#      - **Nicht kommentierter** Code kann zum **Nichtbestehen** führen
#      
# <div class="alert alert-block alert-danger">
# <b>Wichtig:</b> Sie sind einer bestimmten <b>Praktikumsgruppe</b> zugewiesen. Ihre Abgaben werden nur in dieser Gruppe akzeptiert. Beachten Sie hierzu die Hinweise auf der <b>Moodle-Kursseite</b>.
# </div>

# # Lernziele
# 
#  - Verwendung von Sets und Dictionaries 
#  - Mengenoperationen mit Sets
#  - erster Umgang mit einfachen bedingten Anweisungen
#  - erster Umgang mit einfachen for-Schleifen
#  - Vergleichsoperatoren bei Listen
#  - Teilbereichsoperatoren

# # Aufgabe 1 - Summe einzigartiger Ziffern.  <a id='Aufgabe1'></a>
# 
# Entwickeln Sie ein Programm, das eine Ganzzahl (Integer) vom Benutzer einliest und die Summe der einzigartigen Ziffern dieser Zahl anzeigt. Wenn der Benutzer zum Beispiel `122344` eingibt, sollte Ihr Programm `1+2+3+4=10` anzeigen. Verwenden Sie die `input`-Funktion, um die Eingabe des Benutzers entgegenzunehmen und geben Sie das Ergebnis auf folgende Weise aus: 
# 
# _Eingabe Benutzer_:  
# 
# `122222233444444`
# 
# _(mögliche) Ausgabe Programm_:  
# 
# `1+2+3+4=10`
# 
# **Hinweis**: Verwenden Sie zur Lösung dieser Aufgabe ein `set` oder ein `dictionary`. Sie dürfen davon ausgehen, dass der Benutzer eine Ganzzahl eingibt. Die Reihenfolge, in der die Ziffern in der Darstellung der Summe ausgegeben werden, ist nicht relevant (beim oberen Beispiel ist also z.B. auch die Ausgabe `4+1+3+2=10` zulässig).

# In[ ]:


# Lösen Sie Aufgabe 1 in dieser Zelle
number = int(input("Eingabe Benutzer:"))
number_set = set()
total = 0
for digit in str(number):
    int(digit)

    if digit in number_set:
        continue
    else:
        number_set.add(digit)

for nums in number_set:
    total=total+int(nums)

print(total)


# # Aufgabe 2 - Konzertbesucher. <a id='Aufgabe2'></a>
# 
# Die Personen in den Listen `concert_A` und `concert_B` haben unterschiedliche Konzerte besucht. 
# 
# ```python
# concert_A = ["Anne", "Michael", "Marco", "Stefanie"]
# concert_B = ["Tobias", "Anne", "Willi", "Maja", "Frodo", "Stefanie"]
# ```
# 
# **Teil 1**:  
# 
# Schreiben Sie ein Programm, dass folgende Fragen mit Hilfe von `set`s und den dazugehörigen Mengenoperationen beantworten kann: 
#  - Welche Personen haben beide Konzerte besucht?
#  - Waren alle Personen, die Konzert A besucht haben, auch bei Konzert B?
#  - Wer war auf Konzert A, aber nicht auf Konzert B? 
#  - Wer war auf Konzert B, aber nicht auf Konzert A?
#  - Wer hat eins der Konzerte besucht?
#  
#  
# Erwartete Ausgabe:
# 
# Auf beiden Konzerten waren folgende Personen: `{Name A, Name X, ...}`    
# Waren alle Personen, die Konzert A besucht haben, auch bei Konzert B? `True` oder `False`     
# Konzert A, aber nicht Konzert B haben besucht: `{Name Y, Name Z, ...}`    
# Konzert B, aber nicht Konzert A haben besucht: `{Name V, Name W, ...}`   
# In einem der Konzerte waren: `{Name M, Name N, ...}`   
# 
# 
# **Teil 2**: 
# 
# Die Besucher von Konzert A (Menge $A$) und Konzert B (Menge $B$) können als Teilmengen der Menge 
# 
# ```python
# omega = {"Maja", "Willi", "Michael", "Frodo", "Anne", "Marco", "Stefanie", "Tobias", "John", "Mary"}
# ```
# 
# angesehen werden. Formulieren Sie $\overline{A \cap B} = \overline{A} \cup \overline{B}$ als boolschen Ausdruck und geben Sie das Ergebnis aus als:   
# 
# `Das Ergebnis des Ausdrucks ist:` `True` oder `False` 
# 
# $\overline{A}$ steht hier für das Komplement von $A$, also für $\Omega \setminus A$.
# 

# In[ ]:


# Lösen Sie Teil 1 von Aufgabe 2 in dieser Zelle
# Lösen Sie Aufgabe 1 in dieser Zelle
concert_A = ["Anne", "Michael", "Marco", "Stefanie"]
concert_B = ["Tobias", "Anne", "Willi", "Maja", "Frodo", "Stefanie"]
a_besucher = "";
b_besucher = "";
beide_konzerte = set()
beide_konzerte_besucht = True
a_aber_nicht_b = set()
b_aber_nicht_a = set()

for a_besucher in concert_A:
    for b_besucher in concert_B:
        if a_besucher==b_besucher:
            beide_konzerte.add(a_besucher)
        if a_besucher in concert_B:
            continue
        else:
            a_aber_nicht_b.add(a_besucher)
            beide_konzerte_besucht = False

        if b_besucher in concert_A:
            continue
        else:
            b_aber_nicht_a.add(b_besucher)

min_ein_konzert = a_aber_nicht_b.union(b_aber_nicht_a)

print("Auf beiden Konzerten waren folgende Personen: ", beide_konzerte)
print("Waren alle Personen, die Konzert A besucht haben, auch bei Konzert B?", beide_konzerte_besucht)
print("Konzert A, aber nicht Konzert B haben besucht:  ", a_aber_nicht_b)
print("Konzert B, aber nicht Konzert A haben besucht: ", b_aber_nicht_a)
print("In einem der Konzerte waren: ", min_ein_konzert)


# In[13]:


# Lösen Sie Teil 2 von Aufgabe 2 in dieser Zelle
omega_ohne_a_und_b = ["John", "Mary"]
komplement_a_b = ["Tobias", "Willi", "Maja", "Frodo", "Michael", "Marco"]


# # Aufgabe 3 - Anagramme.  <a id='Aufgabe3'></a>
# 
# Zwei Wörter sind Anagramme, wenn sie die gleichen Buchstaben enthalten, aber in unterschiedlicher Reihenfolge. 
# 
# Oder, laut [Wikipedia](https://de.wikipedia.org/wiki/Anagramm): Als Anagramm wird eine Buchstabenfolge bezeichnet, die aus einer anderen Buchstabenfolge allein durch Umstellung (Permutation) der Buchstaben gebildet ist. Der Vorgang dieser Umstellung wird als Anagrammieren, in der Kryptographie auch als Transposition bezeichnet. 
# 
# Schreiben Sie ein Programm, dass vom Benutzer nacheinander zwei einzelne Wörter als Eingabe entgegennimmt und dann bestimmt, ob die beiden Wörter Anagramme sind oder nicht. Wir vernachlässigen hierbei die Groß- und Kleinschreibung und werten z.B. auch die Wörter "Ampel" und "Palme" als Anagramme. Die Ausgabe sollte diesen Beispielen entsprechen:
# 
# **Beispiel 1**:
# 
# _Eingabe Benutzer_: 
# 
# String1: `Ampel`    
# String2: `Palme`
# 
# _Ausgabe Programm_:   
# 
# `Ampel und Palme sind Anagramme.` 
# 
# **Beispiel 2**:
# 
# _Eingabe Benutzer_: 
# 
# String1: `Hallo`    
# String2: `Welt`
# 
# _Ausgabe Programm_:   
# 
# `Hallo und Welt sind keine Anagramme.`
# 
# **Hinweis**: Sie dürfen die Funktion `sorted` verwenden.

# In[ ]:


# Führen Sie diese Zelle aus, um den 'Docstring' der sorted Funktion zu sehen
get_ipython().run_line_magic('pinfo', 'sorted')


# In[ ]:


# Lösen Sie Aufgabe 3 in dieser Zelle
s1=input("String1: ")
s2=input("String2: ")
print("\n")

s1_lower = s1.lower()
s2_lower = s2.lower()

if(sorted(s1_lower)==sorted(s2_lower)):
      print(s1 + " und " + s2 + " sind Anagrame")
else:
      print(s1 + " und " + s2 + " sind  keine Anagrame")


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


# # Bonusaufgabe 5 - Teillisten von Listen. <a id='Aufgabe5'></a>
# 
# <div class="alert alert-block alert-danger">
# <b>Wichtig:</b> Diese Aufgabe muss nicht bearbeitet werden, um den Leistungsnachweis für dieses Aufgabenblatt zu erreichen. Sie ist optional. </b>
# </div>
# 
# Eine Teilliste ist eine Liste, die einen Teil der Elemente einer größeren Liste enthält.  Eine Teilliste darf ein Element, mehrere Elemente oder gar kein Element enthalten. Eine leere Liste ist immer eine Teilliste jeder Liste. Die Liste selbst ist auch immer eine Teilliste von sich selbst. Es kommt bei den Teillisten aber auf die Reihenfolge der Elemente an. 
# 
# `[2, 3]` ist eine Teilliste von `l=[1, 2, 3, 4]`, aber `[1, 4]` ist keine Teilliste davon, weil die Elemente `1` und `4` nicht aufeinanderfolgen in Liste `l`. 
# 
# Schreiben Sie ein Programm, dass alle Teillisten einer vorgegebenen Liste bestimmen und ausgeben kann. 
# 
# Beispiele:
# 
# ```python
# l = [1, 2, 3]
# ```
# 
# Alle Teillisten:
# ```python
# [], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]
# ```

# In[ ]:


# Lösen Sie Aufgabe 5 in dieser Zelle und testen Sie Ihren Code mit den vorgegebenen 3 Listen 

l = [1, 2, 3]
# l = ["a", "b", "c", "d"]
# l = [["a", "b"], [1, 2]]

