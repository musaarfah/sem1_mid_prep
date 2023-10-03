from random import*
x1=(randint(0,100))
x2=(randint(0,100))
x3=(randint(0,100))
x4=(randint(0,100))
print(x1,x2,x3,x4)
if x1>x2:
    x1,x2=x2,x1
if x2>x3:
    x2,x3=x3,x2
if x3>x4:
    x3,x4=x4,x3
if x2>x3:
    x2,x3=x3,x2
if x1>x2:
    x1,x2=x2,x1
print(x1,x2,x3,x4)