# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

n = int(input('Введите число от 1 до 7: '))

if (n == 6 or n == 7) == True:
    print('Выходной')

elif (n > 7 or n < 0):
    print('Некорректное значение')

else:
    print ('Будний день')