inp = input('Введи кричалку: ')
phrase = inp.split(' ')
letters = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
final_lst = []
for word in phrase:
    count = 0
    for letter in word:
        if letter in letters:
            count += 1
    final_lst.append(count)
if len(set(final_lst)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')
