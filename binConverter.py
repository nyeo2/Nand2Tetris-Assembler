def dectobin(dec):
    if type(dec) != int:
        dec = int(dec)
    final = ''
    while dec != 0:
        final = str(dec % 2) + final
        dec //= 2
    
    return final

def bintodec(bina):
    binal = []
    final = 0
    for char in bina:
        binal.append(int(char))
    
    expt = 0
    while binal:
        final += binal.pop() * (2 ** expt)
        expt += 1
    return final
