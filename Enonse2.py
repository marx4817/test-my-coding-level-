n =input("Antre yon non antye: ")
if n.isdigit():
    b= int(n)
    if b % 4 ==0:
        print("NOK")
    else:
        print("OK")