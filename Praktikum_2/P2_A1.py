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

#Eingabe der Zahl mit Input und als Integer
number = int(input("Eingabe Benutzer:"))

#Set für die einzigartigen Zahlen
number_set = set()

#Variable für die SUmme
total = 0

#For-Schleife zum iterieren der Eingabe
for digit in str(number):
    int(digit)

    #Überprüfung ob die Zahl bereits im Set vorhanden ist
    if digit in number_set:
        continue
    else:
        number_set.add(digit)

#Iterieren durch das Set für die Summe
for nums in number_set:
    total=total+int(nums)

#Ausgabe der Summe
print(total)
