# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import speech_recognition as sr

FILE = 'audio.wav'

r = sr.Recognizer()
with sr.AudioFile(FILE) as source:
    audio = r.record(source)  # read the entire audio file

#source = sr.AudioFile(FILE).__enter__()
#audio = r.record(source)

try:
    text = r.recognize_google(audio, language='ru-RU')
    print(text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))