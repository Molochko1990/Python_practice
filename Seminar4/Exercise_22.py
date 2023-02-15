n, m = input('Введите кол-во элементов в первом и втором множестве: ').split()
lst1 = []
lst2 = []
# Создание двух списков
for x in range(1, int(n)+1):
    x = input(f'Введите значение {x} элемента для первого множества: ')
    lst1.append(x)

for x in range(1, int(m)+1):
    x = input(f'Введите значение {x} элемента для второго множества: ')
    lst2.append(x)


# lst1 = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
# lst2 = [3, 6, 9, 12, 15, 18]


lst3 = [v for v in lst1 + lst2 if v in lst1 and v in lst2]
final_lst = []
for i in lst3:
    if lst3.count(i) > 1 and i not in final_lst:
        final_lst.append(i)

final_lst.sort()
print(final_lst)
