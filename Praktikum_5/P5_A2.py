def add_line_numbers(file_to_add_line_numbers):
    #erster File-Stream um alle Zeilen rauszulesen
    with open(file_to_add_line_numbers, 'r') as program:
        data = program.readlines()

    #zweiter Filestream um die Zeilen mit Nummern reinzuschreiben
    with open(file_to_add_line_numbers, 'w') as program:
        for (number, line) in enumerate(data):
            program.write('%d  %s' % (number + 1, line))


s = """Sed ut perspiciatis unde omnis iste natus error sit voluptatem 
accusantium doloremque laudantium,  totam rem aperiam, eaque ipsa quae 
ab illo inventore veritatis et quasi architecto beatae vitae 
dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas 
sit aspernatur aut odit aut fugit, 
sed quia consequuntur magni dolores eos qui ratione 
voluptatem sequi nesciunt. Neque porro quisquam est, 
qui dolorem ipsum quia dolor sit amet, consectetur, 
adipisci velit, sed quia non numquam eius modi tempora 
incidunt ut labore et dolore magnam aliquam quaerat voluptatem. 
Ut enim ad minima veniam, quis nostrum 
exercitationem ullam corporis suscipit laboriosam, 
nisi ut aliquid ex ea commodi consequatur? 
Quis autem vel eum iure reprehenderit qui in ea 
voluptate velit esse quam nihil molestiae consequatur, 
vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?

"""
import os

NUM_LINES = 17
FILE = 'test.txt'

with open(FILE, 'w') as file:
    file.write(s)

add_line_numbers(FILE)

file = open(FILE, 'r')
lines = file.readlines()
assert len(lines) == NUM_LINES
assert lines[0][0] == '1'
assert lines[-1][0:2] == '17'
assert lines[-1][0:3] == '17 '
file.close()

if os.path.isfile(FILE):
    os.remove(FILE)