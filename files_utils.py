import json
import csv
import yaml

JSON_DICT = {
    'intricately': True,
    'have_to_do': True,
}

def write_json(data, file_path: str, encoding: str = "utf-8") -> None:
    '''функция записывающая словарь python в JSON-файл'''
    with open('test.json', 'w', encoding='utf-8') as file:
        json.dump(JSON_DICT, file, indent=4, ensure_ascii=False)

# write_json(JSON_DICT, 'test.json')# вызываем функцию для записи, результат увидим в следующей функции чтения

def read_json(file_path: str, encoding: str = "utf-8") -> dict:
    '''функция читающая JSON-файл и возвращающая словарь python'''
    with open('test.json', 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data

# print(read_json('test.json'))# принтуем результат функции чтения и записи

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

# write_csv(CSV_DICT, 'test.csv')# вызываем функцию для записи, результат увидим в следующей функции чтения

def read_csv(file_path, delimiter=';', encoding: str ='utf-8-sig') -> list[list[str]]:
    '''функция читающая CSV-файл и возвращающая список списков'''
    with open('test.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file, delimiter=';')
        data = list(reader)
    return data

# print(read_csv('test.csv'))# принтуем результат функции чтения и записи

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

#--------------------------------------------------------------------------------

TXT_STR = 'string for test.txt'

def write_txt(data, file_path, encoding: str = "utf-8") -> None:
    '''функция записывающая данные в текстовый файл'''
    with open('test.txt', 'w', encoding="utf-8") as file:
        file.write(str(TXT_STR) + '\n')

# write_txt(TXT_STR, 'test.txt')# вызываем функцию для записи, результат увидим в следующей функции чтения

def read_txt(file_path, encoding: str = "utf-8") -> str:
    '''функция читающая текстовый файл и возвращающая строку'''
    with open('test.txt', 'r', encoding="utf-8") as file:
        data = file.read()
    return data

# print(read_txt('test.txt'))# принтуем результат функции чтения и записи

NEW_TXT_STR = 'new string for test.txt'

def append_txt(data, file_path, encoding: str = "utf-8") -> None:
    '''функция добавляющая новую дстроку к текстовому файлу'''
    with open('test.txt', 'a', encoding="utf-8") as file:
        file.write(str(NEW_TXT_STR) + '\n')

# append_txt(NEW_TXT_STR, 'test.txt')# Вызываем функцию для добавления NEW_TXT_STR в test.txt
# print(read_txt('test.txt'))# Проверяем результат, читая обновленный файл

#--------------------------------------------------------------------------------

YAML_DICT = {
    'temp': 25,
    "feels_like": 23,
    'description': "light rain",
}

with open('test.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(YAML_DICT, file, allow_unicode=True)

def read_yaml(file_path: str, encoding: str = "utf-8") -> dict:
    '''функция читающая YAML-файл и возвращающая словарь python'''
    with open('test.yaml', 'r', encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return data

# print(read_yaml('test.yaml'))# принтуем результат функции чтения и записи
