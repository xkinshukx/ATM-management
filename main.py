from atm import check_balance, deposit_money, withdraw_money
from pin import verify_pin

print("===== Welcome to ATM =====")

if verify_pin():

    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit_money()

        elif choice == "3":
            withdraw_money()

        elif choice == "4":
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid choice!")