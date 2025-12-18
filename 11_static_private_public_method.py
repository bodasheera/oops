class BankAccount:

    def __init__(self, user ):
        self.user = user
        self.balance = 0


    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self.balance += amount
            print(f"{self.user} new balance is {self.balance}")
            self.__log_transaction("deposit")

    # protected method - class and sub class . but no error if object
    def _is_valid_amount(self, amount):
        return amount > 0

    # private method - only inside class. error if subclass and object
    def __log_transaction(self, txn ):
        print(f"{self.user} new balance is {self.balance} by {txn}")
    
    @staticmethod
    def is_valid_interest_rate(r):
        print(0 <= r <= 3) 
    

a = BankAccount("a")
a.deposit(100)
BankAccount.is_valid_interest_rate(2)
BankAccount.is_valid_interest_rate(5)
BankAccount.is_valid_interest_rate(-5)
