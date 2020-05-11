"""
Butynets' Danylo
Python 3.8
"""


import json
from list import List
from linkedlist import Linked
from dictionary import Dict


class MusicADT:
    """
    Represent MusicADT class and it operations it can perform.
    """
    def __init__(self, first_y, last_y, fullmode=False):
        """
        Initialize empty ADT, with mentioned time bounds.
        (endbling fullmode sets maximum bounds(1940-2016))
        :param first_y: int
        :param last_y: int
        :param fullmode: bool
        """
        assert first_y < last_y and first_y in range(1940, 2017) \
               and last_y in range(1940, 2017), "Range of years is 0 or negative."
        list_size = last_y - first_y + 1
        if fullmode:
            self.full = True
            self.first = 1940
            self.last = 2017
            list_size = 77
        else:
            self.full = False
            self.first = first_y
            self.last = last_y
        self.main = List(list_size)
        for i in range(len(self.main)):
            self.main[i] = Linked()

    def fill_adt(self):
        """
        Fill the ADT corresponding to its time bounds.
        :return: None
        """
        index = 0
        with open("../docs/results.json", encoding='utf-8', errors="ignore") as file:
            data = json.load(file)
            for year in data.keys():
                if int(year) in range(self.first, self.last + 1):
                    for dct in data[year]:
                        new = Dict()
                        for key in dct.keys():
                            new[key] = dct[key]
                        self.main[index].add(new)
                    index += 1

    def years_top_genre(self, year):
        """
        Print the most popular genre of the given year and its percentage.
        :param year: int
        :return: None
        """
        assert year in range(self.first, self.last + 1), "Chosen year is not mentioned years."
        start = self.main[year - self.first].head()
        genres = Dict()
        while start is not None:
            gen = start.item["Generalized Genre"]
            if gen not in genres.keys():
                genres[gen] = 1
            else:
                genres[gen] += 1
            start = start.next
        res = genres.keys()[0]
        for genre in genres.keys():
            if genres[genre] > genres[res]:
                res = genre
        print("Genre:", res,
              "\nPercentage:", genres[res]/len(self.main[year - self.first]))

    def multiple_year_top(self, start_y, finish_y):
        """
        Print the most popular genre on the given timeline and its percentage.
        :param start_y: int
        :param finish_y: int
        :return: None
        """
        assert start_y < finish_y and start_y in range(self.first, self.last + 1)\
            and finish_y in range(self.first, self.last + 1)
        genres = Dict()
        cumulative_amount = 0
        for year in range(start_y - self.first, finish_y - self.first + 1):
            linked = self.main[year].head()
            while linked is not None:
                gen = linked.item["Generalized Genre"]
                if gen not in genres.keys():
                    genres[gen] = 1
                else:
                    genres[gen] += 1
                linked = linked.next
            cumulative_amount += len(self.main[year])
        res = genres.keys()[0]
        for genre in genres.keys():
            if genres[genre] > genres[res]:
                res = genre
        print("Genre:", res,
              "\nPercentage:", genres[res] / cumulative_amount)

    def get_whole_year(self, year):
        """
        Print info( position, author, track name) for every song in the year.
        :param year: int
        :return: None
        """
        assert year in range(self.first, self.last + 1), "Chosen year is not mentioned years."
        start = self.main[year - self.first].head()
        while start is not None:
            print(start.item["Position"], start.item["Track"] +
                  " by " + start.item["Author"])
            start = start.next

    def track_search(self, track_name):
        """
        Print all the songs, whose track name contains your given string.
        :param track_name: str
        :return: None
        """
        counter = 0
        result_dict = Dict()
        if self.full:
            for year in range(len(self.main)):
                for track in self.main[year]:
                    if track_name in track["Track"]:
                        result_dict[counter] = track["Track"] + " by " + track["Author"]
                        counter += 1
            print("Search results:")
            for i in result_dict:
                print(i)
        else:
            print("Please, reload in full mode.")

    def genre_search(self, genre):
        genre = genre.lower()
        counter = 0
        result_dict = Dict()
        if self.full:
            for year in range(len(self.main)):
                for track in self.main[year]:
                    if track["Original Genres"]:
                        for genres in track["Original Genres"]:
                            info = track["Track"] + " by " + track["Author"]
                            if genre in genres.lower():
                                result_dict[counter] = info + \
                                    "; Genres:" + str(track["Original Genres"])
                                counter += 1
                                break
            print("Search results:")
            for i in result_dict:
                print(i)

        else:
            print("Please, reload in full mode.")

    def refactor_for_json(self):
        """
        Transforms the ADT into json compatible form.
        Used once when collecting the data using Spotipy and bs4.
        :return: None
        """
        with open("../docs/results.json", mode="w", errors="ignore", encoding="utf-8") as file:
            res = dict()
            for year in range(len(self.main)):
                res[year + 1940] = []
                for song in self.main[year]:
                    song_d = dict()
                    for key in song.keys():
                        song_d[key] = song[key]
                    res[year + 1940].append(song_d)
            json.dump(res, file, ensure_ascii=False, indent=4)

    def graph(self):
        print("No")

