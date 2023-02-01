from read_data import import_dictionary
import csv
from logg import logging
def delete_data(k):
    logging.info(f"Deleting employe {k}")

    array = import_dictionary()
    for i in array:
        for value in i.values():
            if value == k:
                array.remove(i)
    with open('office.csv', mode="w", encoding='utf-8', newline='') as data:
        fc = csv.DictWriter(data, fieldnames=array[0].keys())
        fc.writeheader()
        fc.writerows(array)