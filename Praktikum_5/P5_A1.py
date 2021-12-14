import os.path
# Lösen Sie Aufgabe 1 in dieser Zelle
PATHS = ['./files/python_1.txt', './files/python_2.txt']
OUTPUT_FILE = './files/cat.txt'

def concatenate(PATHS):
    #Datei öffnen mit w+ um reinzuschreiben
    with open(OUTPUT_FILE, 'w+') as writeFile:
        #Schleife über die Dateien in die Liste
        for file in PATHS:
            #beide Dateien öffnen
            with open(file) as inputFile:
                #reinschreiben was aus dem input-File gelesen wird
                writeFile.write(inputFile.read())
            #nach jeder Zeile einen Umbruch
            writeFile.write("\n")
    #mit sum jeweils um eins raufaddieren um die Gesamtanzahl
    #der Zeilen zu lesen
    num_lines = sum(1 for line in open(OUTPUT_FILE))
    return num_lines

PATHS = ['./files/python_1.txt', './files/python_2.txt']
OUTPUT_FILE = './files/cat.txt'

import os.path

assert os.path.isfile(OUTPUT_FILE)
assert concatenate(PATHS) == 16

wiki_count = open(OUTPUT_FILE, 'r').read().count("wikipedia")
assert wiki_count == 2