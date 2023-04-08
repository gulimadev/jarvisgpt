from main import Main
from asciimatics.screen import Screen
from app import validador
from dotenv import load_dotenv
import pygame
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import os
from playsound import playsound
import requests
import requests_oauthlib
import json
import base64



c = Main()
load_dotenv()
if __name__ == "__main__":
        # Configuração do ambiente com as credenciais e permissões necessárias
    username = os.getenv('SPOTIPY_USERNAME')
    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')


    scope = "user-modify-playback-state"

    client_creds = f'{client_id}:{client_secret}'
    client_creds_64 = base64.b64encode(client_creds.encode())

    token_data = {
        'grant_type': 'authorization_code',
        'code': 'AQD0yXvFEOvw',
        'redirect_uri': 'http://localhost:8888/callback'
    }

    token_header = {
        'Authorization': f'Basic {client_creds_64.decode()}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post('https://accounts.spotify.com/api/token', data=token_data, headers=token_header)



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