# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.

numbers = str(input('Put numbers: '))
num_list = list(numbers)
new_list = []

for i in num_list:
    if num_list.count(i) < 2:
        new_list.append(i)
print(*new_list, sep=" ")





