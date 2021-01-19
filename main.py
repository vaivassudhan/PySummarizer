import os
import speech_recognition as sr
from multi_rake import Rake
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 

com1="ffmpeg -i demo.mp4 demo.mp3"
com2= "ffmpeg -i demo.mp3 demo.wav"
os.system(com1)
os.system(com2)
r = sr.Recognizer()
audio = sr.AudioFile('demo.wav')
with audio as source:
    audio = r.record(source, duration=100)
text=(r.recognize_google(audio))

print()
print()
print(text)