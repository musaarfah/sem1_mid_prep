from random import*
i=1
count=1
max=0
min=100
min_count=1
while i<=10:
    num1=randint(0,10)
    num2=randint(0,10)
    num3=randint(0,10)
    print(num1,num2,num3)
    avg=((num1+num2+num3)/3)
    if avg>max:
        max=avg
        count=i
    i=i+1
print(f'Set {count} has max avg')