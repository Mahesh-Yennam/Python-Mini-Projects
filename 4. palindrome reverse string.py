
# 4.Write a Python function that checks whether a word or phrase is palindrome or not.

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, 
# e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .
# replace() method in a string to help out with dealing with spaces. 
# Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.

def revstring(string):
    string = string.replace(' ','')
    temp = string
    revstring=string[::-1]
    # print(revstring)
    if revstring == temp:
        print('It is palindrome string')
    else:
        print('It is not palindrome string')
        

revstring('mahesh')
revstring('race car')