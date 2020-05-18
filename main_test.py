"""
Butynets' Danylo
Python 3.8
"""

from time import sleep
from music_adt import MusicADT


def main():
    print("Welcome to the Music Genre research program."
          "This is a quick tutorial to demonstrate capabilities of"
          "this ADT and results of working with Spotify API.\n"
          "If you are asked to enter any number or number from"
          "specific range, please follow the instructions, as this"
          "program was developed for other purposes.")
    full = input("Type anything if you want to activate fullmode."
                 "It would take whole database for operations."
                 "If you want to manually enter the time period in years, "
                 "just press ENTER.\n")
    if full:
        adt = MusicADT(1940, 2016, fullmode=full)
        adt.fill_adt("../docs/results.json")
        print("First, searching by track.")

        print("Enter the name of the track you want to find. "
              "Warning! This feature requires accuracy with input!")
        track = input()
        adt.track_search(track)

        print("\n\n\nNow let's try entering a genre to find songs that match it. "
              "Warning! This feature requires accuracy with input!")
        genre = input()
        adt.genre_search(genre)

        print("\n\n\nNow the graphic time.")
        sleep(3)
        adt.graph()
    else:
        low = int(input("Enter lower year you are aiming for (1940 - 2016).\n"))
        high = int(input("Enter higher year you are aiming for (1940 - 2016).\n"))
        while low and high not in range(1940, 2017):
            low = int(input("Enter lower year bound you are aiming for (1940 - 2016).\n"))
            high = int(input("Enter higher year bound you are aiming for (1940 - 2016).\n"))
        adt = MusicADT(low, high)
        adt.fill_adt("../docs/results.json")
    print("\n\n\nNow enter the year(1940-2016 if fullmode, your bounds otherwise). You will get "
          "the top trending genre of that year.")
    year = int(input())
    adt.years_top_genre(year)

    print("\n\n\nSleep fo 10 seconds. Now let's see the whole info about the year you mentioned.")
    sleep(10)
    adt.get_whole_year(year)

    print("\n\n\nFinally enter 2 years considering the corresponding bounds, this will provide"
          "you with the most popular genre on the entire time period.")
    year_1 = int(input("Enter lower year:"))
    year_2 = int(input("Enter higher year:"))
    adt.multiple_year_top(year_1, year_2)

    print("\n\n\nThat is it for now, you can continue researching "
          "this program by looking at open source code of mine.")


if __name__ == '__main__':
    main()
