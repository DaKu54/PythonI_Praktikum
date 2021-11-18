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

#Zwei Strings als Input
s1=input("String1: ")
s2=input("String2: ")
print("\n")

#Strings als Lowercase, um Vergleichbarkeit zu gewährleisten
s1_lower = s1.lower()
s2_lower = s2.lower()

#Beide Stringe mit sorted-Funktion vergleichen
if(sorted(s1_lower)==sorted(s2_lower)):
      print(s1 + " und " + s2 + " sind Anagrame")
else:
      print(s1 + " und " + s2 + " sind  keine Anagrame")

