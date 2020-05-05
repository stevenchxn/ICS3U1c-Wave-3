next = integer = int(input("Enter an integer that is 2 or greater: "))
factor = 2
print (f"The prime factors of {integer} are: ")

while factor <= next:
    if next % factor == 0:
        next = (next / factor)
        print (factor)
    else:
        factor += 1