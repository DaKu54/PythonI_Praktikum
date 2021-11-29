def count_words(liste_strings):
    liste_strings= [str(int) for int in liste_strings]
    dict_strings = {words:liste_strings.count(words) for words in liste_strings}
    return dict_strings


#mit Hilfe einer list-comprehension die Wörter aus dem Benutzerinput herausfiltert, die mit einem Großbuchstaben beginnen
def count_capital_words(*variable):
    variable= list(variable)
    variable= [str(int) for int in variable]
    variable = [zeichen.strip() for zeichen in variable]
    variable = [zeichen for zeichen in variable if zeichen.istitle()]
    variable = [zeichen for zeichen in variable if zeichen[0].isalpha()]
    #return variable
    variable = count_words(variable)
    return variable


count_capital_words(1,"       2", 3)
#count_capital_words("A", "b", "a_B")
count_capital_words("_U", "I_") #== {"I_": 1}
#count_capital_words({1}) == {}