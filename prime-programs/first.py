# given number prime or not
n = int(input('enter any number'))
if n <= 1 :
    print('it is not prime no.')
else:
    is_prime = True
    for i in range(2,n) :
        if n%i ==0:
            is_prime = False
