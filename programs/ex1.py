#immutability example
l1= [10,20,'abcdef',30,40]
l2= l1
print(type(l1))
print(l1)
print(l2)
l1[0]= 7777
print(l1)
print(l2)
# slicing operation in list
print(l1[1:3])

# append and remove in list
l1.append(50)
l1.append(60)
print(l1)
l1.remove(50)
print(l1)