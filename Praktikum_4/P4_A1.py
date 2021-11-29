import string
def morse_code(eingabe):
    eingabe = eingabe.lower()
    eingabe = [zeichen for zeichen in eingabe if zeichen.isalnum()] #isalpha() sind nur buchstaben
    eingabe = " ".join(eingabe)
    print(eingabe)
    morse_code = ".-,-...,-.-.,-..,.,..-.,--.,....,..,.---,-.-,.-..,--,-.,---,.--.,--.-,.-.,...,-,..-,...-,.--,-..-,-.--,--..,-----,.----,..---,...--,....-,.....,-....,--...,---..,----."
    morse_code = morse_code.split(",")
    let_dig= list(string.ascii_lowercase) + list(string.digits)
    dictionary = {k:v for k, v in zip(let_dig, morse_code)}
    vergleich = [dictionary[k] for k in eingabe if k in dictionary]
    vergleich = " ".join(vergleich)
    return vergleich

assert morse_code("Hello, World!") == ".... . .-.. .-.. --- .-- --- .-. .-.. -.."
assert morse_code("Hello,World!") == morse_code("hello world")
assert morse_code("123 Eins Zwei Drei") == ".---- ..--- ...-- . .. -. ... --.. .-- . .. -.. .-. . .."
assert morse_code("5") == "....."
assert morse_code("!@#$^&*") == ""