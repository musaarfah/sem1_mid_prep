from random import*
i=1
while i<=10:
    num=randint(1,100)
    print('Number : ',num)
    left=num//10
    right=num%10
    if left==2:  print('Twenty',end=' ')
    elif left==3:
        print('Twenty',end=' ')
    elif left==4:
        print('Twenty',end=' ')
    elif left==5:
        print('Twenty',end=' ')
    elif left==6:
        print('Twenty',end=' ')
    elif left==7:
        print('Twenty',end=' ')
    elif left==8:
        print('Twenty',end=' ')
    elif left==9:
        print('Twenty',end=' ')
    if num==10:
        print('Ten',end='')
    elif num==11:
        print('Eleven',end='')
    elif num==12:
        print('Twelve',end='')
    elif num==13:
        print('Thirteen',end='')
    elif num==14:
        print('Fourteen',end='')
    elif num==15:
        print('Fifteen',end='')
    elif num==16:
        print('Sixteen',end='')
    elif num==17:
        print('Seventeen',end='')
    elif num==18:
        print('Eighteen',end='')
    elif num==19:
        print('Nineteen',end='')
    elif num==20:
        print('Twenty',end='')
    elif num==100:
        print('One Hundred',end='')
    elif right ==1:
        print('One',end=' ')
    elif right ==2:
        print('Two',end=' ')
    elif right ==3:
        print('Three',end=' ')
    elif right ==4:
        print('Four',end=' ')
    elif right ==5:
        print('Five',end=' ')
    elif right ==6:
        print('Six',end=' ')
    elif right ==7:
        print('Seven',end=' ')
    elif right ==8:
        print('Eight',end=' ')
    elif right ==9:
        print('Nine',end=' ')
    i=i+1