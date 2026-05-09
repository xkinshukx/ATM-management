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

balance = 5000
speak("Your Current Balance is",balance)