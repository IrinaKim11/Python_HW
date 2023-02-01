from read_data import import_dictionary
from logg import logging
def find_data(k):
    logging.info(f"Find employe {k}")

    array = import_dictionary()
    for i in array:
        for value in i.values():
            if value == k:
                print(i)