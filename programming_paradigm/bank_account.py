
from tkinter import dnd


class BankAccount:
    def __init__(self,account_balance=0.00):
        self.account_balance = account_balance

    def deposit(self,amount):
        self.account_balance += amount
    
    def withdraw(self,amount):
        self.account_balance -= amount
        if self.account_balance >= 0:
            return True
        else:
            return False
        
    def display_balance(self):
        print(f'the Balance is: {float(self.account_balance)}')
        return 0

b = BankAccount(100)
b.withdraw(10)
b.display_balance()
