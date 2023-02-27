import Functions

def menu():
    inp = int(input('Нажми "1", чтобы вывести справочник\n'
          'Нажми "2", чтобы записать новый контакт\n'
          'Нажми "3", чтобы найти контакт\n'
          'Нажми "4", чтобы изменить данные контакта\n'
          'Нажми "5", чтобы удалить данные контакта\n'
          'Нажми "0", чтобы завершить работу\n'
          '>>> '))

    if inp == 0:
        Functions.end_pr()
    elif inp == 1:
        Functions.output_direct()
        menu()
    elif inp == 2:
        Functions.add_an_entry(Functions.get_data())
    elif inp == 3:
        print('/n'.join(Functions.find_entry(input('Введите ФИО или телефон: '))))
    elif inp == 4:
        Functions.output_direct()
        Functions.change_dat()
    elif inp == 5:
        Functions.output_direct()
        Functions.delete_dat()
    else:
        print('Неверный ввод')
        return menu()

if __name__ == '__main__':
    menu()
