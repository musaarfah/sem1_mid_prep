from random import*
i=1
while i<=10:
    num=randint(1,100)
    right=num%10
    left=num//10
    if right==0:
            right=''
    elif right==1:
            right='One'
    elif right==2:
            right='Two'
    elif right==3:
            right='Three'
    elif right==4:
            right='Four'
    elif right==5:
            right='Five'
    elif right==6:
            right='Six'
    elif right==7:
            right='Seven'
    elif right==8:
            right='Eight'
    elif right==9:
            right='Nine'

    if left==2:
            left='Twenty'
    elif left==3:
            left='Thirty'
    elif left==4:
            left='Forty'
    elif left==5:
            left='Fifty'
    elif left==6:
            left='Sixty'
    elif left==7:
            left='Seven'
    elif left==8:
            left='Eight'
    elif left==9:
        lef='Nine'
    print(f'Number {num} in English is {left} {right}')
    if num==100:
        print(f'Number {num} in English is One Hundred')
    elif num==11:
        print(f'Number {num} in English is Eleven')
    elif num==12:
        print(f'Number {num} in English is Twelve')
    elif num==13:
        print(f'Number {num} in English is Thirteen')
    elif num == 14:
        print(f'Number {num} in English is Fourteen')
    elif num==15:
        print(f'Number {num} in English is Fifteen')
    elif num==16:
        print(f'Number {num} in English is Sixteen')
    elif num==17:
        print(f'Number {num} in English is Seventeen')
    elif num==18:
        print(f'Number {num} in English is Eighteen')
    elif num==19:
        print(f'Number {num} in English is Nineteen')
    i=i+1