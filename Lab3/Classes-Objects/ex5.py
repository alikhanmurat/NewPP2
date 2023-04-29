class bank_account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        print(f"Deposited {money} || balance: {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print(f"Can't be overdrawn!")
        else:
            self.balance -= money
            print(f"{money} withdrawn || balance: {self.balance}")

account = bank_account(str(input()), int(input()))

print ("Amount of money to Deposit ₸")
x = int(input())
account.deposit(x)

print ("Amount of money to Withdraw ₸")
y = int(input())  
account.withdraw(y)

print ("Amount of money to Withdraw ₸")
z = int(input())
account.withdraw(z)

print ("Amount of money to Deposit ₸")
w = int(input())
account.deposit(w)
