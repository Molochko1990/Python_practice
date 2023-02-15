def exp(a, b):
    if b < 1:
        return 1
    return a * exp(a, b-1)

a = int(input('Введите число а = '))
b = int(input('Введите число b = '))
print(exp(a, b))