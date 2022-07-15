# print table of given number with function and without for and while loop


# using map and lambda function
def table(n):
    t = list(map(lambda x:x*n,range(1,11)))
    #print(t)
    for i in t:
        print(i)

table(5)


# using default argument and recusion
##def table(n,i=1):
##    if i>10:
##        return
##    print(n*i)
##    return table(n,i+1)
##
##table(5)
