import json
def get_data_week(count_days:int, path:str):
    'Allow get sum few data of 7 or less count of files. Less 7 just when nessesary count files is not existing.'
    # Open file with programm data for check count existing files.
    with open(f'{path}/programm_data.json', encoding='utf-8') as file:
        programm_dict = json.load(file)
        if(count_days > len(programm_dict["Existing_files"])):
            print("given quantity files out of range existing files. But will returned value of max existing days. ")
        # Probably so important variable that next code will contain amount time of learning or programming.
        amount_learning_time = 0
        mental_work = 0
        # Open all existing files.
        for file_index in range(len(programm_dict["Existing_files"]) - 1, 0, -1):
            if(file_index + 1 == len(programm_dict["Existing_files"]) - count_days):
                break
            else:
                with open(f"{path}/{file_index}.json", encoding='utf-8') as main_file:
                    main_dicionary = json.load(main_file)
                    # get periods struct of json file. 
                    for period_index in range(len(main_dicionary)):
                        # Get all nessesary data of all periods in whole file, also perform cheking of existing reqirment key.  
                        try:
                            amount_learning_time += int(main_dicionary[period_index]["учебное_время"])
                            mental_work += int(main_dicionary[period_index]["когнитивная_нагрузка"])
                        except:
                            continue
        return amount_learning_time, mental_work