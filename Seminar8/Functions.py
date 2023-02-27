def output_direct():
    try:
        print_all()
    except FileNotFoundError:
        print('В справочнике еще никого нет, сперва добавьте хотя бы один контакт')
def get_data():
    last_name = input('Введите Фамилию: ').strip()
    first_name = input('Введите Имя: ').strip()
    middle_name = input('Введите Отчество или оставьте поле пустым: ').strip()
    phone_number = input('Введите номер телефона: ').strip()
    if middle_name == '':
        return (last_name, first_name, phone_number)
    else:
        return (last_name, first_name, middle_name, phone_number)

def print_all():
    pb = open('phonebook.txt', 'r', encoding='utf-8')
    print('Актуальный справочник:\n\n' + pb.read()+ '============================')
    pb.close()

def find_entry(word):
    pb = open('phonebook.txt', 'r', encoding='utf-8')
    list_of_found_entries = []
    for line in pb:
        if word in line.split():
            list_of_found_entries.append(line)
    pb.close()
    return list_of_found_entries

def add_an_entry(data):
    pb = open('phonebook.txt', 'a', encoding='utf-8')
    pb.write(' '.join(data)+'\n')
    pb.close()

def change_dat():
    inp = input('Напишите или скопируйте из списка '
                'и вставьте полное ФИО и номер человека, '
                'данные которого нужно изменить\n>>>')
    print("Введите новые данные...")
    with open ('phonebook.txt', 'r', encoding='utf-8') as pb:
        old_dat = pb.read()
    new_dat = old_dat.replace(inp, ' '.join(get_data()))
    with open('phonebook.txt', 'w', encoding='utf-8') as pb:
        pb.write(new_dat)

def delete_dat():
    inp = (input('Напишите или скопируйте из списка и '
                'вставьте полное ФИО и номер человека, '
                'данные которого нужно удалить\n>>>')).strip()
    with open('phonebook.txt', 'r', encoding='utf-8') as pb:
        old_dat = pb.read()
    new_dat = old_dat.replace(inp+'\n', '')
    with open('phonebook.txt', 'w', encoding='utf-8') as pb:
        pb.write(new_dat)
def end_pr():
    print('Работа закончена')