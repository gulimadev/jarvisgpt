import main as Main
import os
from datetime import datetime
import threading
from asciimatics.screen import Screen
import re
import dotenv as dotenv
import spotipy
import spotipy.util as util

c = Main.Main()
dotenv.load_dotenv()
man = "Gustavo"
ia = "ana"
comandos_windows = {
    "navegador": "start chrome",
    "explorador": "start explorer",
    "bloco de notas": "start notepad",
    "painel de controle": "control",
    "desligar computador": "shutdown /s /t 0",
    "reiniciar computador": "shutdown /r /t 0",
    "Spotify": "start spotify",
    "calculadora": "start calc",
    "Microsoft Word": "start winword",
    "Excel": "start excel",
    "PowerPoint": "start powerpnt",
    "Outlook": "start outlook",
    "Paint": "start mspaint",
    "Adobe Reader": "start acrord32",
    "Windows Media Player": "start wmplayer",
    "Skype": "start skype",
    "Zoom": "start zoom",
    "Google Drive": "start https://drive.google.com",
    "OneDrive": "start https://onedrive.live.com",
    "Bing": "start https://www.bing.com/search?q=",
    "Google": "start https://www.google.com/search?q=",
    "pesquise YouTube": "start https://www.youtube.com/results?search_query=",
    "vscode": "start code",
    "site" : "https://www.google.com/search?q=",
    "chat" : "start https://chat.openai.com/chat",
    "acorda" : "start code & start spotify & start https://chat.openai.com/chat & start https://www.bing.com/chat",
    "horas" : "que horas sao",
    "quem" : "teste",
}

def execucao():
    while True:
        validador(c.reconhecedor_voz())


def validador (voz):
    palavras = []
    try:
        palavras = voz.lower().split()
        if palavras:
            print (f" Este ======={palavras}")
    except AttributeError:
        print ("variavel 'voz' vazia")
        execucao()
    print(voz)
    if ia in palavras and "alarme" in palavras:
        c.voz_reprodutor(f"Para que horas deseja definir o alarme?")
        voz_g = c.reconhecedor_voz()
        padrao = r"(\d+):(\d+)" # padrão para extrair a hora e o minuto
        resultado = re.search(padrao, voz_g) # busca pelo padrão no texto
        if resultado: # se encontrou uma correspondência
            hora = resultado.group(1) # obtém o primeiro grupo de captura (hora)
            minuto = resultado.group(2) # obtém o segundo grupo de captura (minuto)
            print(f"Hora: {hora}, Minuto: {minuto}") # imprime os valores extraídos
            thread_alarme = threading.Thread(target=c.ligAlarme, args=(hora, minuto))
            # inicia a thread
            thread_alarme.start()
            execucao()
        else: # se não encontrou uma correspondência
            print("Não foi possível extrair a hora e o minuto do texto")
        
    elif ia in palavras and "modo" in palavras:
        resp = input ("Digite o que deseja? \n")
        validador(resp)
    
    elif ia in palavras and "significa" in palavras:
        c.voz_reprodutor(c.motor_gpt(voz))
    elif ia in palavras and "traduza" in palavras:        
        c.voz_reprodutor(c.motor_gpt(voz))
    elif ia in palavras and "calcule" in palavras:
        c.voz_reprodutor(c.motor_gpt(voz))      
    elif ia in palavras and "buscar" in palavras or "busca" in palavras and "youtube" in palavras:
        index = palavras.index("youtube") + 1
        pesquisa = "+".join(palavras[index:])
        index_voz = palavras.index("youtube") + 1
        pesquisa_voz = " ".join(palavras[index_voz:])
        url = f"https://www.youtube.com/results?search_query={pesquisa}"
        os.system(f"start {url}")
        c.voz_reprodutor(f"Ok, {man}, estou pesquisando {pesquisa_voz} no Youtube.")
    
    elif "oi" in palavras and ia in palavras:
        print ("Oi eu estou te ouvindo!")
        c.voz_reprodutor(f"Oi {man}, eu estou te ouvindo!")
        
        c.voz_reprodutor(c.motor_gpt(c.reconhecedor_voz()))
        #del palavras
        execucao()
        
    else:
        for chave, valor in comandos_windows.items():
            #print (f"Esta e a chave que estou olhando: {chave.lower()}")
            chave_temporaria = chave.lower().split()
            for chaves in chave_temporaria:
                if chaves in [palavra for palavra in palavras] and "ana" in palavras:
                    if chaves in ["site"]:
                        index = palavras.index("site") + 1
                        pesquisa = "+".join(palavras[index:])
                        index_voz = palavras.index("site") + 1
                        pesquisa_voz = " ".join(palavras[index_voz:])
                        url = f"https://www.google.com/search?q={pesquisa}"
                        os.system(f"start {url}")
                        c.voz_reprodutor(f"Ok, {man}, estou pesquisando {pesquisa_voz} no Google.")
                        execucao()
                    elif chaves in ["acorda"]:
                        c.voz_reprodutor(f"Ok, {man}, vamos começar os trabalhos !!!")
                        os.system(valor)
                        os.system("wt ping 1.1.1.1 -n 99999999")
                        execucao()
                    elif chaves in ["horas"]:
                        now = datetime.now()
                        hora = now.strftime("%H:%M:%S")
                        c.voz_reprodutor(f"Agora são {hora}.")
                        c.clima()
                        execucao()    
                    elif chaves in ["quem"]:
                        c.voz_reprodutor(f"Olá! Eu sou a Ana, 'Inteligência Artificial', desenvolvida pelo Dev: Gustavo Lima.")
                        execucao()
                    c.voz_reprodutor(f" Ok, {man} estou executando: {chave}")
                    os.system(valor)#del palavras
                    execucao()              
        execucao()
        
        
def animacao():
    Screen.wrapper(c.demo)



if __name__ == "__main__":
    anime = threading.Thread(target=animacao)
    anime.start()
    execucao()