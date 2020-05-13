"""
Butynets Danylo
Simplest example of getting all names of songs
from a web-page's top for the given year, building a
"""

import json
from urllib import request
from bs4 import BeautifulSoup
import plotly.graph_objects as go


# Currently this code works for any year
# in between 1945 and 2012. The following year require different
# approach due to another html form.
year = 2000

# Getting the html using urllib and turning into a "soup" to work with using bs4.
html = request.urlopen(f"http://billboardtop100of.com/{year}-2/")
soup = BeautifulSoup(html, 'html.parser')

top = []
# In the mentioned range of years each song of top-100
# is located in the "tr" tag. Then the block is transformed into
# strings and formed into list.
for song in soup.find_all('tr'):
    tmp_list = []
    for string in song.strings:
        if string != "\n":
            tmp_list.append(string)
    top.append(tmp_list)

# Lets visualise info we got in pie chart by the first character a song's name starts with.
chars = dict()
for song in top:
    character = song[2][0]
    if character not in chars:
        chars[character] = 1
    else:
        chars[character] += 1
labels = list(chars.keys())
values = list(chars.values())
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()


# Now lets try to keep all this info inside a json file.
data = {"data": [chars]}
with open("../docs/example.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
