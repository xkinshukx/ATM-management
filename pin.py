import pyttsx3
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

correctpin = "2836"


def verifypin():
    enteredpin = input("Enter your PIN: ")

    if enteredpin == correctpin:
        return True

    else:
        print("Incorrect PIN.. Access Denied.")
        return False