char1=input('Character 1 : ')
char2=input('Character 2 : ')
order1=ord(char1)
order2=ord(char2)
count=0
if order1&1==order2&1:
    count=count+1
if order1&2==order2&2:
    count=count+1
if order1&4==order2&4:
    count=count+1
if order1&8==order2&8:
    count=count+1
if order1&16==order2&16:
    count=count+1
if order1&32==order2&32:
    count=count+1
if order1&64==order2&64:
    count=count+1
if order1&128==order2&128:
    count=count+1
print(f'In {char1} and {char2} {count} bits are same')
