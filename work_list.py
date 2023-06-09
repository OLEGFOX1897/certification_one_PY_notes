import save_load_csv
from datetime import datetime


def creat_note(list, title, body):
    note_list = []
    new_id = int(list[len(list)-1][0])+1
    time = datetime.now().strftime('%H:%M')
    date = datetime.now().strftime('%Y-%m-%d')
    note_list = [new_id, date, time, title, body]
    list.append(note_list)
    return list


def edit_note(id, list, title, body):
    time = datetime.now().strftime('%H:%M')
    date = datetime.now().strftime('%Y-%m-%d')
    for i in range(0, len(list), 1):
        if list[i][0] == str(id):
            list[i][1] = date
            list[i][2] = time
            list[i][3] = title
            list[i][4] = body
    return list


def del_note(id, list):
    for i in range(0, len(list), 1):
        if list[i][0] == str(id):
            i_del = i
            list.pop(i_del)
            break
    return list


def sort_date(list):  # no realese
    list_date=[]
    for i in range(1,len(list),1):
        list_date.append(list[i][1])
    list_date_sort=sorted(list_date)
    new_list=[]
    for i in range(0,len(list_date_sort),1):
        for j in range(0,len(list),1):
            if list_date_sort[i]==list[j][1]:
                new_list.append(list[j])
    return new_list


def find_note(id, list):
    list_out = []
    for i in range(0, len(list), 1):
        if str(id) == str(list[i][0]):
            list_out.append(list[i][1])
            list_out.append(list[i][2])
            list_out.append(list[i][3])
            list_out.append(list[i][4])
            break
    return list_out
