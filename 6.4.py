eggs=int(input('Eggs :'))
remainder=eggs%3
if remainder==0:
    packs=eggs//3
elif remainder!=0:
    packs=(eggs//3)+1
print('Packs = ',packs)