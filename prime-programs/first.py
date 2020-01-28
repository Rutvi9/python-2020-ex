# given number prime or not
n = int(input('enter any number'))
if n <= 1 :
    print('it is not prime no.')
else:
    is_prime = True
    for i in range(2,n//2+1) : # from 2 to n//2
        if n%i ==0:
            is_prime = False
            break
    if is_prime == True:
        print('prime no.')
    else:
        print('is not prime no.')