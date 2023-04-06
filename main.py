import speech_recognition as sr 
from gtts import gTTS
import pyaudio 
import time


class Main:

    def reconhecedor_voz(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Fale alguma coisa!")
            audio = r.listen(source)
        try:
            texto = r.recognize_google(audio, language='pt-BR')
            print ("Você disse: " + texto)
            return texto
        except sr.UnknownValueError:
            print ("Não entendi o que você disse!")
        except sr.RequestError as e:
            print ("Não foi possível realizar a requisição; {0}".format(e))



