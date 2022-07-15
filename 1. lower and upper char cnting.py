##1.Write a Python function that accepts a string and calculates the number of upper case letters
##and lower case letters.
##Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
##Expected Output : 
##No. of Upper case characters : 4
##No. of Lower case Characters : 33

string = 'Hello Mr. Rogers, how are you this fine Tuesday?'

def ulchar(str):
    ucnt=0
    lcnt=0
    for i in str:
        if ord(i) in range(ord('A'),ord('Z')+1):
            ucnt+=1
        elif ord(i) in range(ord('a'),ord('z')+1):
            lcnt+=1
    print('No. of Upper case characters:', ucnt)
    print('No. of lower case characters:', lcnt)

ulchar(string)

