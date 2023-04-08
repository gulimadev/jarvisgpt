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
from requests import post



c = Main()
load_dotenv()
if __name__ == "__main__":
        # Configuração do ambiente com as credenciais e permissões necessárias
    username = os.getenv('SPOTIPY_USERNAME')
    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
    scope = "user-modify-playback-state"

    def get_token ():
        auth_string = f"{client_id}:{client_secret}"
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
        
        url = "https://accounts.spotify.com/api/token"
        
        heards = { 
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}
        result = requests.post(url, data=data, headers=heards)
        json_result = json.loads(result.content)
        token = json_result["access_token"]
        
        
    def get_auth_header(token):
        return {"Authorization": f"Bearer {token}"}
        
    def search_for_artist (token, artist_name):
        url = "https://api.spotify.com/v1/search"
        hearders = get_auth_header(token)
        query = f"q={artist_name}&type=artist&limit=1"
        query_url = f"{url}{query}"
        result = requests.get(query_url, headers=hearders)
        json_result = json.loads(result.content)
        print (json_result)        
    
    search_for_artist(get_token(), "beatles")
    token = get_token()








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