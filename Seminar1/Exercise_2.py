'''
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''
x = int(input('Введите X: '))
y = int(input('Введите Y: '))
z = int(input('Введите Z: '))

result1 = not(x or y or z)
result2 = not x and not y and not z
if result1 == result1:
    print(True)
else:
    print(False)
