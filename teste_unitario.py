import platform

if __name__ == "__main__":

    


# Obter o nome do sistema operacional
    print(platform.system())

    # Obter a versão do sistema operacional
    print(platform.version())

        
    
    
    # b = Bank()
    # def ler_lista_filtrada( tipo_lembrete, busca):
        
    #     b.connect()
    #     tipo_lembrete = tipo_lembrete
        
    #     palavras = busca.split()  # separar as palavras da string de busca
        
    #     # criar uma lista vazia para armazenar as condições da consulta SQL
    #     condicoes = []
        
    #     # adicionar uma condição para cada palavra da busca, usando a sintaxe LIKE '%palavra%'
    #     for palavra in palavras:
    #         condicoes.append("item LIKE %s")
        
    #     # juntar todas as condições com o operador OR
    #     condicoes_sql = " OR ".join(condicoes)
        
    #     # criar a consulta SQL com as condições da busca
    #     query_verifica = f"SELECT * FROM lista WHERE tipo_lembrete = %s AND ({condicoes_sql})"
        
    #     # executar a consulta SQL com os parâmetros
    #     parametros = [  tipo_lembrete] + [f"%{palavra}%" for palavra in palavras]  # criar uma lista com os parâmetros da consulta SQL
    #     b.cursor.execute( query_verifica, parametros)
    #     resultados =    b.cursor.fetchall()  # Obter uma lista de tuplas
        
    #     # criar uma lista vazia para armazenar os itens da coluna `lembrete`
    #     lista_itens = []
        
    #     # iterar sobre as tuplas da lista de resultados e adicionar os itens à lista criada acima
    #     for tupla in resultados:
    #         lista_itens.append(tupla[1])  # supondo que a coluna `lembrete` é a segunda coluna (índice 1) na tupla
        
    #     # reproduzir a lista de itens para o usuário
    #     m = Main()
    #     m.voz_reprodutor(f"Os itens da lista de {tipo_lembrete} que correspondem à busca {busca} são: {', '.join(lista_itens)}")
        
    #     b.cursor.close()
    # #palavras = [""]
    
    
    # def ler_lista(tipo_lembrete):
    #     b.connect()
        
    #     # Consultar todos os tipos distintos de lembrete da tabela
    #     b.cursor.execute("SELECT DISTINCT tipo_lembrete FROM lista")
    #     tipos = [t[0] for t in  b.cursor.fetchall()]
        
    #     # Verificar se o tipo de lembrete solicitado existe na lista de tipos
    #     if tipo_lembrete not in tipos:
    #         m = Main()
    #         m.voz_reprodutor(f"Desculpe, não há lista de {tipo_lembrete} cadastrada.")
    #         b.cursor.close()
    #         return
        
    #     # Criar a consulta SQL para listar os itens do tipo de lembrete solicitado
    #     query_verifica = "SELECT item FROM lista WHERE tipo_lembrete = %s"
        
    #     # Executar a consulta SQL com o parâmetro
    #     b.cursor.execute(query_verifica, (tipo_lembrete,))
    #     resultados =    b.cursor.fetchall()
        
    #     # Criar uma lista vazia para armazenar os itens
    #     lista_itens = []
        
    #     # Iterar sobre as tuplas da lista de resultados e adicionar os itens à lista criada acima
    #     for tupla in resultados:
    #         lista_itens.append(tupla[0])  # supondo que a coluna `item` é a primeira coluna (índice 0) na tupla
        
    #     # Reproduzir a lista de itens para o usuário
    #     m = Main()
    #     m.voz_reprodutor(f"Os itens da lista de {tipo_lembrete} são: {', '.join(lista_itens)}")
        
    #     b.cursor.close()
        
    
    
    # def exibir_lista(tipo_lembrete):
    #     # Chama a função ler_lista para obter os itens da lista
    #     lista_itens = ler_lista(tipo_lembrete)
    #     # Cria uma nova janela
    #     janela = tk.Tk()
    #     janela.title(f"Lista de {tipo_lembrete}")
        
    #     # Cria um widget de texto para exibir os itens da lista
    #     texto = tk.Text(janela)
    #     texto.pack()
        
    #     # Adiciona cada item da lista ao widget de texto
    #     for item in lista_itens:
    #         texto.insert(tk.END, item + "\n")
        
    #     # Inicia o loop principal do tkinter para exibir a janela
    #     janela.mainloop()
    #     #busca = " ".join(palavras)  # juntar todas as palavras em uma única string
    #     #ler = ler_lista(tipo_lembrete="casa dos pais", busca=busca)  # passar a string como um único parâmetro
    # m = Main()
    # lista = m.reconhecedor_voz()
    # lista_ler = lista.split()
    # index = lista_ler.index("lista") + 1
    # ver =" ".join(lista_ler[index:])
    # ler = exibir_lista(ver)
    
    #url = 'https://www.youtube.com/watch?v=LVbUNRwpXzw&t=1310s'
    #video = YouTube(url)
    #video.streams.get_highest_resolution().download()
    # video = AudioSegment.from_file("Music for Productive Work — Tony Starks Concentration Mix.mp4", format="mp4")

    # # Extraia o áudio do arquivo de vídeo
    # audio = video.set_channels(1)  # converte para um canal de áudio mono
    # audio = audio.set_frame_rate(44100)  # ajusta a taxa de amostragem para 44100 Hz (padrão do MP3)

    # Salve o arquivo de áudio MP3
    

    


    #     # Configuração do ambiente com as credenciais e permissões necessárias
    # agora = datetime.datetime.now()
    # data_formatada = agora.strftime("%Y-%m-%d %H:%M:%S")
    # print(data_formatada)


    # os.environ['SPOTIPY_REDIRECT_URI']
    # username = os.getenv('SPOTIPY_USERNAME')
    # client_id = os.getenv('SPOTIPY_CLIENT_ID')
    # client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
    # scope = "user-modify-playback-state"

    # redirect_uri = 'http://localhost/'

    # token = util.prompt_for_user_token(username, client_id,
    #                                 client_secret, redirect_uri)
    # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(token=token))
    # results = sp.search(q='Despacito Luis Fonsi', type='track')
    # track_uri = results['tracks']['items'][0]['uri']
    # sp.start_playback(uris=[track_uri])







    # # Obter uma autorização do Spotify usando o protocolo OAuth 2.0
    # oauth = requests_oauthlib.OAuth2Session(client_id, scope=scope)
    # authorization_url, state = oauth.authorization_url("https://accounts.spotify.com/authorize")
    # print("Acesse esse link no seu navegador: ", authorization_url)
    # authorization_response = input("Digite a URL completa que você foi redirecionado: ")
    # token = oauth.fetch_token("https://accounts.spotify.com/api/token", authorization_response=authorization_response, client_secret=client_secret)

    # # Obter o token de acesso
    # access_token = token["access_token"]

    # # Definir o cabeçalho para autenticação nas requisições da API do Spotify
    # headers = {
    #     "Authorization": f"Bearer {access_token}"
    # }

    # # Definir o endpoint e os parâmetros para o método play
    # endpoint = "https://api.spotify.com/v1/me/player/play"
    # params = {
    #     "context_uri": "spotify:album:5ht7ItJgpBH7W6vJ5BqpPr" # Exemplo de um álbum do Beatles
    # }

    # # Fazer uma requisição PUT para a API do Spotify usando o método play
    # response = requests.put(endpoint, headers=headers, params=params)

    # # Verificar se a requisição foi bem sucedida
    # if response.status_code == 204:
    #     print("Música reproduzida com sucesso!")
    # else:
    #     print("Ocorreu um erro ao reproduzir a música.")