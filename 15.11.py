from random import *

def main():
    i = 1
    while i <= 10:
        c1 = randint(0, 255)
        c2 = randint(0, 255)
        count = 0
        if (c1 & 1 ) == (c2 & 1):   count = count + 1;
        if (c1 & 2 ) == (c2 & 2):   count = count + 1;
        if (c1 & 4 ) == (c2 & 4):   count = count + 1;
        if (c1 & 8 ) == (c2 & 8):   count = count + 1;
        if (c1 & 16 ) == (c2 & 16):   count = count + 1;
        if (c1 & 32 ) == (c2 & 32):   count = count + 1;
        if (c1 & 64 ) == (c2 & 64):   count = count + 1;
        if (c1 & 128 ) == (c2 & 128):   count = count + 1;
        print (f'{c1} and {c2} has {count} same bits')
        i = i + 1

main()