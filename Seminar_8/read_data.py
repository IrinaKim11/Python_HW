import csv
from logg import logging
def import_dictionary():
    with open("office.csv", mode="r", encoding='utf-8') as f:
        dict_reader = csv.DictReader(f)
        list_of_dict = list(dict_reader)
    return list_of_dict

def export_data_screen():
    logging.info(f"Show all employes")

    with open("office.csv", mode="r", encoding='utf-8') as f:
    # Создаем объект DictReader, указываем символ-разделитель ","
        file_reader = csv.DictReader(f, delimiter = ",")
        for row in file_reader:
            print(f' {row["Name"]},{row["Department"]}, {row["Birthday month"]}', end='\n')