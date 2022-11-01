def BinaryConverter(x, n = 2):
    l = []
    while x > 0:
        l.append(x%n)
        x = x//n
    
    l.reverse()
    return l

def Binary_Fraction(x):

    whole = int(x)
    dec = x - int(x)

    l = []
    while whole > 0:
        l.append(whole%2)
        whole = whole//2
    l.reverse()

    whole_f = 0
    for i in range(0, len(l), 1):
        whole_f += l[i]*10**(i)

    m = []
    while dec < 1:
        m.append(dec%2)
        dec = dec*2
    m.reverse()

    dec_n = 0
    for i in range(0, len(m), 1):
        dec_n += m[i]*10**(-i)

    print(whole_f, dec_n)

print(Binary_Fraction(85.125))

