import speech_recognition as sr
import pyaudio
import webbrowser
import pyttsx3
from personal_work import Personal


def speak(sentence):
    engine = pyttsx3.init()
    engine.say(sentence)
    engine.runAndWait()

def processcommand(c):

    # if "open youtube" in c.lower():
    #      webbrowser.open("https://www.youtube.com/") 
    # elif "open google" in c.lower():
    #      webbrowser.open("https://www.google.com/")
    # elif "open gmail" in c.lower():
    #      webbrowser.open("https://mail.google.com/mail/u/0/")
    # elif "open" in c.lower():
    #      work = c.lower().split(" ")[1]
    #      if work=="lead":
    #          webbrowser.open("https://leetcode.com/")


    if "open" in c.lower():
        work = c.lower().split(" ")[1]
        link = Personal.get(work)

        if link :
            webbrowser.open(link)
        else:
            speak("command not found")




if __name__ == "__main__" :
    speak("initializing jarvis")



    while True : 

        try :
            r = sr.Recognizer()   # it creates speech recognizer
            m = sr.Microphone()    # to access your microphone

            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source)                 # it takes the audio 
                text = r.recognize_google(audio)         # it converts that audio in text


                if "jarvis" in text.lower():
                    speak("how can i help you")

                    with sr.Microphone() as source:
                        print("activated jarvis...")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        print(command)

                    if "stop" in command.lower():
                        speak("jarvis deactivated")
                        break


                    processcommand(command)

        except Exception as e:
            print("error")