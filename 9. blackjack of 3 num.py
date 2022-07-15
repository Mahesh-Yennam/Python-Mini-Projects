# 9.BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def blackjack(a,b,c):
    sum=a+b+c
    if sum<=21:
        return sum
    elif sum>21:
        if a==11 or b==11 or c==11:
            sum-=10
            if sum>21:
                return 'BUST'
        return sum

print(blackjack(5,6,7)) # 18 less than 21
print(blackjack(9,9,9)) # 27 as no ll so output will be 27 only
print(blackjack(9,9,11)) # 29 as 11 there 29-10=19 
print(blackjack(11,11,11)) # 33 as 11 there 33-10=23 still greater than 21 so bust


