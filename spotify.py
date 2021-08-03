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
# songsjp.head(200)
# print (songsjp.head(200))

songsjp = pd.read_csv("regional-global-daily-latest.csv",header=1)
# songsjp.head(200)
# print (songsjp.head(200))

song_info = pd.DataFrame()
# 楽曲数分の情報を取得
for url in songsjp["URL"]: 
    # df= pd.DataFrame.from_dict(spotify.audio_features(url), index=spotify.audio_features.keys())
    print (spotify.audio_features(url))
    # [0], index=[0]



# results = sp.search(q='japantop50', limit=20,type='playlist')
# for idx, track in enumerate(results['artist']['name']):
#     print(idx, track['artist']['name'])

#     song_info = songsjp.append(df)
# song_info.head(10)
# print(song_info.head(10))
# songsjp = pd.DataFrame() # 空のdfを作成



# for url in songsjp["URL"]: # jp_dailyのURL列を1つずつなめる
#    a = pd.DataFrame.from_dict(spotify.audio_features(url)) # URLに該当する曲の特徴を抽出
#    songsjp = songsjp.append(a) # 読み込んだ特徴を行へ追加

# songsjp = songsjp.reset_index(drop=True)



#songs=np.arange(1000).reshape((200,5))
#np.set_printoptions(threshold=np.inf)

# pd.set_option("display.max_rows",None)

#for track in songs['tracks']:
#  print(track)

# songsgl = pd.read_csv("regional-global-daily-latest.csv",header=1)
# songsgl.head(200)
# print (songsgl.head(200))

# songs_info_jp = pd.DataFrame()
# for url in songsjp["URL"]: 
#   df = pd.DataFrame.from_dict(spotify.audio_features(url))
#   songs_info_jp= songs_info_jp.append(df)
# songs_info_jp.head(10)

# songs_info_jp = songs_info_jp.reset_index(drop = True)
# songs_info_jp.head(10)


# df = pd.DataFrame
# df.head()



# def track_features(track_ids, limit = 20):
#     return pd.DataFrame(sp.audio_features(track_ids))

# print(track_features(track_info()['track_id']).drop(['track_href', 'analysis_url', 'id', 'uri'], axis=1))




