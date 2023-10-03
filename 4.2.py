from random import*
num =randint(1,10)
user_input=int(input('Enter Guess :'))
if user_input==num:
    print('Winner')
else:
    print('Loser')
    print('Number : ',num)
    num1=randint(1,10)
    user_input1=int(input('Second Guess :'))
    if user_input1==num1:
        print('Winner')
    else:
        print('Loser')
        print('Number : ',num1)
        num2=randint(1,10)
        user_input2=int(input('Final Guess :'))
        if user_input2==num2:
            print('Winner')
        else:
            print('Loser')
            print('Number :',num2)
