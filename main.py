import webbrowser
import speech_recognition as s_r
import time
import pyttsx3
# print(s_r.Microphone.list_microphone_names())
r = s_r.Recognizer()
engine = pyttsx3.init('sapi5')
with s_r.Microphone() as source:
    print("Listening....")
    r.pause_threshold = 1
    audio = r.listen(source)
try:
    print("Recognizing....")
    query = r.recognize_google(audio, language='en-in')
    if query == "YouTube":
        print("Opening Youtube..")
        engine.say("Opening Youtube...")
        webbrowser.open("https://www.youtube.com/")
        engine.startLoop(True)
    elif query == "monkey type":
         print("Opening MonkeyType..")
         engine.say("Opening MonkeyType...")
         webbrowser.open("https://monkeytype.com/")
         engine.startLoop(True)
    else:
         print("Sorry that is not available")
         engine.say("Sorry that is not available")
         engine.startLoop(True)             
except Exception as e:
      print(e)