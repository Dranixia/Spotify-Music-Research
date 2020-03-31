"""
Оскільки неможливо напряму визначити жанри,
ми будемо дивитися на жанрову класифікацію виконавця
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# entering our client_id and client_secret id
# https://developer.spotify.com/dashboard/applications
# create app and copy your keys here
cid = ''
secret = ''

# gaining access to all the public data using our ids
ccm = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=ccm)

# a random band and track names
name = "amon amarth first kill"

# searching for the track in a Spotify browser
track = sp.search(name, 1, 0)

# access the uri of the band
artist_uri = track['tracks']['items'][0]['artists'][0]['id']

# using artist's URI to get info about him/her/them in json
artist_json = sp.artist(artist_uri)

# which contains info about genres of this band
print(artist_json['genres'])
