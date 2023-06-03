import webbrowser
import speech_recognition as s_r
import random
import pyttsx3
import sys
import json
import requests
# print(s_r.Microphone.list_microphone_names())
engine = pyttsx3.init('sapi5')
def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()
def toss():
    coin = ["Heads","Tails"]
    headortail = random.choice(coin)
    speak(headortail)
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
def weather():
    city = "Visakhapatnam"
    url = f"http://api.weatherapi.com/v1/current.json?key=56e64a35c7c346a689055403230803&q={city}"
    r = requests.get(url) # type(r) = "String"
    # print(r.text)
    weatherdictionary = json.loads(r.text) #pronunce loads as lods or load string
    temp_in_c = weatherdictionary["current"]["temp_c"]
    speak(f"The temperature in {city} is: {temp_in_c} degrees celcius")
if __name__ == "__main__":
    while True:
        try:
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
                break
            elif query == "flip a coin":
                toss()
            elif query == "jarvis what is today's weather" or query == "what is today's weather" or query == "today's weather" or query == "weather" or query == "today weather" or query == "what is today weather" or query == "jarvis what is today weather":
                # city = "Visakhapatnam"
                # url = f"http://api.weatherapi.com/v1/current.json?key=56e64a35c7c346a689055403230803&q={city}"
                # r = requests.get(url) # type(r) = "String"
                # # print(r.text)
                # weatherdictionary = json.loads(r.text) #pronunce loads as lods or load string
                # temp_in_c = weatherdictionary["current"]["temp_c"]
                # speak(f"The temperature in {city} is: {temp_in_c} degrees celcius")
                weather()
            elif query == "hello" or query == "hello jarvis" or query == "hi" or query == "hi jarvis":
                greetings = ["Namaste Sir","Hello Sir","How are you sir","How is Nikshita?","How may I help you"]
                speak(random.choice(greetings))
            elif query == "i am fine" or query == "i am fine , how about you":
                speak("Great to listen, Iam also fine. But remember whatever position you are in is not permanent")
            elif query == "im not fine" or query == "im depressed":
                speak("I told you one phrase when you were fine , whatever position you are in is not permanent. Just listen to this video")
                webbrowser.open("https://www.youtube.com/watch?v=CXRxrYBgUIo&ab_channel=Psych2Go")
            else:
                speak("Sorry that is not available")
        except:
            speak("Can you repeat that again")