# 6.OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald

def old_macdonald(string):
    ns=''
    cnt=0
    for i in string:
        n=string.index(i)
        if n==0 or n==3 and cnt<2:
            ns=ns+i.upper()
            cnt+=1
        else:
            ns=ns+i
    print(ns)

old_macdonald('macdonald')
