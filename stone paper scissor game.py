# Mahesh Yennam
# stone paper scissor game

import random

print('Stone Paper Scissors Game')

keywords = ['Stone','Paper','Scissors']

compChoice = random.choice(keywords)

##print(keyword)

chances = 3
chance = 1
userWins = 0
compWins = 0

while chances:
    print('--------------------')
    print('1.Stone\n'
          '2.Paper\n'
          '3.Scissors')
    print('--------------------')
    
    print("Chance:", chance)
    choice = input("Enter your choice: ")
    
    while choice not in ('1','2','3'):
        print('Invalid Input')
        choice = input("Enter your choice: ")
    if choice == '1':
        userChoice = keywords[0]
    elif choice == '2':
        userChoice = keywords[1]
    elif choice == '3':
        userChoice = keywords[2]

    print('---------------------')
    print('Your choice: ', userChoice)
    print('Computer choice: ', compChoice)
    print('---------------------')

    if userChoice == keyword[0] and compChoice == keyword[1]:
        compWins += 1
    elif userChoice == keyword[0] and compChoice == keyword[2]:
        userWins += 1
    elif userChoice == keyword[1] and compChoice == keyword[0]:
        userWins += 1
    elif userChoice == keyword[1] and compChoice == keyword[2]:
        compWins += 1
    elif userChoice == keyword[2] and compChoice == keyword[0]:
        compWins += 1
    elif userChoice == keyword[2] and compChoice == keyword[1]:
        userWins += 1
    else:
        userWins += 0
        compWins += 0

    
        
    chance += 1
    chances -=1

    
    
    
    
