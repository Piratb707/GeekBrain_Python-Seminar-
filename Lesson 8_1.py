# Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. Доделать задание вебинара и реализовать Update, Delete
# Информация о человеке: Фамилия, Имя, Телефон, Описание
#
# Корректность и уникальность данных не обязательны.
#
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
#
# 2) CRUD: Create, Read, Update, Delete
#
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
#
# 4) импорт данных из текстового файла формата csv
#
# Используйте функции для реализации значимых действий в программе


import csv

phonebook = {}


def create_record(last_name, first_name, phone_number, description):
    phonebook[last_name] = [first_name, phone_number, description]
    print(f"Запись {last_name} успешно добавлена в справочник.")


def read_record(last_name):
    if last_name in phonebook:
        print(f"Фамилия: {last_name}")
        print(f"Имя: {phonebook[last_name][0]}")
        print(f"Телефон: {phonebook[last_name][1]}")
        print(f"Описание: {phonebook[last_name][2]}")
    else:
        print(f"Запись с фамилией {last_name} не найдена в справочнике.")


def update_record(last_name, first_name=None, phone_number=None, description=None):
    if last_name in phonebook:
        if first_name:
            phonebook[last_name][0] = first_name
        if phone_number:
            phonebook[last_name][1] = phone_number
        if description:
            phonebook[last_name][2] = description
        print(f"Запись {last_name} успешно обновлена.")
    else:
        print(f"Запись с фамилией {last_name} не найдена в справочнике.")


def delete_record(last_name):
    if last_name in phonebook:
        del phonebook[last_name]
        print(f"Запись {last_name} успешно удалена из справочника.")
    else:
        print(f"Запись с фамилией {last_name} не найдена в справочнике.")


def export_to_csv(file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Фамилия", "Имя", "Телефон", "Описание"])
        for last_name, data in phonebook.items():
            row = [last_name] + data
            writer.writerow(row)
    print(f"Справочник успешно экспортирован в файл {file_name}.")


def import_from_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            last_name = row[0]
            data = row[1:]
            phonebook[last_name] = data
    print(f"Справочник успешно импортирован из файла {file_name}.")


# Пример использования
create_record("Иванов", "Иван", "1234567", "Старший менеджер")
create_record("Петров", "Петр", "7654321", "Младший менеджер")

export_to_csv("phonebook.csv")
import_from_csv("phonebook.csv")

read_record("Иванов")
update_record("Иванов", phone_number="9876543")
delete_record("Петров")

