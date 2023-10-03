from random import*
i=1
max=0
count=1
while i<=10:
    num1=randint(1,100)
    num2=randint(1,100)
    num3=randint(1,100)
    print(num1,num2,num3)
    avg=int((num1+num2+num3)/3)
    if avg>max:
        max=avg ; count=i
    i=i+1
print(f'Set {count} has highest average {max}')