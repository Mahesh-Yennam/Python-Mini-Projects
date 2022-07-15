# Mahesh Yennam
# Game - Guess the Number

import random

randomNumber = random.randrange(1,10)

print('Select a number between 1 to 9')
print('You have Three chances')
print('-----------------------------')
chances = 3
c = 1
while chances:
    print('Chance:',c)
    choice = input('Enter your Choice: ')

    if choice == randomNumber:
        print('Correct')
        print('-----------------------------')
    else:
        print('Incorrect')
        print('-----------------------------')
    chances -= 1
    c += 1
else:
    print('Out of guesses') 
    print('Correct Number is:', randomNumber)
    print('Play again!!!')
        


        
    
