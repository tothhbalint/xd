import spotipy
import os
import time
from spotipy import oauth2
import sys
import spotipy.util as util
import json
import webbrowser
from PIL import Image
import requests
from io import BytesIO
import subprocess 
import psutil
import urllib.request


PORT_NUMBER = 8080
SPOTIPY_CLIENT_ID = '5d60096429124df0a47d71d98a060844'
SPOTIPY_CLIENT_SECRET = '17c0e97a5eaa442e80df170a744531bf'
SPOTIPY_REDIRECT_URI = 'http://localhost:8080'
SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'

username = sys.argv[1]
scope='user-read-private user-read-playback-state user-modify-playback-state'

temp=0

try:
    token=util.prompt_for_user_token(username,scope,SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI)
except(AttributeError):
    #os.remove(f".cache-{username}")
    token=util.prompt_for_user_token(username,scope)

spotify=spotipy.Spotify(auth=token)
track = spotify.current_user_playing_track()    
artist = track['item']['artists'][0]['name']
song = track['item']['name']
albumcover=track['item']['album']['images'][1]
url = albumcover['url']    
#print(url)
print(artist+"-"+song)
urllib.request.urlretrieve(url, ".a.jpg")


# hide image
#for proc in psutil.process_iter():
    #if proc.name() == "display":
     #   proc.kill()
