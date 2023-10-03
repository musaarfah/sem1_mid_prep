from random import*
x1=randint(1,1000)
x2=randint(1,1000)
x3=randint(1,1000)
print(x1,x2,x3)
if x1>x2:
 print('Numbers are not in order')
elif x1<x2 and x2<x3:
 print('Numbers are in order')
