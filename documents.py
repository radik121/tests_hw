documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


# Функция для вывода имени человека по номеру документа
def user_name(data):
    while True:
        a = input('Введите номер документа: ')
        for k in data:
            if a == k["number"]:
                return k["name"]


# Функция для вывода полки по номеру документа
def shelf_name(data):
    while True:
        a = input('Введите номер документа: ')
        for key, volue in data.items():
            if a in volue:
                return f'Номер полки: {key}'
            # return(f'Документа с номером {a} нет')


# Функция для вывода всего списка документов
def list_all(data):
    lst = [f'{i["type"]}, {i["number"]}, {i["name"]}' for i in data]
    return '\n'.join(lst)


# Функция для добавления нового документа, имени в каталог и в расположение полок
def add_all(data, shelf):
    num_doc = input('Введите номер документа: ')
    type_doc = input('Введите тип документа: ')
    name = input('Введите имя и фамилию: ')
    new_dict = {'type': type_doc, 'number': num_doc, 'name': name}
    data.append(new_dict)
    while True:
        shelf_add = input('Введите номер полки: ')
        if shelf_add in shelf.keys():
            shelf[shelf_add].append(num_doc)
        return f'Вы добавили {new_dict.values()} на полку {shelf_add}'


# Функция для удаления данных по номеру документа из каталога и полок
def delete(data, shelf):
    while True:
        del_doc = input('Введите номер документа: ')
        # for k in data:
        #   if k["number"] == del_doc:
        #     del k["number"], k["type"], k["name"]
        for i in range(len(data)):
            if data[i]['number'] == del_doc:
                del data[i]

                for k, v in shelf.items():
                    if del_doc in v:
                        v.remove(del_doc)
                    return f'Вы удалили документ {del_doc}'


# Функция для перемещения документа по полкам
def doc_by_loc(shelf):
    doc = input('Введите номер документа: ')
    loc = input('Введите номер полки: ')
    for k, v in shelf.items():
        if doc in v and loc in shelf.keys():
            v.remove(doc)
            shelf[loc].append(doc)
            return shelf
        else:
            return 'Вы ввели не верные данные'


def main(data, direct):
    while True:
        print('-' * 30)
        user_input = input(
            '''Введите команду:\np – имя человека по номеру документа;\ns – номер полки по номеру док-та;\nl – список 
            всех документов;\na – новый документ в каталог и в перечень полок;\nd – удаление из каталога и переченя 
            полок;\nm – перемещение доку-та с текущей полки на целевую;\nq - выход из программы;\n''')
        print('-' * 30)
        if user_input == 'q':
            return 'До свидания!'
        elif user_input == 'p':
            print(user_name(data))
        elif user_input == 's':
            print(shelf_name(direct))
        elif user_input == 'l':
            print(list_all(data))
        elif user_input == 'a':
            print(add_all(data, direct))
        elif user_input == 'd':
            print(delete(data, direct))
        elif user_input == 'm':
            print(doc_by_loc(direct))


if __name__ == '__main__':
    print(main(documents, directories))