'''Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai.
Последняя строка содержит число X'''

import random

n = int(input('Введите количество элементов в массиве: '))
x = int(input('Введите число x: '))
lst = [random.randint(i, n) for i in range(1, n + 1)]
print('Сгенерированный список: ', lst)
cnt = lst.count(x)
print(cnt)