# Mahesh Yennam
# Voting mini project

cnt_A=0
cnt_B=0

while True:
    vote=input('Enter your vote to A/B or Q to quit: ')
    if vote.lower()=='a':
        cnt_A+=1
    elif vote.lower()=='b':
        cnt_B+=1
    elif vote.lower()=='q':
        break
    else:
        print('Invalid input')

print('A group got {} votes'.format(cnt_A))
print('B group got {} votes'.format(cnt_B))

if cnt_A>cnt_B:
    print('A group won by {} votes'.format(cnt_A-cnt_B))
elif cnt_A==cnt_B:
    print('Tie between both A and B group')
else:
    print('B group won by {} votes'.format(cnt_B-cnt_A))

