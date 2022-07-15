li = []

counts = 5
while counts:
    n = int(input("Enter a number: "))
    li.append(n)
    counts -= 1

odd = []
for i in li:
    if i%2!=0:
        odd.append(i)
        
largest_odd = odd[0]

for i in odd:
    if i > largest_odd:
        largest_odd = i

print(largest_odd)
    
