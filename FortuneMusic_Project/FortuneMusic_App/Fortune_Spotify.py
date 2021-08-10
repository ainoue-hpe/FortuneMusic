import csv, operator
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import numpy as np
import random
from FortuneMusic_App import branch
from .branch import hikaku




lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

client_id = '023480561f7749a182e794a5ec355145'
client_secret = 'd5f92f42727842bbaa8d211abbee5cc2'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="023480561f7749a182e794a5ec355145",
                                                           client_secret="d5f92f42727842bbaa8d211abbee5cc2"))



#pd.set_option("display.max_rows", None, "display.max_columns", None)

#songsjp = pd.read_csv("FortuneMusic_App/csv_data/regional-jp-daily-latest.csv",header=1)

#songsgl = pd.read_csv('FortuneMusic_App/csv_data/regional-global-daily-latest.csv',header=1)

#song_info = pd.DataFrame()

#for url in songsjp["URL"]: 
    #n=spotify.audio_features(url)[0]
 
def judge(data):
    number=random.randint(0,1)
    print(number)
    if number==0:

        word=branch.hikaku(data)
        print(word)
        file_jp = pd.read_csv('FortuneMusic_App/csv_data/日本TOP200.csv')
        file_sort_jp = file_jp.sort_values('%s' % word,ascending=False)
        file_URL_jp = file_sort_jp.loc[:,'URL']
        kekka=('\n'.join(file_URL_jp.to_list()))
        print('\n'.join(file_URL_jp.to_list()))


    elif number==1:
        word=branch.hikaku(data)
        print(word)
        file_gl = pd.read_csv('FortuneMusic_App/csv_data/グローバルTOP200.csv')
        file_sort_gl = file_gl.sort_values('%s' % word,ascending=False)
        file_URL_gl = file_sort_gl.loc[:,'URL']
        kekka=('\n'.join(file_URL_gl.to_list()))
        print('\n'.join(file_URL_gl.to_list()))

    return kekka