import random
choix = ["salade", "lune", "patate", "hiver", "ourson", "pingouin", "fleur", "amérique", "bateau", "neige"]
mot = random.choice(choix)

#mot = input("Entrez votre mot à deviner : ")
guess = ""
attempt = 8
lettres_donnees = ""
for letter_num in mot :
    guess += "_"

print("Bienvenue dans le jeu du pendu !")

while "_" in guess :
    print("Mot à deviner : " + guess)
    lettre = input("Entrez une lettre : ")
    indexes = []
    i = 0
    if len(lettre) > 1 :
        print("Attention, vous ne pouvez rentrer qu'une lettre à la fois.")
    elif len(lettre) == 0 :
        print("Veuillez proposer une lettre.")
    elif lettre.upper() in lettres_donnees or lettre in guess :
        print("Vous ne pouvez pas saisir plusieurs fois la même lettre.")
    elif lettre in mot :
        for i in range(len(mot)) :
            if lettre in mot[i:] :
                indexes.append(mot[i:].index(lettre) + i)
                i = indexes[-1] + 1
        for index in indexes :
            guess = guess[: index] + lettre + guess[index + 1:]
    elif lettre not in mot :
        attempt -= 1
        if attempt > 0 :
            lettres_donnees += (lettre.upper() + " | ")
            print("Votre lettre n'est pas dans le mot ! Nombre de tentative restantes : " + str(attempt))
            print("Voici les lettres que vous avez déjà essayées : " + lettres_donnees)
        else : 
            print("Vous avez perdu ! Le mot était : " + mot)
            break
if guess == mot :
    print("Vous avez gagné ! le mot était : " + mot)
