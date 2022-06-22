import speech_recognition as sr
from text_to_speech import speak
import random
from datetime import datetime as dt
import os


def add_to_text(user, text):
    txtFile = open("./Conversations.txt", mode="a")
    date = f"[{dt.now().year}/{dt.now().month}/{dt.now().day}] [{dt.now().hour}:{dt.now().minute}:{dt.now().second}]"
    if user == "user":
        txtFile.write(f"Me : {text}  {date}\n")
    else:
        txtFile.write(f"Kassandra : {text}  {date}\n")

    txtFile.close()


def Listen():
    R = sr.Recognizer()
    with sr.Microphone() as Source:
        Audio = R.listen(Source)
        Said = ""

        try:
            Said = R.recognize_google(Audio)
            # print(Said)
        except Exception as E:
            print("Exception: " + str(E))

    return Said


speak(f"Hi, I'm Kassandra.")
add_to_text("kassandra", "Hi, I'm Kassandra.")
Hi_list = ["hi", "hello", "hi there"]
Greeting_list = ["how are you", "how are you doing", "how you doing"]
Greeting_respond_list = ["i'm great, thanks", "very good, thank you"]
Conformation_list = ["ok", "alright", "of course", "very well"]
pos_answers = ["yes", "yeah", "yep"]
neg_answers = ["no", "nope", "nah"]
gratitude_list = ["thank you", "thanks", "gratitude", "thank you very much"]
gratitude_respond_list = ["Your wellcome", "Of course", "Don't mention it", "Any time"]

while True:
    Text = Listen().lower()

    if Text in Hi_list:
        rnd_respond = random.choice(Hi_list)
        print(rnd_respond)
        speak(rnd_respond)
        add_to_text("user", Text)
        add_to_text("Kassandra", rnd_respond)

    elif Text in Greeting_list:
        rnd_respond = random.choice(Greeting_respond_list)
        print(rnd_respond)
        speak(rnd_respond)
        add_to_text("user", Text)
        add_to_text("Kassandra", rnd_respond)

    elif "repeat" in Text:
        rnd_respond = random.choice(Conformation_list)
        print(f"{rnd_respond}, I'm listening.")
        speak(f"{rnd_respond}, I'm listening.")
        add_to_text("user", Text)
        add_to_text("Kassandra", rnd_respond)

        Text = Listen()
        print(Text)
        speak(Text)
        add_to_text("user", Text)
        add_to_text("Kassandra", Text)

    elif Text in gratitude_list:
        rnd_respond = random.choice(gratitude_respond_list)
        print(rnd_respond)
        speak(rnd_respond)
        add_to_text("user", Text)
        add_to_text("Kassandra", rnd_respond)

    elif "open vs code" in Text:
        os.startfile("E:/Software/Microsoft VS Code/Code.exe")
        print("Ok, I'll open visual studio code.")
        speak("Ok, I'll open visual studio code.")
        add_to_text("user", Text)
        add_to_text("Kassandra", "Ok, I'll open visual studio code.")

    elif "open github desktop" in Text:
        os.startfile("C:/Users/Ranger Omid/AppData/Local/GitHubDesktop/GitHubDesktop.exe")
        print("Ok, I'll open git hub desktop.")
        speak("Ok, I'll open git hub desktop.")
        add_to_text("user", Text)
        add_to_text("Kassandra", "Ok, I'll open git hub desktop.")

    elif "py charm" in Text:
        os.startfile("E:/Software/PyCharm 2021.3/bin/pycharm64.exe")
        print("Ok, I'll open py charm.")
        speak("Ok, I'll open py charm.")
        add_to_text("user", Text)
        add_to_text("Kassandra", "Ok, I'll open py charm.")

    else:
        print(Text)
        add_to_text("user", Text)
        print("Sorry, Cannot understand that")
        speak("Sorry, Cannot understand that")
        add_to_text("Kassandra", "Sorry, Cannot understand that")
        print("do you have any other request?")
        speak("do you have any other request?")
        add_to_text("Kassandra", "do you have any other request?")
        Text = Listen()
        if Text in pos_answers:
            print("I'm listening")
            speak("I'm listening")
            add_to_text("user", Text)
            add_to_text("Kassandra", "I'm listening")

        else:
            add_to_text("user", Text)

            break
