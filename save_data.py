import json
def save(path:str, list:list):
    with open(path, mode='w') as file:
        json.dump(list, file, indent=2, ensure_ascii=False)