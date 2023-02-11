def fibonacci_sequence(n) :
    sequence = [0, 1]
    if n < 1 :
        print("Il faut au moins un chiffre dans la suite.")
        return
    elif n < 3 :
        return sequence[:n]
    else :
        for i in range(n-2) :
            sequence.append(sequence[i]+sequence[i+1])
    return sequence




