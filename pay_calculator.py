#This program adds exception handling to to overtime.py program

try:
    hours = float(input('Enter hours:')) #Input for hours worked

    rate = float(input('Enter rate:')) #Input for pay rate

    overtime = (rate * 1.5) * (hours - 40) #Calculate overtime as 1.5 * pay for hours worked over 40

    #if more than 40 hours were worked, add overtime pay calculation and print both pay and overtime pay
    if hours > 40: 
        pay = (rate * 40) + overtime
        print('Pay:$', pay)
        print('Overtime:$', overtime)

    #if 40 or less hours were worked then do simple pay rate calculation and print pay
    else:
        pay = rate * hours
        print('Pay:$', pay)
except ValueError:
    print('Error: Please enter a valid number')

