number =input("antre yon nonb: ")

if number.isdigit():
    number1 =int(number)
try:
    lis =[i for i in range(number1)]
    lis1 =[]
    a =1
    for i in range(len(lis)):
        a +=1
        if i ==0:
            lis=lis[::-1]
            n=lis[-1]
            lis1.insert(0, n)
        else:
            del lis[-1]
            lis=lis[::-1]
            n=lis[-1]
            lis1.insert(0, n)
    print(lis1)
except NameError:
    print("Ou pa antre yon nonb")

try:
    b= int(input("Antre yon nonb wap cheche ak index li a: "))
except ValueError:
    print("Ou dwe antre yon nonb antye")

for i in lis1:
    if i==b:
        print("nonb wap cheche a se: "+str(i)+" index li se: " + str(lis1.index(i)))