
import datetime
import pyttsx3
speaker = pyttsx3.init()
speaker.say('i m hero')
speaker.runAndWait()

engine=pyttsx3.init('sapi5')
voices=engine.getproperty('voices')
print(voices[1].id)
engine.setproperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():  
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("good Afternoon!")
    else:
        speak("good Evening!")
    speak("i am rex sir.please tell me how may i help u")              
if __name__=="__main__": 
    wishMe()   