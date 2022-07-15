# created class customer to create an obj of each customer
class customer:
    def __init__(self, name, email, password, address):
        self.name = name
        self.email = email
        self.password = password
        self.address = address

# created a customers list to add the new cutomers
customers = []

def register():
    name = input("Enter your name: ")
    email = input("Enter your email id: ")
    password = input("Enter your password: ")
    address = input("Enter your address: ")
    obj = customer(name, email, password, address)
    customers.append(obj)

def login():
    email1 = input("Enter your email id: ")
    password1 = input("Enter your password: ")
    # print(customers)
    for obj in customers:
        if email1 == obj.email and password1 == obj.password:
            print("Successfully Logged in!!!")
            return True
    else:
        print("Incorrect Email or Password!!!")
        return False 
    
# a prompt to register and login
while True:
    print('----------------------------------')
    print("1) Register\n"
        "2) Login")
    ch = input("Enter your choice: ")
    print('----------------------------------')
    if ch == '1':
        register()
    elif ch == '2':
        res = login()
        if res:
            break
    else:
        print("Invalid input")

# for heading of veg and non-veg items and price 
it = 'Items'
r = 'Rs'

# for heading of the bill
b = 'Bill'
q = 'Qty'
a = 'Amount'
t = 'Total'

# veg dict with name and price
veg = {
    'Veg Manchurian Dry': 90,
    'Mushroom Chilly Dry': 110,
    'Paneer Chilly Dry': 120
}

# adding the veg items and price into list
veg_items = [i for i in veg.keys()]
veg_price = [i for i in veg.values()]

# non-veg dict with name and price
non_veg = {
    'Chicken Manchurian Dry': 130,
    'Chicken Crispy': 140,
    'Chicken Lollypop': 160
}

# adding the non-veg ites and price into list
non_veg_items = [i for i in non_veg.keys()]
non_veg_price = [i for i in non_veg.values()]

# appending the ordered items to the list
ordered_items = []
ordered_price = []
ordered_qty = []

def vegmenu():
    print(f'{it:^28} - {r}')
    cnt = 0
    for k,v in veg.items():
        cnt += 1
        print(f'{cnt}) {k:<25} - {v}')

def nonvegmenu():
    print(f'{it:^28} - {r}')
    cnt = 0
    for k,v in non_veg.items():
        cnt += 1
        print(f'{cnt}) {k:<25} - {v}')

def orderveg(n):
    if veg_items[n] in ordered_items:
        m = ordered_items.index(veg_items[n])
        qty = int(input("Enter the quantity: "))       
        ordered_qty[m] += qty
    else:
        ordered_items.append(veg_items[n])
        ordered_price.append(veg_price[n])
        qty = int(input("Enter the quantity: "))
        ordered_qty.append(qty)

def ordernonveg(n):
    if non_veg_items[n] in ordered_items:
        m = ordered_items.index(non_veg_items[n])
        qty = int(input("Enter the quantity: "))       
        ordered_qty[m] += qty
    else:
        ordered_items.append(non_veg_items[n])
        ordered_price.append(non_veg_price[n])
        qty = int(input("Enter the quantity: "))
        ordered_qty.append(qty)

# a prompt to select veg or non-veg then based on the selection
# the menu of respective is shown to order 
while True:
    print('----------------------------------')
    print("1) Veg Menu\n"
    "2) Non-Veg Menu\n"
    "3) Exit for Bill")
    ch = input('Enter your choice: ')
    print('----------------------------------')
    if ch == '1':
        # displaying the veg menu
        vegmenu()
        ch2 = input("Enter your choice: ")
        if ch2 == '1':                
            orderveg(int(ch2)-1)
        elif ch2 == '2':
            orderveg(int(ch2)-1)
        elif ch2 == '3':
            orderveg(int(ch2)-1)
        else:
            print("Invalid Input")

    elif ch == '2':
        # displaying the non-veg menu
        nonvegmenu()
        ch3 = input("Enter your choice: ")
        if ch3 == '1':
            ordernonveg(int(ch3)-1)
        elif ch3 == '2':
            ordernonveg(int(ch3)-1)
        elif ch3 == '3':
            ordernonveg(int(ch3)-1)
        else:
            print("Invalid Input")
    elif ch == '3':
        break
    else:
        print("Invalid Input")


# generating bill
def bill():
    print(f'{b:^40}')
    print('-------------------------------------------')
    print(f'{it:^28} {r:<4} {q:<4} {t:<5}')
    print('-------------------------------------------')
    cnt = 0
    for i in range(len(ordered_items)):
        cnt += 1
        s = ordered_price[i]*ordered_qty[i]
        print(f'{cnt}) {ordered_items[i]:<25} {ordered_price[i]:<4} {ordered_qty[i]:<4} {s:<5}')

    total = 0
    for i in range(len(ordered_items)):
        total += ordered_price[i]*ordered_qty[i]

    e = ''
    print(f'{e:<32} Total {total:<5}')

bill()
