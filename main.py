import webbrowser
import speech_recognition as s_r
import time
import pyttsx3
import sys
# print(s_r.Microphone.list_microphone_names())
engine = pyttsx3.init('sapi5')
def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()
def takeinputfromuser():
    r = s_r.Recognizer()
    engine = pyttsx3.init('sapi5')
    with s_r.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        print("Recognizing....")
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User : {query} \n")
        except:
            print("Can you repeat that again please")
    return query
if __name__ == "__main__":
    while True:
        query = takeinputfromuser()
        query = query.lower()
        if query == "youtube" or query == "open youtube":
            print("Opening Youtube..")
            speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com/")
        elif query == "monkey type":
            print("Opening MonkeyType..")
            speak("Opening MonkeyType...")
            webbrowser.open("https://monkeytype.com/")
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
        else:
            print("Sorry that is not available")
            speak("Sorry that is not available")