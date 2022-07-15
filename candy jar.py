# Mahesh Yennam
# Candy Jar mini project

print('Welcome to Candy Shop')

candies=100

while candies:
    n=int(input('How many Candies do you want: '))
    if n>0 and n<=candies:
        print('Here have it and Visit again')
        candies-=n
    elif n>candies:
        print('Sorry')
        print('Only {} Candies Left'.format(candies))
    else:
        print('Invalid Input')
else:
    print('All Candies are Sold')

