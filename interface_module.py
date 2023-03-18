import work_list
import save_load_csv
import clean_input_error


def main_menu(list):
    print('-----------------------------------------------------------------------------------------')
    print(f'ГЛАВНОЕ МЕНЮ', "1. Создать заметку", '2. Просмотреть список всех заметок',
          '3. Завершить работу', "Введите вариант действия:", sep='\n')
    action = clean_input_error.inp_num(1)
    if action == 1:
        creat_note(list)
    elif action == 2:
        list_notes(list)
    elif action == 3:
        finish_work(list)
    else:
        print('Неправильный ввод!')
        main_menu(list)


def creat_note(list):
    print('-----------------------------------------------------------------------------------------')
    print('СОЗДАНИЕ ЗАМЕТКИ')
    title_new = input('Введите заголовок заметки:')
    body_new = input('Введите тело заметки:')
    print('-----------------------------------------------------------------------------------------')
    print(f"1. Сохранить этот вариант", '2. Редактировать',
          '3. Выйти без сохранения', "Введите вариант действия:", sep='\n')
    action = clean_input_error.inp_num(1)
    if action == 1:
        print('-----------------------------------------------------------------------------------------')
        print('ВАША ЗАМЕТКА СОХРАНЕНА')
        new_List = work_list.creat_note(list, title_new, body_new)
        main_menu(new_List)
    elif action == 2:
        creat_note(list)
    elif action == 3:
        main_menu(list)


def list_notes(list):
    print('-----------------------------------------------------------------------------------------')
    print('СПИСОК ЗАМЕТОК')
    print_notes(list)
    print('-----------------------------------------------------------------------------------------')
    print(f"1. Для просмотра/редактирования/удаления заметки", '2. Для сортировки заметок по дате', '3. Вернуться в главное меню',
          "Введите вариант действия:", sep='\n')
    action = clean_input_error.inp_num(1)
    if action == 1:
        play_note(list)
    elif action == 2:
        sorted_data(list)
    elif action == 3:
        main_menu(list)
    else:
        print('Неправильный ввод варианта!!!')
        list_notes(list)


def play_note(list):
    print('-----------------------------------------------------------------------------------------')
    print('Введите номер id заметки для ее просмотра/редактирования/удаления или 0, чтобы вернуться в основное меню:')
    action_one = clean_input_error.inp_num(1)
    finish_note = int(list[len(list)-1][0])
    if action_one == 0:
        main_menu(list)
    elif action_one > 0 and action_one <= finish_note:
        list_note = work_list.find_note(action_one, list)
        print("Заголовок заметки: "+list_note[2])
        print("Текст заметки: "+list_note[3])
        print("Создана: "+list_note[0])
        print("В: "+list_note[1])
        print('-----------------------------------------------------------------------------------------')
        print(f"1. Для редактирования", '2. Для удаления',
              '3. Вернуться к списку заметок', "Введите вариант действия:", sep='\n')
        action_two = clean_input_error.inp_num(1)
        if action_two == 3:
            list_notes(list)
        elif action_two == 1:
            edit_note(action_one, list)
        elif action_two == 2:
            del_note(action_one, list)
        else:
            print(
                '-----------------------------------------------------------------------------------------')
            print('Неверный ввод варианта действия с заметкой. Повторите ввод!')
            play_note(list)
    else:
        print('-----------------------------------------------------------------------------------------')
        print('Такой заметки нет. Повторите ввод')
        play_note(list)

def sorted_data(list):
    new_list=work_list.sort_date(list)
    print_notes(new_list)
    list_notes(list)


def edit_note(id, list):
    print('-----------------------------------------------------------------------------------------')
    print("ОКНО РЕДАКТИРОВАНИЯ ЗАМЕТКИ id={}".format(id))
    title = input("Введите новое название заметки: ")
    body = input("Введите текст заметки:")
    new_list = work_list.edit_note(id, list, title, body)
    print('-----------------------------------------------------------------------------------------')
    print("Изменения для заметки c id={} сохранены.".format(id))
    list_notes(new_list)


def del_note(id, list):
    new_list = work_list.del_note(id, list)
    print('-----------------------------------------------------------------------------------------')
    print("Заметка c id={} удалена!".format(id))
    list_notes(new_list)


def finish_work(list):
    print('Работа завершена. Досвидание')
    save_load_csv.save_note(list)


def print_notes(list):
   print('id |   Дата создания   | Время создания |  Название заметки ')
   for i in range(1, len(list), 1):
       print('{}         {}           {}         {}'.format(
           list[i][0], list[i][1], list[i][2], list[i][3]))
