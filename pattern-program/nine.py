# diamond pattern
n = int(input('enter no of rows'))
for i in range(n) :
    print(' '*(n-i-1)+'* '*(i+1))
for i in range(n) :
    print(' '*(i+1)+'* '*(n-i-1))

