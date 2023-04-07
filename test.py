import main as Main
import os
from datetime import datetime
from multiprocessing import Process
import time
from asciimatics.screen import Screen



c = Main.Main()

man = "Gustavo"
comandos_windows = {
    "navegador": "start chrome",
    "explorador de arquivos": "start explorer",
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
    "YouTube": "start https://www.youtube.com/results?search_query=",
    "vscode": "start code",
    "site" : "https://www.google.com/search?q=",
    "chat" : "start https://chat.openai.com/chat",
    "acorda" : "start code & start spotify & start https://chat.openai.com/chat & start https://www.bing.com/chat",
    "horas" : "que horas sao",
    "quem" : "teste",
}


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
    if "oi" in palavras and "ana" in palavras:
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
            print ("Continuo escutando")
        #del palavras 
        #del voz
        execucao()
        
        
def animacao():
    Screen.wrapper(c.demo)

# def execucao():
#     while True:
#         # criando processos para executar as funções
#         processo_validador = Process(target=validador, args=c.reconhecedor_voz())
#         processo_animacao = Process(target=animacao) # usar a função animacao em vez de lambda
#         # iniciando os processos
#         processo_animacao.start()
#         processo_validador.start()

#         # esperando os processos terminarem
#         processo_animacao.join()
#         processo_validador.join()

# #execucao()

def execucao():
    while True:
        validador(c.reconhecedor_voz())


execucao()