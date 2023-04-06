import speech_recognition as sr 
from gtts import gTTS
import pyaudio 
import time
import openai
from pygame import mixer
from io import BytesIO
import tempfile
import os


class Main:

    def reconhecedor_voz(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("E so chamar JARVIS")
            audio = r.listen(source)
        try:
            texto = r.recognize_google(audio, language='pt-BR')
            print ("Você disse: " + texto)
            return texto
    
        except sr.UnknownValueError:
            print ("Não entendi o que você disse!")
        except sr.RequestError as e:
            print ("Não foi possível realizar a requisição; {0}".format(e))


    def motor_gpt (self, voz):

        openai.api_key = os.environ.get("OPENAI_API_KEY")
        
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt = voz,
            max_tokens=3900,
        )
        text = response.choices[0].text
        return text 
        
    def voz_reprodutor (self, texto):
        tts = gTTS(text=texto, lang='pt-br')
        temp_file = "temp.mp3"
        tts.save(temp_file)
        mixer.init()
        mixer.music.load(temp_file)
        mixer.music.play()
        while mixer.music.get_busy():
            continue
        os.remove(temp_file)