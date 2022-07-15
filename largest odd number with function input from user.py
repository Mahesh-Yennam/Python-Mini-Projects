def largest_odd():
    li = []

    counts = 5
    while counts:
        n = int(input("Enter a number: "))
        li.append(n)
        counts -= 1

    largest_odd = li[0]

    for i in li:
        if i > largest_odd and i%2!=0:
            largest_odd = i
            
    return largest_odd

print(largest_odd())
    
