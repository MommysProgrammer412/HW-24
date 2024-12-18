import json

JSON_DICT = {
    'intricately': True,
    'have_to_do': True,
}

def write_json(data, file_path: str, encoding: str = "utf-8") -> None:
    '''функция записывающая словарь python в JSON-файл'''
    with open('test.json', 'w', encoding='utf-8') as file:
        json.dump(JSON_DICT, file, indent=4, ensure_ascii=False)

write_json(JSON_DICT, 'test.json')# вызываем функцию для записи и проверяем результат в файле test.json

def read_json(file_path: str, encoding: str = "utf-8") -> dict:
    '''функция читающая JSON-файл и возвращающая словарь python'''
    with open('test.json', 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data

print(read_json('test.json'))# принтуем результат функции чтения

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

append_json(NEW_JSON_DICT, 'test.json')# Вызываем функцию для добавления NEW_JSON_DICT в test.json
print(read_json('test.json'))# Проверяем результат, читая обновленный файл