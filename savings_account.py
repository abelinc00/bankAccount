
from bank_account import BankAccount

class savingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance,account_number, routing_number,interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance,account_number, routing_number)
        self.interest_rate = interest_rate

    def interest(self):
        interestAdded = self.current_balance * (self.interest_rate / 100)
        self.current_balance += interestAdded
        print(f"Interest Added: ${interestAdded}. New Balance: ${self.current_balance}")
