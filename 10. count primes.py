# 10.COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25

def count_primes(n):
    primes=0
    for i in range(1,n+1):
        cnt=0
        for j in range(1,i+1):
            if i%j==0:
                cnt+=1
        if cnt==2:
            primes+=1
    return primes

print(count_primes(100))
    
