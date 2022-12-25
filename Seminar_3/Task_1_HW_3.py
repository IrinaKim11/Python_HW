# 1. Задайте список, состоящий из произвольных чисел, количество задаёт
# пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных
# позициях(не индексах).

import random

from random import randrange

n = 5
a = [randrange(1, 10) for i in range(n)]
print(a)

list_length = len(a)
sum_num = 0
count = 0
while count < list_length:
    sum_num += a[count]
    count = count + 2

print(sum_num)