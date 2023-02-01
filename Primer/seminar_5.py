# 1. Создайте список из N натуральных чисел(0 до N),
#    упорядоченных по возрастанию. Среди чисел не хватает
#    одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
#    Найдите это число.

from random import choice


def make_list():
    num = int(input("Input your number, please: "))
    ls = [i for i in range(num + 1)]
    ls.remove(choice(ls))
    print(ls)
    return ls

def find_num(lst):
    for i in range(1, len(lst)):
        if lst[i] - 1 != lst[i - 1]:
            return lst[i] - 1
    return -1


print(find_num(make_list()))


# 2. Создайте список, в который попадают числа,
#    описывающие возрастающую последовательность.
#    Порядок элементов менять нельзя.


from random import choices

def FillList():
    n = int(input('Введите длину списка '))
    my_list = choices(range(n * 2), k=n)
    return my_list

def SortList(s_list):
    new_list = []
    for i in range(len(s_list)):
        temp = s_list[i]
        d_list = [temp]
        for j in range(i + 1, len(s_list)):
            if s_list[j] > temp:
                temp = s_list[j]
                d_list.append(temp)
        if len(d_list) > 1:
            new_list.append(d_list)
    return new_list

a = FillList()
print(a)
print()
print(SortList(a))
