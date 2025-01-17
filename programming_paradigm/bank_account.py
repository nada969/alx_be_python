
from tkinter import dnd


class BankAccount:
<<<<<<< HEAD
    def __init__(self,account_balance=0.00):
        self.account_balance = account_balance
=======
    def __init__(self,account_balance=0):
        #["Current Balance:"]
        self.account_balance = account_balance 
>>>>>>> ec1d69fc68d3f9ca3581e5247a563cb0a6610fa3

    def deposit(self,amount):
        self.account_balance += amount
    
    def withdraw(self,amount):
        self.account_balance -= amount
        if self.account_balance >= 0:
            return True
        else:
            return False
        
    def display_balance(self):
<<<<<<< HEAD
        print(f'the Balance is: {float(self.account_balance)}')
=======
        print(f'Current Balance: ${float(self.account_balance)}')
>>>>>>> ec1d69fc68d3f9ca3581e5247a563cb0a6610fa3
        return 0

b = BankAccount(100)
b.withdraw(10)
b.display_balance()
