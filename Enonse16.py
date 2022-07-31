import string


def dekrip(a):
    alfabet = string.ascii_uppercase
    mo =""
    ma=""
    dek = a.split(" ")
    for s in dek:
        if s[0]==">":
            for i in range(27):
                if s[1:3].isdigit():
                    if i == int(s[1:3]):
                        c= s
                        b= alfabet.index(c[3])
                        mo += alfabet[b+int(s[1:3])]
                else:
                    if i == int(s[1]):
                        c= s
                        b= alfabet.index(c[2])
                        mo += alfabet[b+i]
        elif s[0]=="<":
            for i in range(27):
                if s[1:3].isdigit():
                    if i == int(s[1:3]):
                        c= s
                        b= alfabet.index(c[3])
                        mo += alfabet[b-int(s[1:3])]
                else:
                    if i == int(s[1]):
                        c= s
                        b= alfabet.index(c[2])
                        mo += alfabet[b-i]
    return mo



print(dekrip(">5K <0Y <3W <3K <6U <3Q"))

