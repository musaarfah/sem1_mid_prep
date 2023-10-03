from random import*
i=1
count0=0
count1=0
while i<=5:
    e=randint(0,1)
    print(e)
    if e==0:
        count0=count0+1
    elif e==1:
        count1=count1+1
    i=i+1
print(f'zeroes : {count0}\nones : {count1}')