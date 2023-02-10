#Fonction qui affiche le plus grand et le plus petit nombre dans une chaine de caractères.

def high_and_low(number):
    numbers = number.split()
    print(numbers)
    minimum = numbers[0]
    for num in numbers :
        if int(num) < int(minimum) :
            minimum = num
    maximum = numbers[0]
    for num in numbers :
        if int(num) > int(maximum) :
            maximum = num
    return str(maximum) + " " + str(minimum)

