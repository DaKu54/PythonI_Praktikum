# Lösen Sie Aufgabe 1 in dieser Zelle
PATHS = ['./files/python_1.txt', './files/python_2.txt']
OUTPUT_FILE = 'cat.txt'
OUTPUT_FILE_PATH = './files/' + OUTPUT_FILE

def concatenate(PATHS):
    readFiles = ['firstFile.txt', 'secFile.txt']

    with open(OUTPUT_FILE_PATH, 'w+') as writeFile:
        for file in readFiles:
            with open(file) as inputFile:
                writeFile.write(inputFile.read())
            writeFile.write("\n")
    num_lines = sum(1 for line in open('cat.txt'))

    return num_lines

PATHS = ['./files/python_1.txt', './files/python_2.txt']
OUTPUT_FILE = 'cat.txt'

import os.path

print(OUTPUT_FILE_PATH)

assert os.path.isfile(OUTPUT_FILE)
assert concatenate(PATHS) == 16

wiki_count = open(OUTPUT_FILE, 'r').read().count("wikipedia")
assert wiki_count == 2