def largest_odd(*args):
    li = args

    largest_odd = li[0]

    for i in li:
        if i > largest_odd and i%2!=0:
            largest_odd = i
            
    return largest_odd

print(largest_odd(2,6,7,11,8,9))
    
