import speech_recognition as sr
import adapter as adptr
import os

r = sr.Recognizer()

def audio_to_text():
    adptr.convert()
    msg = sr.AudioFile('audio.flac')
    with msg as source:
        audio = r.record(source)
        text = r.recognize_google(audio_data = audio, language = "it-IT")
        os.remove("audio.flac")
        return text
