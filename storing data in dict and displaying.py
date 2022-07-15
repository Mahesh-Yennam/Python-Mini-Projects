# Mahesh Yennam
# accepting data from the user and storing in the dict

mydict = {}

while True:
    key = input('Enter the Title: ')
    value = input('Enter the Content: ')
    mydict[key]=value
    proceed = input('Do you want to add more y or n: ')
    while proceed.strip().lower() not in ('y','n'):
        print('Invalid Input')
        proceed = input('Do you want to add more y or n: ')
    if proceed.strip().lower()=='y':
        continue
    elif proceed.strip().lower()=='n':
        break
        
print('Data is:',mydict)
