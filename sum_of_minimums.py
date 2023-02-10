#Fonction qui additionne les minimums de plusieurs sous-listes
def sum_of_minimums(numbers):
    sum = 0
    minimums = []
    for sublists in numbers :
        minimum = sublists[0]
        for number in sublists :
            if number < minimum :
                minimum = number
        sum += minimum
    return sum

sum_of_minimums([ [ 7,9,8,6,2 ], [5,8,7,4,5], [6,3,5,4,3] ])
