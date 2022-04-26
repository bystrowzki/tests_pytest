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


def name_by_number(list):
    doc_number = input("Введите номер документа: ")
    for docs in list:
        for key in docs:
            if docs[key] == doc_number:
                print("Имя: " + docs["name"])
                return docs["name"]


def shelf_by_number(dict):
    number = input("Введите номер документа: ")
    x = 0
    for shelf in dict:
        for doc_number in dict[shelf]:
            if doc_number == number:
                x = shelf
            elif doc_number != number:
                continue
    if x == 0:
        print("Такого номера не существует. Попробуйте снова.")
        return ValueError
    else:
        print("Номер полки: " + x)
        return x


def list_of_docs(list):
    data = []
    for docs in list:
        for key in docs.keys():
            x = docs[key]
            data.append(x)
            print(docs[key], end=" ")
        print()
    return data


def new_document(list, dict):
    doc = {"type": None, "number": None, "name": None}
    number = input("Введите номер документа: ")
    doc_type = input("Введите тип документа: ")
    name = input("Введите имя владельца: ")
    shelf = input("Введите номер полки для документа: ")
    doc["number"] = number
    doc["type"] = doc_type
    doc["name"] = name
    try:
        dict[shelf].append(number)
        list.append(doc)
        return len(list)
    except KeyError:
        try:
            shelf2 = input("Такой полки не существует, попробуйте снова.\nВведите номер полки для документа: ")
            dict[shelf2].append(number)
            list.append(doc)
            return len(list)
        except KeyError:
            print("Такой полки не существует.")
            return KeyError


def delete_document(list, dict):
    number = input("Введите номер документа: ")
    x = 0
    for docs in list:
        for key in docs:
            if docs[key] == number:
                x = docs
    try:
        list.remove(x)
        for shelf in dict:
            for doc_number in dict[shelf]:
                if doc_number == number:
                    dict[shelf].remove(doc_number)
                    return len(list)
    except ValueError:
        print("Такого номера не существует. Попробуйте снова.")
        return len(list)


def move_document(dict):
    number = input("Введите номер документа: ")
    shelf = input("Введите номер полки документа: ")
    new_shelf = input("Введите номер полки для документа: ")
    try:
        dict[shelf].remove(number)
        dict[new_shelf].append(number)
        print(dict)
        return dict
    except ValueError:
        print("Вы ввели неверный номер документа или полки, попробуйте снова.")
        return dict


def new_shelf(dict):
    shelf = input("Введите номер новой полки: ")
    if shelf in dict:
        print("Такая полка уже существует. Попробуйте снова.")
        return KeyError
    else:
        dict[shelf] = []
        return len(dict)


def main(list, dict):
    while True:
        print("[p] - Имя по номеру документа")
        print("[s] - Номер полки по номеру документа")
        print("[l] - Список всех документов")
        print("[a] - Добавить новый документ")
        print("[d] - Удалить документ")
        print("[m] - Переместить документ")
        print("[as] - Добавить новую полку")
        print("[0] - EXIT")

        choice = input("Сделайте выбор: ")
        if choice == "p":
            name_by_number(list)
        elif choice == "s":
            shelf_by_number(dict)
        elif choice == "l":
            list_of_docs(list)
        elif choice == "a":
            new_document(list, dict)
        elif choice == "d":
            delete_document(list, dict)
        elif choice == "m":
            move_document(dict)
        elif choice == "as":
            new_shelf(dict)
        elif choice == 0:
            break

if __name__ == '__main__':
    main(documents, directories)