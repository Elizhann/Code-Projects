#This is a program that adds functions to the overtime.py file

def main():
    hours = float(input('Enter hours:')) 

    rate = float(input('Enter rate:')) 

    compute_pay(hours, rate)

def compute_pay(hours, rate):

    if  hours > 40:
        base_pay = rate * hours
        overtime = (rate * 1.5) * (hours - 40)
        total_pay = base_pay + overtime
        print('Base Pay:$', base_pay)
        print('Overtime:$', overtime)
        print('Total Pay:$',total_pay)
        
    else:
        total_pay = rate * hours
        print('Total Pay:$', total_pay)           
main()



