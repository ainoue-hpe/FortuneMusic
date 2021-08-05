import csv, operator
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import numpy as np

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

client_id = '023480561f7749a182e794a5ec355145'
client_secret = 'd5f92f42727842bbaa8d211abbee5cc2'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="023480561f7749a182e794a5ec355145",
                                                           client_secret="d5f92f42727842bbaa8d211abbee5cc2"))



pd.set_option("display.max_rows", None, "display.max_columns", None)

songsjp = pd.read_csv("regional-jp-daily-latest.csv",header=1)

songsgl = pd.read_csv("regional-global-daily-latest.csv",header=1)

song_info = pd.DataFrame()

for url in songsjp["URL"]: 
    n=spotify.audio_features(url)[0]
 
file_jp = pd.read_csv('日本TOP200.csv')
file_sort_jp = file_jp.sort_values('danceability')
file_URL_jp = file_sort_jp.loc[:,'URL']

print(file_URL_jp)

file_gl = pd.read_csv('グローバルTOP200.csv')
file_sort_gl = file_gl.sort_values('danceability')
file_URL_gl = file_sort_gl.loc[:,'URL']

print(file_URL_gl)