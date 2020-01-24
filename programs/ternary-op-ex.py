a= 10
b= 20
c= 30 if a>b else 40
print(c)

# for user defined values
a = int(input('Enter 1st no.'))
b = int(input('Enter 2nd no.'))
min = a if a<b else b
print(min)

# nested ternary operator example
a = int(input('Enter 1st no.'))
b = int(input('Enter 2nd no.'))
c = int(input('Enter 3rd no.'))

min= a if a<b and a<c else b if b<c else c
print(min)

# another example for ternary operator
a = int(input('Enter 1st no.'))
b = int(input('Enter 2nd no.'))

result= "Both number are equal" if a==b else "smaller" if a<b else "bigger"
print(result)
