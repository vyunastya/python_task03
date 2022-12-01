# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
decimal_number = int(input("Введите десятичное число: "))
binary_number_reverse = ''
binary_number =''
while decimal_number > 0:
    binary_number_reverse += str(decimal_number % 2)
    decimal_number //= 2
size = len(binary_number_reverse)
for i in range(size):
    binary_number += binary_number_reverse[size-i-1]
print(f'Двоичное: {binary_number}')