# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# Без использования встроенной функции преобразования, без строк.

def convert(num: int):
    result = []
    while num > 0:
        result.append(num % 2)
        num //= 2
    return result

def rev(my_list: list):
    my_list.reverse()
    return my_list

my_list = convert(int(input("Put your number: ")))
print(*rev(my_list), sep="")