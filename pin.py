correct_pin = "1234"


def verify_pin():
    entered_pin = input("Enter your PIN: ")

    if entered_pin == correct_pin:
        return True

    else:
        print("Incorrect PIN! Access Denied.")
        return False