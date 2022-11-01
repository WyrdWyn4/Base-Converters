def converter(number, norm = 10, base = 2, precision = 5):

    # Here, we check if the types are correct or not
    if (type(number) != int and type(number) != float) or type(base) != int or type(norm) != int  or base < 2 or norm < 2:
        return False

    if base == norm:
        return number
    
    # We check if the number is negative
    # If it is, we will make it positive
    # But, we will add a sign in the end
    if number < 0:
        negative = True
        number = abs(number)
    else:
        negative = False

    # Here, we check if we have a decimal number
    if type(number) == float:
        Delta = number - int(number)
        Epsilon = []
    
    # Here, we import the Math Library
    import math

    # Here, we have the codes for Bases from 2 to 63
    Alpha = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E",
             "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", 'h', "i",
             "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
             "y", "z", "_"]

    # This one here is specifically for Base 64
    Alpha_64 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
                "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d",
                "e", "f", "g", 'h', "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7",
                "8", "9", "+", "/",]

    # Converting from base norm to base 10
    # Forgot that alphabets existed
    # smh

    """
    # First, we target the whole numbers
    number = list(str(int(number)))
    number.reverse()

    # We create two lists, for further use
    temp = list()
    Bruh = list()

    # First, we make everything an integer and append to temp
    for i in number:
        temp.append(int(i))

    # Then, we convert that to 
    for i in range(0, len(temp), 1):
        Bruh.append((temp[i]*norm**i))
    
    number = 0
    for i in Bruh:
        number += i

    """

    # Beta is an empty string that we will return in the end
    Beta = str()

    # Gamma is our main list which will store our numbers/characters
    Gamma = []

    # We need to set the length of Gamma here.
    # It will be the largest logarithm
    for i in range(0, int(math.log(number, base)) + 1, 1):
        Gamma.append(0)

    # This is our main indefinite loop
    while True:

        # If the number is lesser than One, we break
        if number < 1:
            break

        # We add 1 to the index first because we will change x
        Gamma[int(math.log(number, base))] += 1

        # int() is used to round the power down
        # We subtract it from the number
        number -= base**int(math.log(number, base))

        # Here we check if the number is 0
        # If so, we break
        if number == 0:
            break
    
    # We need to reverse our list because we started from the larger side
    Gamma.reverse()

    # We convert the numbers to characters
    # We add those to Beta
    for i in Gamma:
        if base == 64: i = Alpha_64[i]
        else: i = Alpha[i]
        Beta += i

    # Now We go for Decimals
    
    # We have to use try-except, because the user might not use decimals
    try:

        # First, we add about 20 spaces to Epsilon
        for i in range(0, precision, 1):
            Epsilon.append(0)                
        
        # This is our main Decimal Loop
        while True:

            # Again, try-except, because we might end up with math error
            # If the number is greater than the precision, we break
            try: 
                if -(math.log(Delta, base)) > precision:
                    break
            except:
                break
            
            # If the log is not a whole number, we add one to the spot
            if (math.log(Delta, base)) == float(int(math.log(Delta, base))):
                Epsilon[(int(math.log(Delta, base)))] += 1
            # Otherwise, we add one to the next spot, because we round up
            else:
                Epsilon[(int(math.log(Delta, base)) - 1)] += 1
            
            # We subtract from the base to the power from Delta
            Delta -= base**(int(math.log(Delta, base)) - 1)

        # We want to remove extra zeroes for precision purposes
        # So, we search for the first non zero
        for i in range(0, len(Epsilon), 1):
            if Epsilon[i] != 0:
                Beta += "."
                break
        
        # We split the list and then reverse it
        Epsilon = Epsilon[i::1]
        Epsilon.reverse()

    except: pass

    # We interchange the numbers with characters
    try:
        for i in Epsilon:
            if base == 64: i = Alpha_64[i]
            else: i = Alpha[i]
            Beta += i
    except:
        pass

    # If the number is smaller than one, we add a zero in front of it
    if Beta[0] == ".":
        Beta = "0" + Beta

    # If the number was negative, we add a sign infront of it
    if negative == True:
        Beta = "-" + Beta

    # We finally return Beta
    return(Beta)

number = 101
norm = 2
base = 10
precision = 20

print(converter(number, norm, base, precision))