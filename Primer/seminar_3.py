# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.


# from random import sample
#
#
# def num_find(len_list, number):
#     new_list = sample(range(1, len_list * 2), k=len_list)
#     print(new_list)
#     if number in new_list:
#         return 'Yes'
#     return 'No'
#
#
# print(num_find(int(input('Введите длину списка -')), int(input('Введите число -'))))


# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
#    Напишите программу, которая определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.

def spisok(count, word='abc'):
    my_list = []
    for i in range(count):
        temp = sample(word, k=3)
        my_list.append("".join(temp))
    return my_list


def index_find(word_2, list_2):
    if word_2 in list_2 and list_2.count(word_2) > 1:
        index_1 = list_2.index(word_2)
        print(list_2.index(word_2, index_1+1))
    else:
        print(-1)


list_1 = spisok(int(input()))
print(list_1)
index_find(input(), list_1)
