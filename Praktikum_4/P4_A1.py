import string
def morse_code(eingabe):

    #Eingabe vergrößer für Vereinheitlichung
    eingabe = eingabe.upper()
    eingabe = " ".join(eingabe)

    # Sonderzeichen rausfiltern
    eingabe = [zeichen for zeichen in eingabe if zeichen.isalnum()]

    morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

    #mit der Stringbibliothek lassen sich alle benötigten Sachen holen und zusammenführen
    buchst_und_zahlen = list(string.ascii_uppercase) + list(string.digits)
    morse_zeichen_uebersetzung = {k:v for k, v in zip(buchst_und_zahlen, morse)}

    #Wort/Satz übersetzung und zurückgeben
    ergebnis = [morse_zeichen_uebersetzung[k] for k in eingabe if k in morse_zeichen_uebersetzung]
    ergebnis = " ".join(ergebnis)
    return ergebnis

assert morse_code("Hello, World!") == ".... . .-.. .-.. --- .-- --- .-. .-.. -.."
assert morse_code("Hello,World!") == morse_code("hello world")
assert morse_code("123 Eins Zwei Drei") == ".---- ..--- ...-- . .. -. ... --.. .-- . .. -.. .-. . .."
assert morse_code("5") == "....."
assert morse_code("!@#$^&*") == ""