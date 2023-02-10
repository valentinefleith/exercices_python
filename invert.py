#Fonction qui inverse les lettres dans un mot

def solution(string):
    invert = ""
    for letter in string :
        invert = letter + invert
    return invert

