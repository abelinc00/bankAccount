
from bank_account import BankAccount

class checkingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance,account_number, routing_number,transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    def transfer(self,amount, target_account):
        if amount <= self.transfer_limit:
            if self.current_balance - amount >= self.minimum_balance:
                self.current_balance -= amount
                target_account.current_balance += amount
                print(f"Transfer Complete: ${amount} to {target_account.customer_name}. New Balance: ${self.current_balance}")
            else:
                print(f"You cannot transfer ${amount} balance would be below the minimum balance")
        else:
            print(f"Transfer limit exceeded. Max allowed is ${self.transfer_limit}")