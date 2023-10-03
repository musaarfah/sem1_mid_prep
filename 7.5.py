num=int(input('Number : '))
if num%2 == 0:
    print('Num is  divisible by 2 only')
    if num%3 ==0:
        print('Number is divisible by 2 ad 3')
if num%3 == 0:
    if num%5==0:
        print('Number is divisible by 3 and 5')
    elif num%7 ==0:
        print('Number is divisible by 3 and 5 and 7')
    else:
        print('Number is divisible by 3 only')
if num%5==0:
    if num%3!=0:
     print('Number is divisible by 5 only')
if num%7==0:
    if num%3!=0:
     print('Number is divisible by 7 only')