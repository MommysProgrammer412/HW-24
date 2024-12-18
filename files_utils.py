import json
import csv
# import yaml

JSON_DICT = {
    'intricately': True,
    'have_to_do': True,
}

def write_json(data, file_path: str, encoding: str = "utf-8") -> None:
    '''функция записывающая словарь python в JSON-файл'''
    with open('test.json', 'w', encoding='utf-8') as file:
        json.dump(JSON_DICT, file, indent=4, ensure_ascii=False)
    print(JSON_DICT, 'test.json')

# write_json(JSON_DICT, 'test.json')# вызываем функцию для записи

def read_json(file_path: str, encoding: str = "utf-8") -> dict:
    '''функция читающая JSON-файл и возвращающая словарь python'''
    with open('test.json', 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data

# print(read_json('test.json'))# принтуем результат функции чтения

NEW_JSON_DICT = [{
'append_dict': True,
},{
'i_did_it': True,
}]

def append_json(data: list[dict], file_path: str, encoding: str = "utf-8") -> None:
    '''функция добавляющая новые данные к JSON-файлу'''
    existing_data = [read_json('test.json')]
    existing_data.extend(NEW_JSON_DICT)
    with open('test.json', 'w', encoding="utf-8") as file:
        json.dump(existing_data, file, indent=4, ensure_ascii=False)

# append_json(NEW_JSON_DICT, 'test.json')# Вызываем функцию для добавления NEW_JSON_DICT в test.json
# print(read_json('test.json'))# Проверяем результат, читая обновленный файл

#--------------------------------------------------------------------------------

CSV_DICT = [
["Шматрица", "Братсво Кольца", "Буря в стакане"],
["Bud", "Kozel", "Hoegaarden"],
]

def write_csv(data, file_path, delimiter=';', encoding: str ='utf-8-sig') -> None:
    '''функция записывающая список списков в CSV-файл'''
    with open('test.csv', 'w', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';', lineterminator='\n')
        writer.writerows(CSV_DICT)
    print(CSV_DICT)

# write_csv(CSV_DICT, 'test.csv')# вызываем функцию для записи

def read_csv(file_path, delimiter=';', encoding: str ='utf-8-sig') -> list[list[str]]:
    '''функция читающая CSV-файл и возвращающая список списков'''
    with open('test.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file, delimiter=';')
        data = list(reader)
    return data

# print(read_csv('test.csv'))# принтуем результат функции чтения

NEW_CSV_DICT = [
['apple', 'banana', 'orange'],
['name', 'surname', 'age'],
]

def append_csv(data, file_path, delimiter=';', encoding: str ='utf-8-sig') -> None:
    '''функция добавляющая новые данные к CSV-файлу'''
    with open('test.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';', lineterminator='\n')
        writer.writerows(NEW_CSV_DICT)

# append_csv(NEW_CSV_DICT, 'test.csv')# Вызываем функцию для добавления NEW_CSV_DICT в test.csv
# print(read_csv('test.csv'))# Проверяем результат, читая обновленный файл