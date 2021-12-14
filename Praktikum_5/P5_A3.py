import re
ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ"

def read_words(file_path):
    #Datei öffnen mit utf8 because of Sonderzeichen und alles uppercase setzen
    with open(file_path, encoding='utf8') as f:
        words = f.read().upper()
    #Ziffern und Unterstriche entfernen
    words = re.sub(r'[0-9_]','', words)
    #Alle Buchstaben finden
    words = re.findall(r'\w+',words)
    return words

def least_used_letter(file_to_investigate):
    cleaned = read_words(file_to_investigate)
    #Dictionary anlegen
    d = dict.fromkeys(ALPH, 0)
    #Wörter durchlaufen
    for word in cleaned:
        #set für die einzigartigen Buchstaben anlegen
        unique = set(word)
        for i in unique:
            d[i] += 1
    num_words = len(cleaned)
    #least used letter herausfinden
    smallest = min(d, key=d.get)
    count = d[smallest]
    return smallest, (count/num_words) * 100

FILE_PATH = './files/words.txt'
ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ"

read_words(FILE_PATH)

assert len(read_words(FILE_PATH)) == 146
assert ALPH in read_words(FILE_PATH)
char, percent = least_used_letter(FILE_PATH)
assert char == 'J'
assert 2.0 < percent < 2.1
assert least_used_letter('./files/python_2.txt')[0] == 'Q'