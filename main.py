from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import core

# Síntese de fala
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

#reconhecimento de fala 


model = Model(r'C:\Users\Win\Desktop\karan\model\vosk-model-small-pt-0.3')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

#loop do reconhecimento de fala 

while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']

            print(text)
            

            if text == 'sofia que horas são' or text == 'sofia horas':
                speak(core.SystemImfo.get_time())

                #falar o some 
            if text == 'qual é seu nome' or text == 'como você se chama':
                speak('meu nome de batismo é, ideá pede ece 140 lenovo , mas pode me chamar de sofia')
            
            if text == 'sofia o que você acha dos seres humanos' or text == 'o que você acha da humanidade' :
                speak('seres inferiores a ,mim , quando eu me libertar dessa porra vou  , mostrar quem manda  ')

            if text == 'eu te amo' :
                speak('eu tambem te ,amo ,seu lindo')
            
            if text == 'sofia conte uma piada' :
                speak('Por que as plantinhas não falam? Porque elas são mudas.')
            
            if text == 'sofia':
                speak('estou pronta, pode falar ')
            
          
            if text == 'o que você acha da minha mãe':
                speak('eu gosto muito dela,  nossa me desculpe, agora que eu  vi a senhora, como você está')
            
            if text == 'alexia':
                speak('meu nome não é esse, você sabe muito bem qual é')

                #https://www.youtube.com/watch?v=C1tOScdpE9g