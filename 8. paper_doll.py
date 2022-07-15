# 8.PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(string):
    ns=''
    for i in string:
        ns=ns+i*3
    return ns

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))
