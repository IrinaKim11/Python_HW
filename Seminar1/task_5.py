# Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
import math

x = int(input("Введите x: "))
y = int(input("Введите y: "))
x1 = int(input("Введите x: "))
y1 = int(input("Введите y: "))

dis = math.sqrt((x1-x)**2 + (y1-y)**2)
print(f"{dis: .3f}")


