from random import randint
rang = 20
lst = [randint(-10,10) for i in range(rang)]
final_lst = []
print('Ввод', lst)
a, b = input('Введите диапазон: ').split()
for i in range(rang):
    if int(a) <= i <= int(b):
        final_lst.append(i)
print(final_lst)
