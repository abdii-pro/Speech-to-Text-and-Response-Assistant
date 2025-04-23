import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    print("Please speak now")
    recognizer.adjust_for_ambient_noise(source)
    audio_data = recognizer.listen(source)
    print("processing")

text = recognizer.recognize_google(audio_data)
print("You Said\n",text)

engine.say("You said " + text)
engine.runAndWait()
