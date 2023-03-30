import speech_recognition as s_r
import time
import pyttsx3
# print(s_r.Microphone.list_microphone_names())
r = s_r.Recognizer()
r = s_r.Recognizer()
engine = pyttsx3.init('sapi5')
with s_r.Microphone() as source:
    print("Listening....")
    r.pause_threshold = 1
    audio = r.listen(source)
try:
    print("Recognizing....")
    query = r.recognize_google(audio, language='en-in')
    print(query)
except Exception as e:
      print(e)