# Mahesh Yennam
# Cart mini project

cart_list=list()

def cart_keys():
    print('-------------------------')
    print('1.Add\n'
          '2.Remove\n'
          '3.Clear\n'
          '4.Show\n'
          '5.Quit')
    print('-------------------------')

def add_cart():
    add=input('Enter what do you want to add: ')
    cart_list.append(add)
    print('\nAdded Successfully\n')

def remove_cart():
    remove=input('Enter what do you want to remove: ')
    cart_list.remove(remove)
    print('\nRemoved Successfully\n')

def clear_cart():
    while True:
            clear=input('Clear all y/n: ')
            print()
            if clear=='y':
                cart_list.clear()
                print('Cleared Successfully\n')
                break
            elif clear=='n':
                break
            else:
                print('Invalid Input\n')
                continue

def show_cart():
    print('The list is',cart_list,'\n')

def exit_cart():
    print('Exit Successfully\n')

while True:
    cart_keys()
    ch=input('Select your choice: ')
    print()
    if ch=='1':
        add_cart()
    elif ch=='2':
        remove_cart()
    elif ch=='3':
        clear_cart()
    elif ch=='4':
        show_cart()
    elif ch=='5':
        exit_cart()
        break
    else:
        print('Invalid Input')


