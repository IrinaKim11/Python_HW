# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите
# на экран их сумму.

number = int(input("Введите число: "))
sum_num = 0
list_num = []

for n in range(1, number + 1):
    result = round((1 + 1 / n) ** n, 3)
    list_num.append(result)
    sum_num += result

print(list_num)
print(sum_num)