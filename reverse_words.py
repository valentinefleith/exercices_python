#Fonction qui inverse les lettres dans une chaine de caractères

def reverse_words(s):
    sentence = s.split()
    sentence.reverse()
    reversed_sentence = ""
    for word in sentence :
        reversed_sentence = reversed_sentence + word + " "
    reversed_sentence.strip()
    return reversed_sentence

