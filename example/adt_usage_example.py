# import class from the module
import json
from ..music_adt import MusicADT
from ..dictionary import Dict
from plotly import graph_objects as go

example = MusicADT(1999, 2001)


def fill_adt(adt, f):
    """
    Fill the ADT corresponding to its time bounds.
    :return: None
    """
    index = 0
    with open(f, encoding='utf-8', errors="ignore") as file:
        data = json.load(file)
        for year in data.keys():
            if int(year) in range(adt.first, adt.last + 1):
                for dct in data[year]:
                    new = Dict()
                    for key in dct.keys():
                        new[key] = dct[key]
                    adt.main[index].add(new)
                index += 1


def year_bars(adt, year):
    """
    Create and open bar graph with genre info
    :param adt: MusicADT
    :param year: int
    :return: None
    """
    assert year in range(adt.first, adt.last + 1), "Chosen year is not mentioned years."
    res = dict()
    for y in range(len(adt.main)):
        if year - adt.first == y:
            for track in adt.main[y]:
                if track["Generalized Genre"]:
                    gen = str(track["Generalized Genre"])
                    if gen not in res:
                        res[gen] = 1
                    else:
                        res[gen] += 1
    trace = go.Bar(x=list(res.keys()), y=list(res.values()))
    fig = go.Figure(data=[trace])
    fig.show()


def graph_lines(adt):
    """
    Create and open a graph with full number information from ADT.
    :param adt: MusicADT
    :return: None
    """
    basic = [["rap", "hip-hop"], "pop", "country", "rock",
             "jazz", "folk", "latin", "blues", "punk", "soul",
             "pop standards", "r&b", "metal", ["house", "electronic", "trance"],
             ["ska", "reggae", "dancehall"], "rock-and-roll", "swing"]
    with open("../docs/adt_test_example.json", encoding='utf-8', errors="ignore") as file:
        data = json.load(file)
        x = list(data.keys())
    fig = go.Figure()
    for genre in basic:
        y = list()
        for year in x:
            y.append(adt.basic_genre_in_year(int(year), genre))
        fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name=str(genre)))
    fig.update_layout(title='Genre Popularity by Year',
                      xaxis_title='Year',
                      yaxis_title='Percentage')
    fig.show()


def genre_samples(adt, genre):
    """
    Print track/author names and sample link of all
    the track with given genre in the ADT.
    :param adt: MusicADT
    :param genre: str
    :return: None
    """
    for y in range(len(adt.main)):
        for track in adt.main[y]:
            if track["Generalized Genre"] == genre:
                print(track["Track"] + " By " + track["Author"], track["Sample"])


# load data into the class
fill_adt(example, "../docs/adt_test_example.json")
# project single year genre info
year_bars(example, 2000)
# project time genre info of the whole ADT
graph_lines(example)
# get some links for audio samples
# if audio had no sample link in API info, receive only the name
genre_samples(example, "r&b")
