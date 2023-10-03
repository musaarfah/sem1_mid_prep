num=int(input('Three digit Number : '))
last_digit=num%10
second_digit=(num//10)%10
first_digit=(num//10)//10
print(f'First Digit :{first_digit}\nSecond Digit :{second_digit}\nThird Digit :{last_digit}')
sum=last_digit+first_digit+second_digit
print('Sum of Digits :',sum)
print(f'Digit in Reverse : {last_digit}{second_digit}{first_digit}')