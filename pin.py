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

correctpin = "2836"


def verifypin():
    print("Enter Your Pin")
    speak("Enter your pin")
    enteredpin = input("Enter your PIN: ")
    
    if enteredpin == correctpin:
        return True

    else:
        print("Incorrect PIN.. Access Denied.")
        speak("Incorrect PIN Access Denied")
        return False