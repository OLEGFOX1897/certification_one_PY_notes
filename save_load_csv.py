import csv


def save_note(list):
    with open('data.csv', 'w', encoding='utf-8') as file:
        for i in range(0, len(list), 1):
            file.write('{};{};{};{};{}\n'
                       .format(list[i][0], list[i][1], list[i][2], list[i][3], list[i][4]))


def load_notes():
    list_notes = []
    with open('data.csv', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=';')
        for row in file_reader:
            list_notes.append(row)
    return list_notes


listy = load_notes()
