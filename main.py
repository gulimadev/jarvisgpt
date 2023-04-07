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
import requests
from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.renderers import StaticRenderer
from asciimatics.scene import Scene



class Main:

    def demo(self, screen):
        scenes = []
        effects = [
            Print(screen, StaticRenderer(images=[".", " /|\\", "/_|_\\"]), 0),
        ]
        scenes.append(Scene(effects, 2))
        effects = [
            Print(screen, StaticRenderer(images=["   |", " /|\\", "/_|_\\"]), 0),
        ]
        scenes.append(Scene(effects, 2))
        effects = [
            Print(screen, StaticRenderer(images=["___|", " /|\\", "/_|_\\"]), 0),
        ]
        scenes.append(Scene(effects, 2))
        screen.play(scenes)
        screen.print_at("Ola, Ola!", 0, 4)
        screen.refresh()
        screen.wait_for_input(10)





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
    def clima (self):
        #API_KEY = os.environ.get("CLIMA")
        API_KEY = 'ff386dfe2eef9bc4b6185ac2f3dc3932'
        #LOCATION = "sua_localizacao_aqui"
        LOCATION = "Rosario, BR"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        try:
            temperatura = data["main"]["temp"]
            descricao_clima = data["weather"][0]["description"]
            self.voz_reprodutor(f"A temperatura atual é de {temperatura:.1f} graus Celsius, na cidade de {LOCATION}")
            self.voz_reprodutor(f"A previsão do tempo é de {descricao_clima}.")
        except KeyError:
            self.voz_reprodutor(f"No momento não estou conseguindo detectar a temperatura e previsão do tempo.")