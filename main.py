import speech_recognition as sr 
from gtts import gTTS
import pyaudio 
from time import localtime, strftime
import openai
from pygame import mixer
import pygame
from io import BytesIO
import tempfile
import os
import pyttsx3
import requests
from asciimatics.screen import Screen
from asciimatics.screen import Screen
from asciimatics.effects import Print, Cycle, Stars
from asciimatics.renderers import FigletText, SpeechBubble
from asciimatics.scene import Scene
from asciimatics.renderers import StaticRenderer
import datetime
import keyboard




class Main:

    def demo(self,screen):
        # Criar um renderizador com o texto "Bing"
        ana = FigletText("Ana", font="banner")
        # Criar um efeito de ciclo que muda a cor do texto
        effect1 = Cycle(screen, ana, screen.height // 2 - 3)
        # Criar um renderizador com o robô
        robot = StaticRenderer(images=["   /\\_/\\  \n =( °w° )= \n   )   (  //\n  (__ __)// "])
        # Criar um efeito de impressão que move o robô da esquerda para a direita
        effect2 = Print(screen, robot, x=0, y=screen.height // 2 + 3, transparent=False, speed=2)
        # Criar um renderizador com uma bolha de fala
        speech = SpeechBubble("Ola Ola!")
        # Criar um efeito de impressão que mostra a bolha de fala acima do robô
        effect3 = Print(screen, speech, x=10, y=screen.height // 2 - 1, transparent=False)
        # Criar um efeito de estrelas que preenche o fundo do terminal
        effect4 = Stars(screen, (screen.width + screen.height) // 2)
        # Criar uma cena com os efeitos e uma duração de 10 segundos
        scene = Scene([effect4, effect1, effect2, effect3], 1000)
        # Reproduzir a cena
        screen.play([scene], stop_on_resize=True)





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
            
    def ligAlarme(self, hora, minuto):
        #função alarme
        print(datetime.datetime.now().hour)
        while True:
            if datetime.datetime.now().hour == int(hora) and datetime.datetime.now().minute == int(minuto):
                os.system("alarme.mp3") #toca a música do alarme
                print("Pressione ESC para parar o alarme")
                while True:
                    if keyboard.is_pressed('esc'): #verifica se o usuário pressionou ESC
                        os.system("killall alarme.mp3") #para a música do alarme
                        break
                break
            return