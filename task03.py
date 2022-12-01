# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

size = int(input('Введите размер списка: '))
value = int(input('Введите максимальное значение элемента списка: '))
number_of_decimals = int(input('Введите до какой цифры после запятой будет округление: '))
my_list = []
for i in range(size):
    my_list.append(round(value * random.random(), number_of_decimals))
print(my_list)
min = 1
max = 0
for i in range(size):
    if my_list[i] % 1 != 0:  # Проверка на целочисленное число
        if min > my_list[i] % 1:
            min = my_list[i] % 1
        if max < my_list[i] % 1:
            max = my_list[i] % 1
print(f'Максимальное значение {round(max, number_of_decimals)}, минимальное значение {round(min, number_of_decimals)} ')
print(f'Разница равна: {round(max - min, number_of_decimals)}')
