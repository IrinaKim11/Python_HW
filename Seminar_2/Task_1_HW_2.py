# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.

number = float(input("Введите число: "))
sum_numb = 0

power = len(str(number))
number *= 10 ** power

while number:
    sum_numb += number % 10
    number //= 10

print(int(sum_numb))

