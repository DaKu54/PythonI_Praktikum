def concatenate(liste_strings):
    OUTPUT_FILE = './files/cat.txt'

    with open(OUTPUT_FILE, "r+") as concatwf: #concatwf=concatwritingfile
        for single_string in liste_strings:
            with open(single_string,"r") as alle:
                print(single_string)
                x = concatwf.write(alle.read()),concatwf.write("\n")
                #print(x) ->Outcome: (830, 1)  (1219, 1)?

    with open(OUTPUT_FILE, "w+") as concatwf:
         for lines in concatwf:
            print(concatwf.readlines())

PATHS = ['./files/python_1.txt', './files/python_2.txt']

concatenate(PATHS)