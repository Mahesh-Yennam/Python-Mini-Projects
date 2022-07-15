# Mahesh Yennam
# Pizza Order mini project

print('Our Pizza list')
print('-------------------------------')
print('1. MARGHERITA      - 200 Rs\n'
      '2. FARM HOUSE      - 250 Rs\n'
      '3. PEPPY PANEER    - 300 Rs\n'
      '4. VEGGIE PARADISE - 300 Rs\n'
      '5. CHEESE N CORN   - 500 Rs')
print('-------------------------------')

pizzas={1:'MARGHERITA     ',2:'FARM HOUSE     ',3:'PEPPY PANEER   ',4:'VEGGIE PARADISE',
        5:'CHEESE N CORN  '}
cost={1:200,2:250,3:300,4:300,5:500}
ordered_pizza=[]
ordered_qty=[]
new_order='y'
while True:
    if new_order.lower()=='y':
        pizza=int(input('Select your Pizza number: '))
        if pizza>len(pizzas): # if input out off list
            print('Invalid input')
            continue
        if pizza in ordered_pizza: # for already ordered pizza increment
            qty=int(input('Enter the Quantity: '))
            x=ordered_pizza.index(pizza)
            ordered_qty[x]+=qty
        else:                       # for newly ordered pizza 
            ordered_pizza.append(pizza)
            qty=int(input('Enter the Quantity: '))
            ordered_qty.append(qty)
        new_order=input('Do you wish to order another pizza y/n: ')
    elif new_order.lower()=='n':
        break
    else:
        print('Invalid input')
        new_order=input('Do you wish to order another pizza y/n: ')


cancel_order=input('Do you wish to cancel any pizza order y/n: ')
while True:
    if cancel_order.lower()=='n':
        print('Your Order Successfull')
        break
    elif cancel_order.lower()=='y':
        pizza=int(input('Select your Pizza number to cancel it: '))
        if pizza>len(pizzas): # if input out off list
            print('Invalid input')
            continue
        if pizza in ordered_pizza: # for already ordered pizza decrement/remove
            x=ordered_pizza.index(pizza)
            existing_qty=ordered_qty[x]
            print('The qty in record is', existing_qty)
            qty=int(input('Enter the Quantity to cancel: '))
            ordered_qty[x]-=qty
            if ordered_qty[x]==0:
                ordered_pizza.remove(pizza)
        cancel_order=input('Do you wish to cancel any pizza order y/n: ')
    else:
        print('Invalid input')
        cancel_order=input('Do you wish to cancel any pizza order y/n: ')

        

print('-------------------------------------')
print('                Bill                 ')
print('-------------------------------------')

final_cost=0
print('sr.no','    Pizzas      ','cost','qty','total')
for i in range(len(ordered_pizza)):
    total_cost=cost[ordered_pizza[i]]*ordered_qty[i]
    print('  {}. '.format(i+1),pizzas[ordered_pizza[i]],'',cost[ordered_pizza[i]],' ',ordered_qty[i],
          '',total_cost)
    final_cost=final_cost+total_cost
print('-------------------------------------')
print('        Final Amount            {}'.format(final_cost))










