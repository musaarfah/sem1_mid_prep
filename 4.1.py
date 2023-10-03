from random import*
a=randint(0,50)
b=randint(0,50)
c=randint(0,50)
if a==0:
    print('Equation is linear')
else:
    disc=(b**2)-4*a*c
    if disc<0:
        print('Roots are Imaginary')
    elif disc>0:
        root1=(-b+disc)/4**a
        root2=(-b-disc)/4**a
        print(root1,root2)