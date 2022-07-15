# Mahesh Yennam
# number guess mini project

a=5
print('--------------------------------------------')
print('You have 3 guesses')
n=int(input('Guess a number between 1 to 10: '))
cnt=3
while True:
    if n==a and cnt>0:
        print('You got it')
        break
    elif n!=a and cnt>1:
        print('Not the correct guess')
        print('--------------------------------------------')
        cnt-=1
        if cnt==1:
            print('You have {} guess left'.format(cnt))
        else:
            print('You have {} guesses left'.format(cnt))
        n=int(input('Guess a number between 1 to 10: '))
    else:
        print('Not the correct guess')
        print('--------------------------------------------')
        print('You are out off guesses')
        break

