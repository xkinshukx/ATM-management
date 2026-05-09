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
        speak("Option 1 Check Balance")
        speak("Option 2 Deposit Money")
        speak("Option 3 Withdraw Money")
        speak("Option 4 Exit")

        choice = input("Select an option: ")

        if choice == "1":
            checkbalance()

        elif choice == "2":
            depositmoney()

        elif choice == "3":
            withdrawmoney()

        elif choice == "4":
            print("Thankyou for using the ATM.")
            speak("Thankyou for using the ATM")
            break

        else:
            print("Invalid choice")
            speak("Invalid choice")