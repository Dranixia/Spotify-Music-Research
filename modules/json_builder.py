"""
Butynets' Danylo
Python 3.8
"""


import urllib.request
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dictionary import Dict
from music_adt import MusicADT


def song_clearer(name):
    """
    Return very simplified name of the artist, so that
    Spotipy could find him/her/them and his/her/their track
    with a higher chance.
    :param name: str
    :return: str
    """
    if " x " in name:
        name = name[:name.index(" x ")]
    if name == "The FiNATTiCZ ":
        name = name.replace("The ", "")
    if "&" in name.lower():
        name = name[:name.index("&")]
    if " feat" in name.lower():
        name = name[:name.lower().index(" feat")]
    if " and " in name.lower():
        name = name[:name.lower().index(" and ")]
    if "with" in name.lower():
        name = name[:name.lower().index("with")]
    if "," in name.lower():
        name = name[:name.index(",")]
    if "xa0" in name.lower():
        name = name[:name.index("xa0") - 1]
    if "/" in name.lower():
        name = name[:name.index("/")]
    if "(" in name.lower():
        name = name[:name.index("(")]
    if " by " in name.lower():
        name = name[:name.lower().index(" by ")]
    return name


def rough_genre_generalization(genres):
    """
    (list) -> tuple or str
    Generalize all tracks genres to a single basic one,
    the list of basic genres is determined earlier in the source mentioned
    on the wiki page 0.
    :return: tuple or str
    """
    basic = [("rap", "hip-hop"), "pop", "country", "rock",
             "jazz", "folk", "latin", "blues", "punk", "soul",
             "pop standards", "r&b", "metal",  ("house", "electronic", "trance"),
             ("ska", "reggae", "dancehall"), "rock-and-roll", "swing"]

    count = Dict()

    for raw in basic:
        count[raw] = 0
        if isinstance(raw, tuple):
            for subgenre in raw:
                for gen in genres:
                    if subgenre in gen:
                        count[raw] += 1
        else:
            for gen in genres:
                if raw in gen:
                    count[raw] += 1
    res = basic[0]
    for g in basic:
        if count[g] > count[res]:
            res = g
    return res


def raw_year_top(year):
    """
    Parse through the the web-page and collect all the data necessary for using
    Spotify API (artists names and their songs). Different years have different HTML markdown.
    :param year: int
    :return: list
    """
    # Year 1940 has other address than other years for some reason.
    if year == 1940:
        html = urllib.request.urlopen(f"http://billboardtop100of.com/336-2/")
    else:
        html = urllib.request.urlopen(f"http://billboardtop100of.com/{year}-2/")
    soup = BeautifulSoup(html, 'html.parser')

    yearly_top = []
    if year in [1940, 1943, 1944]:
        for songs in soup.find_all("p"):
            songs = str(songs).replace("<p>", "").replace("</p>", "").replace("\n", "").split("<br/>")
            song_list = songs
            break
        for song in song_list:
            tmp_list = list()
            tmp_list.append(song[:song.index(".")])
            tmp_list.append(song[song.index("–") + 2:])
            tmp_list.append(song[song.index(".") + 2: song.index("–") - 1])
            yearly_top.append(tmp_list)

    elif year == 1942:
        unreachable = ["41", "The Glenn Miller Orchestra",
                       "(There’ll Be Bluebirds Over) The White Cliffs of Dover"]
        for song in soup.find_all("p"):
            tmp_list = list()
            for s in song.strings:
                try:
                    if int(s[0]):
                        tmp_list.append(s[:s.index('.')])
                        tmp_list.append(s[s.index("by ") + 3:])
                        tmp_list.append(s[s.index('.') + 1: s.index(" by")])
                        yearly_top.append(tmp_list)
                        if int(s[:2]) == 40:
                            yearly_top.append(unreachable)
                except ValueError:
                    continue

    elif year == 2013:
        for songs in soup.find_all("small"):
            songs = str(songs).replace("<small>", "").replace("</small>", "").split("<br/>")
            for song in songs:
                song.replace("\n", "")
                tmp_list = list()
                tmp_list.append(song[:song.index(".")].strip())
                line = "–" if "–" in song else "-"
                tmp_list.append((song[song.index(".") + 5: song.index(line)]))
                tmp_list.append(song[song.index(line) + 2:])
                yearly_top.append(tmp_list)
        yearly_top[99][2] = "Beware"

    elif year == 2015:
        tmp_list = list()
        for s in soup.find_all("h6"):
            try:
                s = str(s).replace("<h6>", "").replace("</h6>", "")
                if s == "1":
                    raise ValueError
                if int(s) < 101:
                    yearly_top.append(tmp_list)
                    tmp_list = list()
                    tmp_list.append(s)
                else:
                    raise ValueError
            except ValueError:
                tmp_list.append(s)
        yearly_top.append(tmp_list)

    else:
        for song in soup.find_all('tr'):
            tmp_list = list()
            for string in song.strings:
                if string != "\n":
                    tmp_list.append(string)
            yearly_top.append(tmp_list)

    return yearly_top


def create_json_data():
    """
    This function is used to create results.json, it runs for about 20 minutes and collects
    data from all the web-pages and uses it together with Spotipy to create
    a json file with all the info needed.
    (Info is stored as ADT and transformed into dict for json file)
    :return: None
    """
    cid = ''
    secret = ''

    ccm = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=ccm)

    adt = MusicADT(1940, 2016)

    for year in range(1940, 2017):
        yearly = raw_year_top(year)
        top = adt.main[year - 1940]

        for song in yearly:
            final = Dict()
            final["Position"] = song[0]
            final["Author"] = song[1]
            final["Track"] = song[2]
            search_name = song_clearer(song[1])
            track_search_name = search_name + " " + song[2]

            composer = sp.search(search_name, 1, type="artist")
            track = sp.search(track_search_name, 1, type="track")

            try:
                artist_genres = composer["artists"]["items"][0]["genres"]
                final["Original Genres"] = artist_genres
                final["Generalized Genre"] = rough_genre_generalization(artist_genres)
            except IndexError:
                # Spotify might not contain info about artists genres, as such
                # they would be replaced by None.
                final["Original Genres"] = None
                final["Generalized Genre"] = None

            try:
                track_sample = track["tracks"]["items"][0]["preview_url"]
                final["Sample"] = track_sample
            except IndexError:
                # Spotify might not contain link for the track sample, as such
                # it would be replaced by None.
                final["Sample"] = None

            top.add(final)

    adt.refactor_for_json()
