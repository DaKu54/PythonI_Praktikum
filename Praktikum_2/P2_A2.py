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

#For-Schleife um die Besucher von Konzert A durchzuiterieren
for a_besucher in concert_A:
    #Noch eine um auch die Besucher von Konzert B durchzuiterieren
    for b_besucher in concert_B:
        #Falls die beiden Besucher übereinstimmen, zu dem set hinzufügen
        if a_besucher==b_besucher:
            beide_konzerte.add(a_besucher)
        if a_besucher in concert_B:
            continue
        else:
            a_aber_nicht_b.add(a_besucher)
            beide_konzerte_besucht = False
        #Einzigartige Besucher von Konzert B suchen
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
