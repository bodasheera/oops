# Encapsulation helps in hiding implementation details only exposing necessary functionality to outside world
# Clear difference between public interface and internal implementation. Users need not worry about how its implemented internally

# Encapsulation focuses on data hiding
# Wrapping data and methods together and restricting direct access to the data.
# A medicine capsule 💊
# The ingredients are protected inside; you can’t access them directly.

class BadBankAccount:

    def __init__(self, balance):
        self.balance = balance

    
account = BadBankAccount(0.0)
account.balance = -1
# print(account.balance)

class BankAccount:

    def __init__(self):
        self._balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit amount must be positive")
        
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Cannot withdraw more than balance")
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        self._balance -= amount

    @property
    def balance(self):
        return self._balance
    
    # dont give setter as it can be accesed from outside which we dont want 
    # @balance.setter
    # def balance(self, new_balance):
    #     self._balance = new_balance


account = BankAccount()
account.deposit(200)
account.withdraw(100)
account.withdraw(100)
# account.balance = -1 # This will fail as there is no setter 
