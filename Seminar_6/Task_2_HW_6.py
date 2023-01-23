# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

def sort_lst(num = int(input("Enter number: "))):
    my_lst = [i for i in range(20, num + 1) if not i % 20 or not i % 21]
    return my_lst

print(sort_lst())