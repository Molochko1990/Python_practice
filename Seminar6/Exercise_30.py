f_el = int(input('Введите первое число: '))
resid = int(input('Введите разность: '))
amount = int(input('Введите количество элементов: '))

lst = [f_el]
for i in range(0, amount-1):
    f_el += resid
    lst.append(f_el)
print('Вывод:', lst)
