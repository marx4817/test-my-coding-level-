import string


def dekrip(a):
    alfabet = string.ascii_uppercase
    mo =""
    ma=""
    dek = a.split(" ")
    for s in dek:
        if s[0]==">":
            for i in range(27):
                if i == int(s[1]):
                    c= s
                    b= alfabet.index(c[2])
                    mo += alfabet[b+i]
        elif s[0]=="<":
            for i in range(27):
                if i == int(s[1]):
                    c= s
                    b= alfabet.index(c[2])
                    mo += alfabet[b-i]
    return mo



print(dekrip("<1T >7H >3C <5Y >13J <2C <5W >4A"))

