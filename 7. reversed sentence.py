# 7.MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def master_yoda(string):
    word_list=string.split(' ')
    word_list=word_list[::-1]
    ns=''
    for i in word_list:
        ns=ns+' '+i
    return ns.strip()

print(master_yoda('I am home'))
print(master_yoda('We are ready'))