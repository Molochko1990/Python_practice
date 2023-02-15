def summ(a, b):
    if b == 0:
        return a
    return summ(a+1,b-1)
a = int(input('Введите число а = '))
b = int(input('Введите число b = '))
print(summ(a, b))