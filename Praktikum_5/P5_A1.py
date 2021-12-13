import os.path
# Lösen Sie Aufgabe 1 in dieser Zelle
PATHS = ['./files/python_1.txt', './files/python_2.txt']
OUTPUT_FILE = './files/cat.txt'

def concatenate(PATHS):

    with open(OUTPUT_FILE, 'w+') as writeFile:
        for file in PATHS:
            with open(file) as inputFile:
                writeFile.write(inputFile.read())
            writeFile.write("\n")
    num_lines = sum(1 for line in open(OUTPUT_FILE))
    return num_lines

PATHS = ['./files/python_1.txt', './files/python_2.txt']
OUTPUT_FILE = './files/cat.txt'

import os.path

assert os.path.isfile(OUTPUT_FILE)
assert concatenate(PATHS) == 16

wiki_count = open(OUTPUT_FILE, 'r').read().count("wikipedia")
assert wiki_count == 2