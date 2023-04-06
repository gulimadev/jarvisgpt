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
            print("Diga algo...")
            audio = r.listen(source)
            print("Áudio captado.")
        try:
            texto = r.recognize_google(audio, language='pt-BR')
            print("Texto reconhecido: " + texto)
            return texto
        except sr.UnknownValueError:
            print("Não foi possível reconhecer o áudio.")
        except sr.RequestError as e:
            print("Erro na conexão com a API de reconhecimento de voz: " + str(e))





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