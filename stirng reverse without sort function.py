# wap to sort the characters in the string in decending or ascending order

s='Python Programming'
ns=''
ds=''
# to print the string in ascending order
for i in range(ord('a'),ord('z')+1):
    for j in s:
        if ord(j.lower())==i:
            ns=ns+j
print('String in ascending order:',ns)

# to print the string in descending order
for i in range(ord('z'),ord('a')-1,-1):
    for j in s:
        if ord(j.lower())==i:
            ds=ds+j
print('String in descending order:',ds)
