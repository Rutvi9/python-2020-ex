# program to read  3 float values from keyboard with , seperation and print sum

a,b,c=[float(x) for x in input('enter three float values for sum').split(',')]
print("sum is", a+b+c)