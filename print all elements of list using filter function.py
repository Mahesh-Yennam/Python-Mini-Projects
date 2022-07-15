# print all elements of list using user-defined and filter function 
li = [1,2,3,6,4]

def m(n):
    return True

f = list(filter(m,li))
print(f)

# print all elements of list using lambda and filter function 
d = lambda x: 1==1
##print(d(5)) # gives True

k = [1,2,3,4,5]

f = list(filter(d,k))
print(f)
