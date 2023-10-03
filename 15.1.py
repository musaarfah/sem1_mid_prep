from random import*
i=1
while i<=10:
    num1=randint(0,255)
    num2=randint(0,255)
    count=0
    if num1 & 1 == num2 & 1:
        count=count+1
    if num1 & 2==num2 & 2:
        count=count+1
    if num1 & 4 == num2 & 4:
        count = count + 1
    if num1 & 8 == num2 & 8:
        count = count + 1
    if num1 & 16 == num2 & 16:
        count = count + 1
    if num1 & 32 == num2 & 32:
        count = count + 1
    if num1 & 64 == num2 & 64:
        count = count + 1
    if num1 & 128 == num2 & 128:
        count = count + 1
    print(f'{num1} and {num2} have {count} same bits''\n')
    i=i+1
