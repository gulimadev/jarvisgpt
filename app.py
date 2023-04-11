import main as Main
import os
from datetime import datetime
import datetime
import threading
from asciimatics.screen import Screen
import re
import dotenv as dotenv
import openai
import time


c = Main.Main()
dotenv.load_dotenv()
man = "Gustavo"
ia = "ana"
comandos_windows = {
    "navegador": "start chrome",
    "explorador": "start explorer",
    "bloco": "start notepad",
    "painel de controle": "control",
    "desligar computador": "shutdown /s /t 0",
    "reiniciar computador": "shutdown /r /t 0",
    "dormir computador": "powercfg /hibernate on",
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
    elif ia in palavras and "calcule" in palavras or "calcula" in palavras:
        c.voz_reprodutor(c.motor_gpt(voz))  
    elif ia in palavras and "converta" in palavras:
        c.voz_reprodutor(c.motor_gpt(voz))  
            
    elif ia in palavras and "download" in palavras:
        b = Main.Bank()
        c.voz_reprodutor("Iniciando modo download")
        arg = r"wt new-tab -p 'windows-terminal' cmd /k python C:\Users\guuhf\Desktop\projetos\jarvisgpt\download.py"
        terminal = threading.Thread(target=os.system, args=(arg,))
        terminal.start()
    elif (ia in palavras) and ("buscar" in palavras or "busca" in palavras or "procure" in palavras) and "youtube" in palavras:
        index = palavras.index("youtube") + 1
        pesquisa = "+".join(palavras[index:])
        index_voz = palavras.index("youtube") + 1
        pesquisa_voz = " ".join(palavras[index_voz:])
        url = f"https://www.youtube.com/results?search_query={pesquisa}"
        os.system(f"start {url}")
        c.voz_reprodutor(f"Ok, {man}, estou pesquisando {pesquisa_voz} no Youtube.")
    
    elif "lembre" in palavras or "lembra" in palavras and "de" in palavras:
        agora = datetime.datetime.now()
        data_formatada = agora.strftime("%Y-%m-%d %H:%M:%S")
        print(data_formatada)
        prompt_personalizado = f"Baseado na data de hoje:{data_formatada},calcule: Por favor crie um event com a mensagem: 'Sua mensagem aqui' e a data/hora: 'YYYY-MM-DD HH:MM:SS'.:{voz}, pode substituir a msg anterior confirme solicitado. Sua resposta deve ser em formato de tabela, com duas colunas: uma para a mensagem do evento e outra para a data/hora do evento. Aqui está um exemplo do formato esperado:\n\n|Mensagem|Data/Hora|\n|Exemplo|YYYY-MM-DD HH:MM:SS|" 
        try:
            resposta = c.motor_gpt(prompt_personalizado)
        # Imprimir a string resposta
        
        except openai.error.InvalidRequestError:
            c.voz_reprodutor("Desculpe, mensagem muito grande, poderia repetir?")
            execucao()
        try:
            print(resposta)
        except UnboundLocalError:
            print("Erro variavel resposta")
            execucao()
        # Remover os caracteres \n e | do início e do final da string resposta
        resposta = resposta.strip("\n|")

        # Imprimir a lista resultante do método split("|")
        print(resposta.split("|"))

        # Extrair o evento da string resposta
        evento = resposta.split("|")[0]

        # Extrair a data e a hora da string resposta
        data_hora = resposta.split("|")[1]

        # Imprimir a lista resultante do método split()
        print(data_hora.split())

        # Dividir a data e a hora em duas strings separadas
        data = data_hora.split()[0]
        hora = data_hora.split()[1]

        # Imprimir as strings evento, data e hora
        print(evento)
        print(data)
        print(hora)

        # Criar uma instância da classe Bank
        b = Main.Bank()

        # Chamar a função criar_evento com os parâmetros corretos
        b.criar_evento(evento, data, hora)
    elif ("ler" in palavras or "lista" in palavras or "liste"  in palavras  or "listar" in palavras) and ("lembretes" in palavras or "lembrete" in palavras):
        b = Main.Bank()
        b.listar_eventos()
        execucao()
    elif ("deleta" in palavras or "deletar" in palavras or "apagar" in palavras) and ("lembretes" in palavras or "lembrente" in palavras):
            b = Main.Bank()
            while True:    
                c.voz_reprodutor("Você tem certeza que deseja deletar todos os lembretes?")
                try:
                    confirma = c.reconhecedor_voz().lower()
                except AttributeError:
                    confirma = c.reconhecedor_voz().lower()
                conf = confirma.split()
                if "sim" in conf:
                    b.deletar_eventos()
                    execucao()
                elif "não" in conf:
                    c.voz_reprodutor("Ok, não irei deletar os lembretes")
                    execucao()
    elif ia in palavras and "criou" in palavras:
        c.voz_reprodutor(f"Quem me criou foi o Developer: Gustavo Lima")
    elif ia in palavras and "receita" in palavras:
        resposta_receita = c.motor_gpt(f"irei Te chamar de {ia} e te pedir uma receita:{voz}")
        with open("receitas.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(resposta_receita)
            arquivo.close()
        os.system("start receitas.txt")
        c.voz_reprodutor(resposta_receita)
    
    elif ia in palavras and "netflix" in palavras:
        c.voz_reprodutor("Ok, estou abrindo o Netflix")
        os.system("start https://www.netflix.com/browse")
    
    elif ia in palavras and "registrar" in palavras or "registra" in palavras or "cadastra" in palavras and "lista" in palavras:
        
        m = Main.Main()
        m.voz_reprodutor("Ok, o que deseja registrar?")
        #execute interface grafica para registrar lista
        m.interface_lista("Registrar Lista", "Digite os itens da lista separados por virgula")
    elif ia in palavras and "ver" in palavras and "lista" in palavras or "listas" in palavras:
        b = Main.Bank()
        index = palavras.index("lista") + 1
        ver =" ".join(palavras[index:])
        b.exibir_lista(ver) #exemplo: ana ver minhas listas compras, roupas, items
        
    elif ia in palavras and "deletar" in palavras or "deleta" in palavras and "minha" in palavras and "lista" in palavras:
        b = Main.Bank()
        index = palavras.index("lista") + 1
        ver =" ".join(palavras[index:])
        b.deletar_itens_por_tipo(ver)
    elif "oi" in palavras and ia in palavras:
        print ("Oi eu estou te ouvindo!")
        c.voz_reprodutor(f"Oi {man}, eu estou te ouvindo!")
        agora = datetime.datetime.now()
        data_formatada = agora.strftime("%Y-%m-%d %H:%M:%S")
        c.voz_reprodutor(c.motor_gpt(f" Data atual: {data_formatada}{c.reconhecedor_voz()}"))
        #del palavras
        execucao()
        
    else:
        for chave, valor in comandos_windows.items():
            #print (f"Esta e a chave que estou olhando: {chave.lower()}")
            chave_temporaria = chave.lower().split()
            for chaves in chave_temporaria:
                if chaves in [palavra for palavra in palavras] and ia in palavras:
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
                        now = datetime.datetime.now()
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

def string_para_datetime(string_data_hora, formato):


        return datetime.strptime(string_data_hora, formato) # converte a string em um objeto datetime

if __name__ == "__main__":
    def alarme():
        b = Main.Bank()
        while True:
            b.alarme_lembretes()
    
    anime = threading.Thread(target=animacao)
    lembrete = threading.Thread(target=alarme)
    anime.start()
    lembrete.start()
    execucao()
