import os
from atm import checkbalance, depositmoney, withdrawmoney
from pin import verifypin
from gtts import gTTS
from playsound import playsound

def speak(text):

    voice = gTTS(
        text=text,
        lang="en",
        slow=False
    )
    if os.path.exists("voice.mp3"):
        os.remove("voice.mp3")

    voice.save("voice.mp3")
    playsound("voice.mp3")


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
        speak("Option 2 Deposite Money")
        speak("Option 3 Withdraw Money")
        speak("Option 4 Exit")

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