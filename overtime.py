hours = float(input('Enter hours:'))

rate = float(input('Enter rate:'))

overtime = (rate * 1.5) * (hours - 40)

if hours > 40:
    pay = (rate * 40) + overtime
    print('Pay:$', pay)
    print('Overtime:$', overtime)

else:
    pay = rate * hours
    print('Pay:$', pay)
