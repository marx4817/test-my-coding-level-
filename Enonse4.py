import Fomataj
a=2
b=3
bonMin =1
bonMax =20
v=0
m =0
for i in range(1, 21):
    if i % a == 0 and i % b != 0:
        print(i, end=",")
        v +=1
print("-> total nonb "+ str(v))
for i in range(1, 21):
    if(i % b == 0 and i % a != 0):
        print(i, end=",")
        m +=1
print("-> total nonb "+ str(m))
m=0
for i in range(1, 21):
    if(i % b == 0 and i % a == 0):
        print(i, end=",")
        m +=1
print("-> total nonb "+ str(m))
m=0
for i in range(1, 21):
    if(i % b != 0 and i % a != 0):
        print(i, end=",")
        m +=1
print("-> total nonb "+ str(m))