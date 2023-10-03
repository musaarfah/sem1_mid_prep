from random import*
i=1
while i<=10:
    num1=randint(1,100)
    num2=randint(1,100)
    print(num1,num2)
    if num1>num2:
        print('First Number is Larger')
    else:
        print('Second Number is Larger')
    i=i+1