from random import*
marks1=randint(0,100)
marks2=randint(0,100)
if marks1==marks2:
 print('Marks are Same')
elif marks1>=85:
    grade1='A'
elif marks1>=80:
    grade1='A-'
elif marks1>=75:
    grade1='B'
elif marks1>=70:
    grade1='B-'
elif marks1>=65:
    grade1='C'
elif marks1>=60:
    grade1='C-'
elif marks1>=55:
    grade1='D'
elif marks1>=50:
    grade1='D-'
elif marks1<50:
    grade1='F'
if marks2>=85:
    grade2='A'
elif marks2>=80:
    grade2='A-'
elif marks2>=75:
    grade2='B'
elif marks2>=70:
    grade2='B-'
elif marks2>=65:
    grade2='C'
elif marks2>=60:
    grade2='C-'
elif marks2>=55:
    grade2='D'
elif marks2>=50:
    grade2='D-'
elif marks2<50:
    grade2='F'
if grade1==grade2:
 print('Marks are almost same')
else:
 print('Marks are Different')