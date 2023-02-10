#Fonction qui fait la somme de tous les nombres présents dans une chaine de caractères. Si plusieurs chiffres sont côte à côte, on prend le nombre qu'ils forment.

def sum_of_integers_in_string(s):
    num = "1234567890"
    sum = 0
    current_number = ""
    for char in s :
        if char in num :
            current_number += char
        else :
            if current_number :
                sum += int(current_number)
                current_number = ""
    if current_number :
        sum += int(current_number)
    return sum

