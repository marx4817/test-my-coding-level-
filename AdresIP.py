adreIP = input("antre adres ip a: ")
rezilta = 0
rezilta_Final = 0
for i in adreIP:
    if i == ".":
        continue
    else:
        rezilta += int(i)
rezilta_Final = rezilta * int(adreIP[0])
print("pot ki ouve a se pot "+ str(rezilta_Final)+" lan")