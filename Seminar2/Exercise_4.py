'''№1 Задайте список из N элементов,
заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.'''

import random
from random import shuffle

def gen_list(i):
    for i in range(i):
        lst.append(random.randint(-i, i))


def prod_of_num():
    print('Сгенерированный список: ', lst, '\n=======================')
    result = 1
    for line in (open('file.txt')).readlines():
        result = lst[int(line)] * result
        print(result)

    print('Произведение элементов на указанных позициях равно = ', result)

i = int(input('Введите количество чисел: '))
lst = []
gen_list(i)
prod_of_num()


'''№2 Реализуйте алгоритм перемешивания списка.'''

shuffle(lst)
prod_of_num()