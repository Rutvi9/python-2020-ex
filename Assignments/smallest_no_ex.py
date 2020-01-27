a= int(input('enter first number'))
b= int(input('enter second number'))
c= int(input('enter third number'))
if a<b and a<c:
    print('smallest number is ',a)
elif b<c:
    print('smallest number is',b)
else:
    print('smallest number is', c)