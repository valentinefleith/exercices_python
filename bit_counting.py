#Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number.

def count_bits(n):
    binary_number = ""
    sum = 0
    while n//2 > 0 :
        binary_number = str(n%2) + binary_number
        n = n//2
    binary_number = str(n%2) + binary_number
    
    for number in binary_number :
        if number == str(1) :
            sum += 1
    return sum
