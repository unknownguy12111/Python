#   RoBoSpeaker can be used to speak 
import pyttsx3
engine = pyttsx3.init()
print('''Welcome to the RoBoSpeaker
Create by Pawan Bhati''')

while True:
    text = input("What you want me to pronounce: ")
    if text.lower() == "quit":
        engine.say("Thanks for using RoBoSpeaker")
        engine.runAndWait()
        break
    else:
        engine.say(text)
        engine.runAndWait()
