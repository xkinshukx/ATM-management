correctpin = "2836"


def verifypin():
    entered_pin = input("Enter your PIN: ")

    if entered_pin == correctpin:
        return True

    else:
        print("Incorrect PIN! Access Denied.")
        return False