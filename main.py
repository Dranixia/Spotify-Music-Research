"""
Butynets' Danylo
Python 3.8
"""


import sys
from time import sleep
from music_adt import MusicADT


class Menu:
    """
    Class for working with Research Program.
    """
    def __init__(self):
        """
        Initialize menu and program.
        """
        answer = ["Y", "N"]
        self.fullmode = input("Do you want to have track and genre "
                              "search on? It will set year "
                              "range to maximum. [Y] or [N]")
        while self.fullmode.upper() not in answer:
            self.fullmode = input("Do you want to have track and genre "
                                  "search on? It will set year "
                                  "range to maximum. [Y] or [N]")
        start = int(input("Enter the first year of the period you want to research."))
        last = int(input("Enter the last year of the period you want to research."))
        self.adt = MusicADT(start, last, fullmode=self.fullmode)

        self.adt.fill_adt("docs/results.json")
        self.choices = {
            "1": self.year_top_func,
            "2": self.mult_year_top_func,
            "3": self.whole_year_func,
            "4": self.track_search_func,
            "5": self.genre_search_func,
            "6": self.adt.graph,
            "7": self.quit
        }

    @staticmethod
    def display_menu():
        """
        Print menu options.
        """
        print("""
Genre Research Menu
1. Receive Top genre of the year
2. Receive Top genre of the Time Period
3. Receive Full info about the year
4. Search Track (fullmode only)
5. Search Genre (fullmode only)
6. Open adt as the graph
7. Quit """)

    def year_top_func(self):
        """
        Launch ADT method.
        :return: None
        """
        y = int(input("Enter the year from the period you are discovering."))
        self.adt.years_top_genre(y)

    def mult_year_top_func(self):
        """
        Launch ADT method.
        :return: None
        """
        first_y = int(input("Enter the year from the period you are discovering."))
        last_y = int(input("Enter the year from the period you "
                           "are discovering.(larger than prevous)"))
        self.adt.multiple_year_top(first_y, last_y)

    def whole_year_func(self):
        """
        Launch ADT method.
        :return: None
        """
        y = int(input("Enter the year from the period you are discovering."))
        self.adt.get_whole_year(y)

    def track_search_func(self):
        """
        Launch ADT method.
        :return: None
        """
        if self.fullmode:
            track = input("Enter track name.")
            self.adt.track_search(track)
        else:
            print("Sorry, no full mode on.")

    def genre_search_func(self):
        """
        Launch ADT method.
        :return: None
        """
        if self.fullmode:
            genre = input("Enter genre you want.")
            self.adt.genre_search(genre)
        else:
            print("Sorry, no full mode on.")

    def run(self):
        """
        Run the program.
        """
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice.".format(choice))

    @staticmethod
    def quit():
        """
        Terminate the program.
        """
        print("Thank you for using this program.")
        sleep(3)
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
