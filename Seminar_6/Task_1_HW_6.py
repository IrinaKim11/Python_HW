# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.


import random

def rand_lst(num = int(input('Enter number: '))):
    return random.sample(range(num+2), num)


my_lst = rand_lst()
print(my_lst)

def sort_lst(lst):
    return [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1]]

print(sort_lst(my_lst))

