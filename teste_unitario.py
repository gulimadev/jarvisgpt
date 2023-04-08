from main import Main
from asciimatics.screen import Screen
from app import validador
import dotenv as dotenv
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
dotenv.load_dotenv()
if __name__ == "__main__":
        # Configuração do ambiente com as credenciais e permissões necessárias
    # username = os.getenv('SPOTIFY_USERNAME')
    # client_id = os.getenv('SPOTIPY_CLIENT_ID')
    # client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
    

    # Autenticação do Spotify
    # auth_response = requests.post('https://accounts.spotify.com/api/token', {
    #     'grant_type': 'client_credentials',
    #     'client_id': client_id,
    #     'client_secret': client_secret,
    # })

    client_id = 'eec7c8bec93d4edf9544ee6326994042'
    client_secret = 'ef55a7e8348a47d4b5c4f6e389c18217'
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