a =input("antre yon nonb: ")
b =input("antre yon 2e non: ")

if a.isdigit() and b.isdigit():
    nonb1, nonb2 = a, b
try:
    if nonb1> nonb2:
        print(nonb1)
    else: 
        print(nonb2)
except(NameError):
    print("ou pa antre yon nonb")