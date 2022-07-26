m='Ayibobo pou tout ayiti'
v='aeiou'
g=list(m)
for i in range(len(g)):
    if g[i] in v:
        g[i-1]="*"
        m="".join(g)
print(m)