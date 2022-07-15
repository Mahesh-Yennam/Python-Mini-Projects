# Mahesh Yennam 
# print 1 to 100 if
# multiple of 3 print Fizz
# multiple of 5 print Buzz
# multiple of both print FizzBuzz

for i in range(1,100+1):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)
