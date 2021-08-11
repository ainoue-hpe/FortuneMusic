import spotipy
import spotipy.util as util

#入力パート Input part
creat_playlist = 'test_list_YYY'

#認証パート Authentication part
username = 'rtwy0vflp87sqme3vs8r7q8hk'
my_id ='023480561f7749a182e794a5ec355145' #client ID
my_secret = 'd5f92f42727842bbaa8d211abbee5cc2' #client secret
redirect_uri ='http://localhost:8888/callback';
 

#アプリの権限付与に使用する
scope = 'user-library-read user-read-playback-state playlist-read-private user-read-recently-played playlist-read-collaborative playlist-modify-public playlist-modify-private'

token = util.prompt_for_user_token(username, scope, my_id, my_secret, redirect_uri)
spotify = spotipy.Spotify(auth = token)

def creat_play_list(list_name):
    spotify.user_playlist_create(username, name = list_name)
    list_data = spotify.user_playlists(user = username)
    for i in range(list_data['total']):
        play_list_name = list_data['items'][i]['name']
        if play_list_name == list_name:
            url = list_data['items'][i]['external_urls']['spotify']
        else:
            pass
    return(url)

play_list = creat_play_list(creat_playlist)
print(play_list)