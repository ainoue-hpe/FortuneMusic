import spotipy
import pandas as pd
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import json

client_id="023480561f7749a182e794a5ec355145"
client_secret="d5f92f42727842bbaa8d211abbee5cc2"

client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# PandasでCSVを読み込む、最初の行は省略
songs = pd.read_csv("regional-jp-daily-latest.csv", index_col = 0, header = 1)
songs.head(10)

# インデックスをリセットし、振り直す
songs = songs.reset_index()
songs.head(10)

# PandasのDataFrame作成
song_info = pd.DataFrame()

# 楽曲数分の情報を取得
for url in songs["URL"]: 
  df = pd.DataFrame.from_dict(Spotify.audio_features(url))
  song_info = song_info.append(df)
song_info.head(10)

# song_infoのインデックスを振り直す
song_info = song_info.reset_index(drop = True)
song_info.head(10)