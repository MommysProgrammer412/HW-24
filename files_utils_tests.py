import yaml
from files_utils import (
    write_json, read_json, append_json,
    write_csv, read_csv, append_csv,
    write_txt, read_txt, append_txt,
    read_yaml, JSON_DICT, NEW_JSON_DICT,
    CSV_DICT, NEW_CSV_DICT, TXT_STR, 
    NEW_TXT_STR, YAML_DICT
)

# Тестирование JSON функций
write_json(JSON_DICT, 'test.json')
print(read_json('test.json'))
append_json(NEW_JSON_DICT, 'test.json')
print(read_json('test.json'))

# Тестирование CSV функций
write_csv(CSV_DICT, 'test.csv')
print(read_csv('test.csv'))
append_csv(NEW_CSV_DICT, 'test.csv')
print(read_csv('test.csv'))

# Тестирование TXT функций
write_txt(TXT_STR, 'test.txt')
print(read_txt('test.txt'))
append_txt(NEW_TXT_STR, 'test.txt')
print(read_txt('test.txt'))

# Тестирование YAML функции
print(read_yaml('test.yaml'))