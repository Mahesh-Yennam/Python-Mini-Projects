# 2.Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

list1 = [1,1,1,1,2,2,3,3,3,3,4,5]

# def newlist(oldlist):
#     n_list = set(oldlist)

#     new_list = list(n_list)

#     print(new_list)

# newlist(list1)

# alternate way with for loop

def newlist(oldlist):
    new_list = []

    for i in oldlist:
        if i not in new_list:
            new_list.append(i)
        
    print(new_list)

newlist(list1)