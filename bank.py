# to make a menu driven program to perform the following operations on a bank account using class
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit

class Bank:
    def __init__(self, name, acc_no, balance):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
    def withdraw(self, amount):
        if self.balance<amount:
            print("Insufficient balance")
        else:
            self.balance-=amount
    def check_balance(self):
        print("Balance is: ", self.balance)
    def display(self):
        print("Name: ", self.name)
        print("Account number: ", self.acc_no)
        print("Balance: ", self.balance)
        
b=Bank("Aayushker", 6, 1000)
b.deposit(100000)
b.withdraw(200)
b.check_balance()
b.display()

