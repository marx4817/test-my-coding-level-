v="5 45 123 12"
a=v.split(" ")
n=1
for i in a:
    #print(i)
    b=0
    for h in i:
        b +=int(h)
    n *= b
print(n)
         