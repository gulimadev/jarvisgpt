import speech_recognition as sr 
from gtts import gTTS
import pyaudio 
import time
import openai
from pygame import mixer
from io import BytesIO
import tempfile
import os
import pyttsx3



class Main:



    def reconhecedor_voz(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Diga algo...")
            r.adjust_for_ambient_noise(source) 
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
        print (text)
        return text 
        
    def voz_reprodutor (self, texto):
        tts = gTTS(text=texto, lang='pt-br')
        temp_file = "temp.mp3"
        if os.path.exists('temp.mp3'):
                # Excluir o arquivo
                os.remove('temp.mp3')
        tts.save(temp_file)
        mixer.init()
        mixer.music.load(temp_file)
        mixer.music.play()
        while mixer.music.get_busy():
            continue
        mixer.music.stop()
        mixer.quit()
        try:
            os.remove(temp_file)
        except:
            pass
