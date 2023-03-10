import datetime
import os
def reckon_file(path:str):
    'Return txt file content, converted to list.'
    # Important list contain converted to finaly list.
    main_list = []
    list_rows = []
    with open(path, encoding='utf-8') as file:
        list_rows = file.read().splitlines()
        for index in range(len(list_rows)):
            if(index == 0):
                list_rows[index] = list_rows[index][-1]
            # Check periods. 
            if(list_rows[index].isdigit()):
                main_list.append({})
            # Check childrens of periods. 
            elif(list_rows[index].find(":")):
                index_word = list_rows[index].strip().find(":")
                # Array may be in the value of children. 
                try:
                    if((list_rows[index].strip())[index_word + 1:].strip()[0] == "["):
                        list_item_list = ((list_rows[index].strip())[index_word + 1:].strip().lstrip("[").strip("]")).split()
                        main_list[len(main_list) - 1][(list_rows[index].strip())[:index_word]] = list_item_list
                    else:
                        main_list[len(main_list) - 1][(list_rows[index].strip())[:index_word]] = ((list_rows[index].strip())[index_word + 1:].strip())
                except IndexError:
                    pass
    return main_list
def update_data(programm_data:str, path:str):
    'Check update files, if datatime of last edit file is not equals datatime in programm_data.json -> file was changed. Return list of updated objects of updated files.'
    update_lists = []
    for i in range(len(programm_data["Existing_files"]) - 1):
        time_sec = os.path.getmtime(f"{path}/{i + 1}.txt")
        time_in_data_time = str(datetime.datetime.fromtimestamp(time_sec))
        if(programm_data['Existing_files_time'][f'{i + 1}.txt'] == time_in_data_time):
            continue
        else:
            update_list = reckon_file(f"{path}/{i + 1}.txt")
            update_lists.append({'object_list': update_list, 'path_to_save': f"{path}/{i + 1}.json"})
            programm_data['Existing_files_time'][f'{i + 1}.txt'] = str(datetime.datetime.fromtimestamp(time_sec))
    return update_lists
def create_file_of_new_day(programm_data:str, path:str):
    '''If txt file is existing, according may will create json file. This method literally do it! Return edited programm_data, 
    which contain few metadate of file, list of new file, and bool variable IsExisiting. So if file haven't edited, why save it?!'''
    IsExisiting = True
    new_list = []
    main_list = []
    new_file = max(programm_data["Existing_files"]) + 1
    try:
        # Geting converted file to main_list.  
        time_sec = os.path.getctime(f"{path}/{new_file}.txt")
        main_list = reckon_file(f"{path}/{new_file}.txt")
        programm_data['Existing_files_time'][f'{new_file}.txt'] = str(datetime.datetime.fromtimestamp(time_sec))
    except:
        IsExisiting = False
    # Embed value of count new file to Existing_files
    if(not(programm_data["Existing_files"][len(programm_data["Existing_files"]) - 1] == new_file) and IsExisiting == True):
        new_list.append(new_file)
        programm_data["Existing_files"] += new_list
    return programm_data, main_list, IsExisiting