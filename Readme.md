🏧 ATM Management System
A voice-enabled ATM simulation built with Python. Performs real ATM operations — with full text-to-speech audio feedback for every action.

⚠️ Proudly powered by Scammers Bank™ — "You have been scammed."


✨ Features

🔐 PIN Authentication — Secure login before accessing any features
💰 Check Balance — View your current account balance
📥 Deposit Money — Add funds to your account
📤 Withdraw Money — Withdraw with insufficient balance detection
🔊 Voice Feedback — Every action is spoken aloud using Google Text-to-Speech (gTTS)


📁 Project Structure
ATM-management/
│
├── main.py        # Entry point — menu, voice greetings, flow control
├── atm.py         # Core ATM functions (balance, deposit, withdraw)
├── pin.py         # PIN verification logic
├── database.py    # Stores account balance data
└── voice.mp3      # Temporary audio file generated at runtime

🛠️ Tech Stack

Python 3
gTTS (Google Text-to-Speech) — converts text to spoken audio
playsound — plays the generated audio file


📦 Installation

Clone the repository

bash   git clone https://github.com/xkinshukx/ATM-management.git
   cd ATM-management

Install dependencies

bash   pip install gtts playsound

Run the program

bash   python main.py

🚀 How It Works

Program starts and greets you with a voice message
You are prompted to enter your 4-digit PIN
On successful login, a menu appears:

   1. Check Balance
   2. Deposit Money
   3. Withdraw Money
   4. Exit

Every action prints a result and speaks it out loud
If balance is insufficient during withdrawal — it lets you know 😅


👨‍💻 Author
Kinshuk (@xkinshukx)
B.Tech Student — AI & Data Science
Skilled in Python & C++ | Exploring Game Development & Data Science
Show Image
Show Image

📄 License
This project is open source and free to use.
