import json
def save(path:str, iterable):
    with open(path, mode='w', encoding = 'utf-8') as file:
        json.dump(iterable, file, indent=2, ensure_ascii=False)