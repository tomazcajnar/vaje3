a = 11 #Variable for printing spaces

for i in range(1,12,2): # for loop for printing stars
    print(' '*a+i*'*')
    a =a-1
print('CONGRATULATIONS !!')

i=1
for j in range(11,0,-2):
    print(i*' '+j*'*')
    i=i+1
