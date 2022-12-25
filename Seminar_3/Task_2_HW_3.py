# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

my_list = [5, 2, 3, 4, 5, 6, 7, 8, 9]

def numbers(my_list):
    list_length = len(my_list)
    res_list = []

    for i in range(list_length // 2):
        res_list.append(my_list[i] * my_list[len(my_list) - i - 1])
    if list_length % 2:
        res_list.append(my_list[list_length // 2])
    return res_list

print(numbers(my_list))