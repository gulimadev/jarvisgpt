from main import Main, Bank
from asciimatics.screen import Screen
from app import validador
from dotenv import load_dotenv
import spotipy
from spotipy import oauth2, SpotifyOAuth
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import os
from playsound import playsound
from requests import post
import datetime
from pytube import YouTube
from pydub import AudioSegment



c = Main()
load_dotenv()
if __name__ == "__main__":
    #url = 'https://www.youtube.com/watch?v=LVbUNRwpXzw&t=1310s'
    #video = YouTube(url)
    #video.streams.get_highest_resolution().download()
    video = AudioSegment.from_file("Music for Productive Work — Tony Starks Concentration Mix.mp4", format="mp4")

    # Extraia o áudio do arquivo de vídeo
    audio = video.set_channels(1)  # converte para um canal de áudio mono
    audio = audio.set_frame_rate(44100)  # ajusta a taxa de amostragem para 44100 Hz (padrão do MP3)

    # Salve o arquivo de áudio MP3
    audio.export("audio.mp3", format="mp3")

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