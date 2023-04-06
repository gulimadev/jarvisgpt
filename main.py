import speech_recognition as sr 
from gtts import gTTS
import pyaudio 
import time
import openai


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


    def motor_gpt (self, voz):

        openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        
        response = openai.Completion.create(
            engine="davinci",
            prompt = voz,
            max_tokens=4000,
        )
        text = response.choices[0].text
        return text 
        
    def voz_reprodutor (self, texto):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        
        p = pyaudio.PyAudio()
        tts = gTTS(text=texto, lang='pt-br')
        stream = p.open(format=FORMAT, 
                        channels=CHANNELS,
                        rate=RATE,
                        output=True,
                        frames_per_buffer=CHUNK)
        
        tts.write_to_fp(stream)
        stream.stop_stream()
        p.terminate()