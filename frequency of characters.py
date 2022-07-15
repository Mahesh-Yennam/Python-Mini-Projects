# wap to print frequency of characters in the string to dictionary

s='pythin programming'
d={}

for i in s:
    if i==' ':
        continue
    d[i]=s.count(i)

print(d)
