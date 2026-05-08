from atm import checkbalance, depositmoney, withdrawmoney
from pin import verifypin

print("----Welcome to Scammers Bank----")

if verifypin():

    while True:

        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            checkbalance()

        elif choice == "2":
            depositmoney()

        elif choice == "3":
            withdrawmoney()

        elif choice == "4":
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid choice!")