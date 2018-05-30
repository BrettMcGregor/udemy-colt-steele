class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

acct = BankAccount("Darcy")
print(acct.owner)
print(acct.balance)
print(acct.deposit(10))
print(acct.withdraw(3))
print(acct.balance)
