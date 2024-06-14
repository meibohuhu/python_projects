# Define Bank Account Below:

class BankAccount:

    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def deposit(self, the_deposit):
        self.balance += the_deposit
        return self.balance

    def withdraw(self, number):
        self.balance -= number
        return self.balance

acct = BankAccount("wendy")
print(acct.deposit(19.2))
