import random

class Customer:
    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

def main():
    name = input('Enter Name: ')
    balance = random.randrange(0, 5000)
    print('Balance: ' + '$' + str(balance))

    action = input('Do you want to withdraw or deposit?: ')
    amount = float(input('Enter Amount: '))

    object = Customer(name, balance)

    if action == 'withdraw':
        print('Balance: ' + '$' + str(object.withdraw(amount)))
    elif action == 'deposit':
        print('Balance: ' + '$' +str(object.deposit(amount)))
    else:
        print('Invalid command')

main()
