import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)


engine.say("olá eu sou a karen")
engine.runAndWait()