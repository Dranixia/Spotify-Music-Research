"""
Butynets Danylo
Simplest example of getting all names of songs
from a web-page's top for the given year.
"""


from urllib import request
from bs4 import BeautifulSoup

# currently this code works for any year
# in between 1945 and 2012. The following year require different
# approach due to another html form.
year = 2000

# getting the html and turning into a "soup" to work with using bs4
html = request.urlopen(f"http://billboardtop100of.com/{year}-2/")
soup = BeautifulSoup(html, 'html.parser')

top = []
# in the mentioned range of years each song of top-100
# is located in the "tr" tag. Then the block is transformed into
# strings and formed into list.
for song in soup.find_all('tr'):
    tmp_list = []
    for string in song.strings:
        if string != "\n":
            tmp_list.append(string)
    top.append(tmp_list)

print(top)
