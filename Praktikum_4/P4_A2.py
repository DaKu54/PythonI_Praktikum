import re

def filter_alphanumeric(eingabe):
    #Alphanummerische Zeichen mit Regex rausfiltern und zurückgeben
    eingabe = re.sub('\W+', ' ', eingabe)
    return eingabe

def longest_word(eingabe2):
    #Alphanum Zeichen rausfiltern und in eine Liste aufsplitten
    gefiltert = filter_alphanumeric(eingabe2)
    word_list = gefiltert.split()

    #Variable, um die maximale Laenge eines Wortes zu finden
    max_len = len(max(word_list, key=len))
    #Alle Wörter mit der maximalen Laenge rausfiltern
    max_words = {word for word in word_list if len(word)==max_len}

    return (max_len, max_words)

test1 = """
Python ist eine universelle, \t \t üblicherweise interpretierte, 
höhere Programmiersprache. Sie hat den Anspruch, einen gut lesbaren, 
knappen Programmierstil zu fördern. \n
So werden beispielsweise Blöcke nicht durch geschweifte Klammern, 
sondern durch Einrückungen strukturiert. \n
Quelle: Wikipedia, Programmiersprache, Python
"""

test2 = """
Implementieren Sie die Funktion longest_word die in einem Inputstring das längste Wort 
(es können mehrere Wörter die gleiche Länge haben) findet und diese maximale Länge als auch alle 
Wörter, die diese Länge haben, in einer Liste als Rückgabewert ausgibt.
Sie dürfen jeder Gruppe von Zeichen, die kein Leerzeichen sind, als Wort interpretieren, 
sogar wenn diese Zahlen oder Satzzeichen sind.
"""

test3 = "HEute heute ist , das Wetter schön schoen !!!!!!"

assert longest_word(test1) == (18, {'Programmiersprache'})
assert longest_word(test2) == (14, {'Implementieren', 'interpretieren'})
assert longest_word(test3) == (6, {'Wetter', 'schoen'})