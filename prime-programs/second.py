# generate prime nos. less than or equal given no.
n =  int(input('enter n value:'))
n1 =2
while n1<=n :
    # code to check whether n1 is prime
    is_prime= True
    for i in range(2,n1//2+1) :
        if n1%i==0 :
            is_prime = False
            break
    if is_prime == True :
        print(n1)
    n1= n1+1

