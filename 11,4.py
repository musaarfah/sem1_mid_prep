from random import*
i=1
while i<=10:
    alph=randint(65,91)
    if alph==65 or alph==69 or alph==73 or alph==79 or alph==85:
        print(f'{chr(alph)} : Alphabet is a Vowel')
    else:
        print(f'{chr(alph)} : Alphabet is a consonant')
    i=i+1
