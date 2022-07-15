# 3.Write a Python function to multiply all the numbers in a list.

# Sample List : [1, 2, 3, -4]
# Expected Output : -24

mylist = [1, 2, 3, -4]

def prolist(list1):
    product = 1
    for i in list1:
        product *= i 
    print(product)

prolist(mylist)
