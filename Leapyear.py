year= int(input('Enter the Year:'))
if year%400 == 0 and year%4 == 0:
    print(f'The {year} is Leap Year')

else:
    print(f'The {year} is normal Year.')


