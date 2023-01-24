import json
def update_limits(programm_data, path) -> dict:
    'Return updated limits of files in programm_data wich is accepted in arguments'
    # Assign name for file of new day f'{i + 2}': int(next_limit)
    programm_data['limits_for_files'][f'{1}'] = programm_data['limit']
    for i in range(len(programm_data['Existing_files']) - 1):
        with open(f'{path}/{i + 1}.json', encoding='utf-8') as json_file:
            previous_object = json.load(json_file)
            work_perform = 0
            mental_work = 0
            for period in previous_object:
                try:
                    work_perform += int(period['учебное_время'])
                    mental_work += int(period['когнитивная_нагрузка'])
                except KeyError:
                    continue
            next_limit = int((programm_data['limits_for_files'][f'{i + 1}'] - (
                work_perform - programm_data['limits_for_files'][f'{i + 1}'])) - mental_work * 0.5)
            if (work_perform <= programm_data['limits_for_files'][f'{i + 1}'] and mental_work < programm_data['limit_mental_work']):
                next_limit = programm_data['limit']
            elif (next_limit < 0):
                next_limit = 0
            if (next_limit < 100):
                next_limit += 50
            amount = i + 2
            programm_data['limits_for_files'][f'{amount}'] = next_limit
    return programm_data


def add_act(activites_data:list, name:str, value:int, period:int):
    activites_data[int(period) - 1][name] = value
    return activites_data