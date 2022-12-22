# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.

number = int(input("Введите число: "))
result = 1
num_list = []
for i in range(number):
    result *= i + 1
    num_list.append(result)
print(num_list)




