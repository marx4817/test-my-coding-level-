from localStoragePy import localStoragePy
localStorage = localStoragePy('Chrome', "sqlite")
item ="Chrome"
b=localStorage.getItem(item)
print(b)