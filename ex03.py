# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите X:'))
y = int(input('Введите Y:'))

if ((x != 0 and x>0) and (y != 0 and y>0)):
    print('Координатная плоскость 1')

elif ((x != 0 and x<0) and (y != 0 and y>0)):
    print('Координатная плоскость 2')

elif ((x != 0 and x<0) and (y != 0 and y<0)):
    print('Координатная плоскость 3')

elif ((x != 0 and x>0) and (y != 0 and y<0)):
    print('Координатная плоскость 4')
