from logg import logging
def add_data():
    logging.info(f"Add emloye")


    name = input('Name: ')

    department = input('Department: ')
    birthday_month = input('Birthday month: ')

    with open('office.csv', mode="a", encoding='utf-8') as data:
        employee = f'{name},{department},{birthday_month}\n'
        data.write(employee)