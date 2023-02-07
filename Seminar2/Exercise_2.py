'''Напишите программу,
которая принимает на вход число N
и выдает набор произведений чисел от 1 до N.'''

number = int(input('Введите число: '))
i = 1
lst = []
while number >= i:
    my_sum = 1
    j = 0
    while i > j:
        j += 1
        my_sum *= j

    lst.append(my_sum)
    i += 1
print(lst)