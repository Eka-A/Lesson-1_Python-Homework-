# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math

x1 = int(input('Введите x1:'))
y1 = int(input('Введите y1:'))
x2 = int(input('Введите x2:'))
y2 = int(input('Введите y2:'))

result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(round(result,2))