#Abby Travers

from savings_account import savingsAccount
from checking_account import checkingAccount

def main():
    savingsone = savingsAccount("Jessica Fort", 5367, 100, "123456789", "112233445", 3)
    savingstwo = savingsAccount("Andreas Jones", 66346, 1000, "987654321", "998877665", 4)

    checkingone = checkingAccount("Jessica Fort", 5000, 100, "123123123", "321321321", 5000)
    checkingtwo = checkingAccount("Andreas Jones", 7000, 500, "65465464", "456456456", 2000)

    checkingone.withdraw(3000)
    savingsone.interest()
    checkingone.transfer(3000, savingsone)
    checkingone.print_customer_information()
    savingsone.print_customer_information()

    savingstwo.interest()
    savingstwo.print_customer_information()

    checkingtwo.withdraw(3000)
    checkingtwo.transfer(3000, savingsone)
    checkingtwo.print_customer_information()


if __name__ == "__main__":
    main()
