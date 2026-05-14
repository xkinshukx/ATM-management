import database

import os
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

def checkbalance():
    print(f"Your balance is Rupees{database.balance}")
    speak(f"Your Balance is Rupees{database.balance}")


def depositmoney():
    amount = float(input("Enter amount to deposit: ₹"))

    database.balance += amount

    print(f"₹{amount} deposited successfully.")
    speak(f"₹{amount} deposited successfully.")
    print(f"Updated Balance: ₹{database.balance}")
    speak(f"Updated Balance: ₹{database.balance}")


def withdrawmoney():
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= database.balance:
        
        database.balance -= amount

        print(f"₹{amount} withdrawn successfully.")
        speak(f"₹{amount} withdrawn successfully.")

        print(f"Remaining Balance: ₹{database.balance}")
        speak(f"Remaining Balance: ₹{database.balance}")

    else:
        print("Insufficent Balance.. Get a job")
        speak("Insufficent Balance..Get a job")