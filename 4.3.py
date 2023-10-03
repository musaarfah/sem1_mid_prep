from random import*
num1=randint(1,10)
num2=randint(1,10)
num3=randint(1,10)
print(num1,num2,num3)
diff1=num1-num2
diff2=num2-num1
diff3=num1-num3
diff4=num3-num1
diff5=num2-num3
diff6=num3-num2
if diff1&diff2&diff3&diff4&diff6&diff5>=2:
    print('OK')
else:
    print('Sorry')