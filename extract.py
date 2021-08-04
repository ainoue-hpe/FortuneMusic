from os import write
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import numpy as np
import csv

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

client_id = '023480561f7749a182e794a5ec355145'
client_secret = 'd5f92f42727842bbaa8d211abbee5cc2'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="023480561f7749a182e794a5ec355145",
                                                           client_secret="d5f92f42727842bbaa8d211abbee5cc2"))



pd.set_option("display.max_rows", None, "display.max_columns", None)

songsjp = pd.read_csv("regional-jp-daily-latest.csv",header=1)
songsjp.head(200)
print (songsjp.head(200))

songsglobal = pd.read_csv("regional-global-daily-latest.csv",header=1)
# songsglobal.head(200)
# print (songsglobal.head(200))

song_info = pd.DataFrame()

# cswrite = csv.writer('spotify.csv')
# f = open('spotify.csv','w', encoding='utf-8', newline='')
# writer = csv.writer(f)

# 楽曲数分の情報を取得
# mykey = list()
# for url in songsjp["URL"]: 
#         # mykey.append(spotify.audio_features(url)[0])
#     df= pd.DataFrame.from_dict(spotify.audio_features(url))
#     print (spotify.audio_features(url))
        # writer.writerows(df)
# for row in df:
#     # df.to_csv("spotify.csv", encoding="shift_jis")
#     new_var = writer.writerows(row)
#     new_var
        
result = list()
with open('spotifyjp.csv') as f:
    # print(f.read()) 
    result = f.read()

    
    # for mykey, myvalue in df.items():
    #     print(mykey + str(myvalue))
    # print (spotify.audio_features(url))
        # print("key:" + mykey + ", values:" + myvalue)
# print(mykey)
# for a in mykey
# f.close()