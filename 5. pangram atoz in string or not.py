# 5.Write a Python function to check whether a string is pangram or not. 
# (Assume the string passed in does not have any punctuation)

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

string = "The quick brown fox jumps over the lazy dog"

def pangrams(string):
    cnt=0
    for i in range(ord('a'),ord('z')+1):
        # print(chr(i))
        if chr(i) in string.lower():
            cnt+=1
    if cnt==26:
        print('it is pangrams')
    else:
        print('it is not a pangrams')

pangrams(string)

