i=1
x=1
integer=int(input('Integer : '))
while i<=integer:
    if integer%x==0:
        print(f'{integer} is divisible by {x}')
    x=x+1
    i=i+1