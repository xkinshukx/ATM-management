import database


def check_balance():
    print(f"Your balance is ₹{database.balance}")


def deposit_money():
    amount = float(input("Enter amount to deposit: ₹"))

    database.balance += amount

    print(f"₹{amount} deposited successfully.")
    print(f"Updated Balance: ₹{database.balance}")


def withdraw_money():
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= database.balance:
        database.balance -= amount

        print(f"₹{amount} withdrawn successfully.")
        print(f"Remaining Balance: ₹{database.balance}")

    else:
        print("Insufficient balance!")