table =[1, 2, 3, 0, 12, 40,90, 5]
maxtab =table[1]
mintab =table[1]
for i in table:
    if i>maxtab:
        maxtab =i
    if mintab>i:
        mintab = i
print("Pi gran vale nan tablo table lan se:", maxtab,  "E pi piti an se:", mintab)