'''Напишите программу,
которая принимает на вход вещественное число
и показывает сумму его цифр.'''

number = float(input('Введите число: '))
number_str = (str(number)).replace('.', '')
result = 0
for i in number_str:
    result += int(i)
print(f'Сумма всех чисел {number} = {result}')

