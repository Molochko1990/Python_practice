'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai.
Последняя строка содержит число X'''

import random

n = int(input('Введите количество элементов в массиве: '))
x = int(input('Введите число x: '))
lst = random.sample(range(20), n)
print('Сгенерированный список: ', lst)

temp = 0
num = lst[temp]

for i in range(n):
    if abs(x - lst[temp]) < abs(x - num):
        num = lst[temp]
        temp +=1
    else:
        temp +=1
print(num)
