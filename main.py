from atm import checkbalance, depositmoney, withdrawmoney
from pin import verifypin
import pyttsx3
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


print("Welcome to Scammers Bank")
speak("Welcome to Scammers Bank")

if verifypin():

    while True:

        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        speak("Select an option")

        choice = input("Select an option: ")

        if choice == "1" or choice == "Check Balance".upper():
            checkbalance()

        elif choice == "2"or choice == "Deposit Money".upper():
            depositmoney()

        elif choice == "3"or choice == "Withdraw Money".upper():
            withdrawmoney()

        elif choice == "4"or choice == "Exit".upper():
            print("Thankyou for using the ATM.")
            speak("Thankyou for using the ATM")
            break

        else:
            print("Invalid choice")
            speak("Invalid choice")