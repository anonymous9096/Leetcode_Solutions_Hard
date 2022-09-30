def CCBN(n):
    digit = n
    binofD = ""
    for i in range(1, digit+1):
        # binDecimal = "".join(bin(i)).replace("b", "")
        binofD+=format(i, "b")

    modulo = (10**9 +7)
    final = int(binofD, 2) % modulo
    return print(final)

if __name__=="__main__":
    nint = 12
    CCBN(nint)