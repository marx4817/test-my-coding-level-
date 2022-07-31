try:
    non1 =int(input("Antre yon nonb antye: "))
    non2 =int(input("Antre yon 2e nonb antye: "))
    if non2 % 2==0:
        b = non2 // non1
        b //=2
    else:
        b = non2 / non1
        b /=2
    print(b)
except ValueError:
    print("Ou pa antre yon non antye")

