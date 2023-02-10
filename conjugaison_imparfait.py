#Conjugue à l'imparfait une entrée de la forme "Pronom + verbe à l'infinif". Ne prend pas en compte l'ajout de voyelles (type je mangeais) ni le verbe être.


def to_imparfait(verb_phrase):
    verb_phrase = verb_phrase[0:len(verb_phrase)-2]
    if verb_phrase.startswith("Je") or verb_phrase.startswith("Tu") :
        verb_phrase += "ais"
    elif verb_phrase.startswith("Il") and verb_phrase[2] == " " :
        verb_phrase += "ait"
    elif verb_phrase.startswith("On") :
        verb_phrase += "ait"
    elif verb_phrase.startswith("Elle") and verb_phrase[4] == " " :
        verb_phrase += "ait"
    elif verb_phrase.startswith("Nous") :
        verb_phrase += "ions"
    elif verb_phrase.startswith("Vous") :
        verb_phrase += "iez"
    elif verb_phrase.startswith("Ils") or verb_phrase.startswith("Elles") :
        verb_phrase += "aient"
    return verb_phrase

