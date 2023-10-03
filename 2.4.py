seconds=int(input('Seconds :'))
hrs=seconds//3600
mins=(seconds%3600)//60
seconds1=(seconds%3600)%60
print(f'Hours :{hrs}\nMinutes :{mins}\nSeconds :{seconds1}')
