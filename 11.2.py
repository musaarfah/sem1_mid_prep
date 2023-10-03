from random import*
i=1
while i<=10:
    num1=randint(1,100)
    num2=randint(1,100)
    num3=randint(1,100)
    print('Numbers unarranged : ',num1,num2,num3)
    max=num3
    if num2>max:
        max=num2
    if num1>max:
        max=num1
    min=num1
    if num2<min:
        min=num2
    if num3<min:
        min=num3
    mid=num2
    if num1>num2 and num1<num3:
        mid=num1
    if num1>num3 and num1<num2:
            mid=num1
    if num3 > num2 and num3<num1:
        mid=num3
    if num3<num2 and num3>num1:
            mid = num3
    print('Numbers arranged : ',min,mid,max)
    i=i+1