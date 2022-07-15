# wap to count alphabers, digits and special symbols in ther string

string='maheshyennam12321#@$#'
#print(len(string))
char=0
digit=0

for alphabet in range(ord('a'),ord('z')+1):
    for letter in string:
        if ord(letter.lower())==alphabet:
            char=char+1
        if letter in range(0,10):
            num+=1
for num in range(0,10):
    for letter in string:
        if letter == str(num):
            digit+=1

print('alphabets in the string:',char)
print('digits in the string:',digit)
print('special characters in the string:',len(string)-char-digit)
