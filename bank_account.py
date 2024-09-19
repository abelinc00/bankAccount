
class BankAccount:
    bank_title = "NMF Bank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self.__routing_number = routing_number

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"Deposited ${amount} New Balance: ${self.current_balance}")

    def withdraw(self, amount):
        if amount > 0:
            if self.current_balance - amount > self.minimum_balance:
                self.current_balance -= amount
                print(f"Withdrawn ${amount} New Balance: ${self.current_balance}")
            else:
                print(f"You cannot withdraw ${amount} balance would be below the minimum balance")
    def print_customer_information(self):
        print(f"Customer: {self.customer_name}")
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Current Balance: ${self.current_balance}")
        print(f"Minimum Balance: ${self.minimum_balance}")
        print(f"Account Number: {self._account_number}")
        print(f"Routing Number: {self.__routing_number}")

    def __get_routing_number(self):
        return self.__routing_number