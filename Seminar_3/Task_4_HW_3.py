#  4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.

import random
from random import uniform

n = int(input("Write size: "))

my_list = [round(random.uniform(1, 10), 2) for i in range(n)]

print(my_list)

def frac(frac_list: list):
    frac_list = []
    for i in range(n):
        frac_list.append(round(my_list[i] - int(my_list[i]), 2))
    return frac_list

def dif(new_list: list):
    min_number = min(new_list)
    max_number = max(new_list)
    result = round(max_number - min_number, 2)
    return result


frac_list = frac(my_list)
print(frac_list)
print(dif(frac_list))
