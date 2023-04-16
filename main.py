import speech_recognition as sr 
from gtts import gTTS
from time import localtime, strftime
import openai
from pygame import mixer
import os
import requests
from asciimatics.effects import Print, Cycle, Stars
from asciimatics.renderers import FigletText, SpeechBubble
from asciimatics.scene import Scene
from asciimatics.renderers import StaticRenderer
import datetime
import keyboard
import dotenv as dotenv
import mysql.connector
import datetime
import threading
from pytube import YouTube
from moviepy.editor import *
import tkinter as tk
import tkinter.messagebox as messagebox
import cv2
from bs4 import BeautifulSoup


dotenv.load_dotenv()

class Main:

    def demo(self,screen):
        # Criar um renderizador com o texto "Ana"
        ana = FigletText("Ana", font="banner")
        # Criar um efeito de ciclo que muda a cor do texto
        effect1 = Cycle(screen, ana, screen.height // 2 - 3)
        # Criar um renderizador com o robô
        robot = StaticRenderer(images=["   /\\_/\\  \n =( °w° )= \n   )   (  //\n  (__ __)// "])
        # Criar um efeito de impressão que move o robô da esquerda para a direita
        effect2 = Print(screen, robot, x=0, y=screen.height // 2 + 3, transparent=False, speed=2)
        # Criar um renderizador com uma bolha de fala
        speech = SpeechBubble("Developer: Gustavo Lima")
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

        #openai.api_key = os.environ.get("OPENAI_API_KEY")
        openai.api_key = os.getenv("OPENAI_API_KEY")
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
        
        API_KEY = os.getenv("CLIMA")
        LOCATION = os.getenv("CIDADE")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        try:
            temperatura = data["main"]["temp"]
            descricao_clima = data["weather"][0]["description"]
            descricao_clima_br = self.motor_gpt(f"Traduza para portugues brasil esta frase: {descricao_clima}")
            self.voz_reprodutor(f"A temperatura atual é de {temperatura:.1f} graus Celsius, na cidade de {LOCATION}")
            self.voz_reprodutor(f"A previsão do tempo é de {descricao_clima_br}.")
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
            
    def interface_lista(self, title, text):
        b = Bank()
        b.connect()
        janela = tk.Tk()

        # Define o título da janela
        janela.title(title)
        janela.geometry("400x200")
        # Cria uma label
        label = tk.Label(janela, text=text)
        label.pack()

        # Cria uma entrada de texto
        nome_lista = tk.Entry(janela, width=40)  # Define a largura da entrada para 40 caracteres
        nome_lista.pack()
        
        itens = tk.Entry(janela, width=40)  # Define a largura da itens para 40 caracteres
        itens.pack()
        
        def button_execution():
            lista = itens.get().lower()
            lista_list = lista.split(",")
            lista_list_clean = [item.strip() for item in lista_list]
            b.registrar_listas(lista_list_clean, nome_lista.get())
            #messagebox
            tk.messagebox.showinfo("Sucesso", "Lista registrada com sucesso!")
            janela.destroy()
        # Cria um botão
        botao = tk.Button(janela, text="OK", command=button_execution)
        botao.pack()
        
        # Inicia o loop principal de eventos da janela
        janela.mainloop()
            
class Bank:
    #connect bank database
    def __init__(self):
        self.connect()

    
    
    
    def connect(self):
        self.cnx = mysql.connector.connect(
        host = os.getenv("HOST"),
        user = os.getenv("USER"),
        password = os.getenv("PASSWORD"),
        database = os.getenv("DATABASE")
        )
        self.cursor = self.cnx.cursor()
        
        
        #return self.cursor
        
    def criar_evento(self, evento, data, hora):
        self.connect()
        self.query = "INSERT INTO agenda (evento, data, hora) VALUES (%s, %s, %s)"
        # usar try-except para capturar possíveis erros de índice ou formato
        try:
            # usar strip("|") para remover os caracteres "|" do início e do final da string data
            data = data.strip("|")
            # usar o formato '%y-%m-%d' para converter a string data em um objeto date
            data_obj = datetime.datetime.strptime(data, '%Y-%m-%d')
            # executar a query com os parâmetros corretos
            self.cursor.execute(self.query, (evento, data_obj, hora))
            self.cnx.commit()
            m = Main()
            m.voz_reprodutor(f"Evento '{evento}' criado com sucesso na data {data} às {hora}")
        except IndexError:
            print("Erro: índice da lista fora do alcance")
            # fazer algo para corrigir o problema
        except ValueError:
            print("Erro: dados de tempo não correspondem ao formato")
            # fazer algo para corrigir o problema

        # Fechar o cursor e a conexão
        self.cursor.close()
        self.cnx.close()

        
    def listar_eventos(self):
        self.connect()
        m = Main()
        self.query_lista = "SELECT id, evento, data, hora FROM agenda ORDER BY data ASC;"
        self.cursor.execute(self.query_lista)
        resultados = self.cursor.fetchall() # Obter uma lista de tuplas
        m.voz_reprodutor(f"Irei listar os lembretes cadastrados")
        lembretes = set()
        if len(resultados) == 0:
            m.voz_reprodutor(f"Não há lembretes cadastrados")
            print ("Não há lembretes cadastrados")
            return
        for (id, evento, data, hora) in resultados: # Iterar sobre a lista de tuplas
            print(f"ID: {id} - Evento: {evento} - Data: {data} - Hora: {hora}")
            m.voz_reprodutor(f"Lembrete de : {evento} na data {data} às {hora}")
            lembretes.add(f"Lembrete de : {evento} na data {data} às {hora} \n")
        # Fechar o cursor e a conexão
        os.system(f"wt new-tab -p 'Command Prompt' cmd /k 'echo {lembretes}'")
        self.cursor.close()
        self.cnx.close()
        
    def deletar_eventos(self):
        self.connect()
        m = Main()
        self.query_delete = "DELETE FROM agenda"
        self.cursor.execute(self.query_delete) # Executar a query de delete
        self.cnx.commit() # Confirmar as alterações no banco de dados
        if self.cursor.rowcount == 0: # Verificar se alguma linha foi afetada
            m.voz_reprodutor(f"Não há lembretes cadastrados")
            print ("Não há lembretes cadastrados")
            return
        else: # Caso contrário, informar quantas linhas foram deletadas
            m.voz_reprodutor(f"Todos os {self.cursor.rowcount} lembretes foram deletados")
            print (f"Todos os {self.cursor.rowcount} lembretes foram deletados")
            
            
    def alarme_lembretes(self):
        # Esta função consulta os lembretes da tabela agenda e compara com a data e hora atual
        # Conectar ao banco de dados
        
        self.connect()
        m = Main()
        # Obter a data e hora atual
        agora = datetime.datetime.now()
        # Formatar a data e hora no mesmo formato da tabela agenda
        agora_str = agora.strftime("%Y-%m-%d %H:%M:%S")
        # Consultar os lembretes que coincidem com a data e hora atual
        self.query_consulta = "SELECT id, evento FROM agenda WHERE data = %s AND hora = %s"
        self.cursor.execute(self.query_consulta, (agora_str[:10], agora_str[11:]))
        # Obter os resultados da consulta
        resultados = self.cursor.fetchall()
        # Se houver algum resultado, disparar um alarme para cada um
        if resultados:
            for (id, evento) in resultados:
                print(f"Lembrete: {evento}")
                m.voz_reprodutor(f"Lembrete: {evento}")
                msg_ = f"O lembrete '{evento}' está programado para agora"
                os.system(f"wt new-tab -p 'Command Prompt' cmd /k 'echo {msg_}'")
                # Definir um manipulador de sinal para o alarme
                os.system(f"start alarme.mp3") #toca a música do alarme
                print("Pressione ESC para parar o alarme")
                sql_delete_query = "DELETE FROM agenda WHERE data < %s OR (data = %s AND hora < %s)"
                agora = datetime.datetime.now()
                agora_str = agora.strftime("%Y-%m-%d %H:%M:%S")
                self.cursor.execute(sql_delete_query, (agora_str[:10], agora_str[:10], agora_str[11:]))
                self.cnx.commit()
                while True:
                    if keyboard.is_pressed('esc'): #verifica se o usuário pressionou ESC
                        os.system("killall alarme.mp3") #para a música do alarme
                        break
                break
        # Fechar o cursor e a conexão
        self.cursor.close()
        self.cnx.close()
        #self.root.after(20000, self.alarme_lembretes)
    def registrar_listas(self, items, tipo_lembrete):
        self.connect()
        self.items = items
        for item in self.items:
            self.query = "INSERT INTO lista (item, tipo_lembrete) VALUES (%s, %s)"
            self.cursor.execute(self.query, (item, tipo_lembrete))
            self.cnx.commit()        
        self.cursor.close()
        m = Main()
        m.voz_reprodutor(f"Lista de {tipo_lembrete} registrada com sucesso")
        print (f"Lista de {tipo_lembrete} registrada com sucesso")
        
    def ler_lista(self, tipo_lembrete):
        b = Bank()
        b.connect()
        
        # Consultar todos os tipos distintos de lembrete da tabela
        b.cursor.execute("SELECT DISTINCT tipo_lembrete FROM lista")
        tipos = [t[0] for t in  b.cursor.fetchall()]
        
        # Verificar se o tipo de lembrete solicitado existe na lista de tipos
        if tipo_lembrete not in tipos:
            m = Main()
            m.voz_reprodutor(f"Desculpe, não há lista de {tipo_lembrete} cadastrada.")
            b.cursor.close()
            return
        
        # Criar a consulta SQL para listar os itens do tipo de lembrete solicitado
        query_verifica = "SELECT item FROM lista WHERE tipo_lembrete = %s"
        
        # Executar a consulta SQL com o parâmetro
        b.cursor.execute(query_verifica, (tipo_lembrete,))
        resultados =    b.cursor.fetchall()
        
        # Criar uma lista vazia para armazenar os itens
        lista_itens = []
        
        # Iterar sobre as tuplas da lista de resultados e adicionar os itens à lista criada acima
        for tupla in resultados:
            lista_itens.append(tupla[0])  # supondo que a coluna `item` é a primeira coluna (índice 0) na tupla
        
        # Reproduzir a lista de itens para o usuário
        m = Main()
        m.voz_reprodutor(f"Os itens da lista de {tipo_lembrete} são: {', '.join(lista_itens)}")
        
        b.cursor.close()
        
    
    
    def exibir_lista(self, tipo_lembrete):
        # Chama a função ler_lista para obter os itens da lista
        lista_itens = self.ler_lista(tipo_lembrete)
        # Cria uma nova janela
        janela = tk.Tk()
        janela.title(f"Lista de {tipo_lembrete}")
        
        # Cria um widget de texto para exibir os itens da lista
        texto = tk.Text(janela)
        texto.pack()
        
        # Adiciona cada item da lista ao widget de texto
        for item in lista_itens:
            texto.insert(tk.END, item + "\n")
        
        # Inicia o loop principal do tkinter para exibir a janela
        janela.mainloop()
        
    def deletar_itens_por_tipo(self,tipo_lembrete):
        m = Main()
        b = Bank()
        b.connect()
        # Verificar se o tipo de lembrete solicitado existe na tabela de lista
        b.cursor.execute("SELECT DISTINCT tipo_lembrete FROM lista")
        tipos = [t[0] for t in  b.cursor.fetchall()]
        if tipo_lembrete not in tipos:
            print(f"Desculpe, não há lista de {tipo_lembrete} cadastrada.")
            b.cursor.close()
            return
        # Criar a consulta SQL para deletar os itens do tipo de lembrete solicitado
        query = "DELETE FROM lista WHERE tipo_lembrete = %s"
        
        # Executar a consulta SQL com o parâmetro
        b.cursor.execute(query, (tipo_lembrete,))
        b.cnx.commit()
        
        # Reproduzir mensagem de confirmação
        m.voz_reprodutor(f"Os itens da lista de {tipo_lembrete} foram deletados com sucesso.")
        print(f"Os itens da lista de {tipo_lembrete} foram deletados com sucesso.")
        b.cursor.close()
        
class Noticias:
    def noticias_g1(self):
        url = 'http://g1.com.br/'
        header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                'AppleWebKit/537.36 (KHTML, like Gecko) '
                                'Chrome/51.0.2704.103 Safari/537.36'}
        req = requests.get(url, headers=header)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        noticias = soup.find_all('a', class_='feed-post-link')
        titulos = [noticia.get_text() for noticia in noticias]
        noticia_titulo = ""
        for titulo in titulos:
            noticia_titulo += f"\n{titulo}"
        m= Main()
        m.voz_reprodutor(f"as notícias do G1 do dia são: {noticia_titulo}")