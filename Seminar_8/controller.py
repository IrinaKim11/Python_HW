from add_data import *
from delete_data import*
from read_data import*
from find_data import *
from logg import logging
def greeting():
    print("Здравствуйте!")

def start():
    print("Что желаем сделать:\n\
    1 - получить всю информацию;\n\
    2 - добавить сотрудника;\n\
    3 - поиск сотрудника;\n\
    4 - удалить данные;\n\
    5 - выход")
    ch = input("Введите цифру: ")
    while True:
        if ch == '1':
            return export_data_screen()
        elif ch == '2':
            add_data()
        elif ch == '3':
            key = input('Введите имя сотрудника: ')
            return find_data(key)
        elif ch == '4':
            key = input('Введите имя: ')
            return delete_data(key)
        elif ch == '5':
            logging.info(f"Finish")
            print("Сеанс окончен, до свидания!")
            break
        else:
            logging.info(f"Something strange")
            print("Введите корректную цифру!")
            start()