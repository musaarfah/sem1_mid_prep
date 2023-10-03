x1=int(input('Integer 1 :'))
x2=int(input('Integer 2 :'))
sum=0
while x1<=x2:
    print(x1,end=' ')
    sum=sum+x1
    x1=x1+1
print('Sum :',sum)