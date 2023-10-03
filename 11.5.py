from random import*
i=1
sum_even=0
sum_odd=0
while i<=10:
    num=randint(1,10)
    print('Number :',num)
    if num%2==0:
        sum_even=sum_even+num
    elif num%2 != 0:
        sum_odd=sum_odd+num
    print('Sum of Even Numbers : ',sum_even)
    print('Sum of Odd Numbers : ',sum_odd)
    i=i+1