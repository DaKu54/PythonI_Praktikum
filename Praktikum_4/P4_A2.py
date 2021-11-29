
def filter_alphanumeric(string):
    import re

    string = re.sub('\W+' ,' ', string  )  # es wird nach allen nicht Alphanumerischen Zeichen(Sondernzeichen) im String gesucht und entfernt
    # und Wörter dann mit ' ' getrennt
    # return string
    leerset = set()
    for i in string:
        longest_word = max(string.split(" ") ,key=len)
        leerset.update([longest_word])
        return (len(longest_word) ,leerset)

test3 = "HEute heute ist , das Wetter schön schoen !!!!!!"

filter_alphanumeric(test3)
# longest_word(test3) #== (6, {'Wetter', 'schoen'})

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
filter_alphanumeric(test3)