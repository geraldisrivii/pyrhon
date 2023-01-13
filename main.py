import open_data
import json
import statistic
import save_data
import work
# Get sorted and edit to json format (dict - python), list, which contain info from user file.]
with open('files/activites_data.json', encoding='utf-8') as file_activitys:
    activites_data = json.load(file_activitys)
    with open('files/programm_data.json', encoding='utf-8') as file_programm:
        # Deserelise json to dictionary programm_data
        programm_data = json.load(file_programm)
        # Check update files, if datatime of last edit file is not equals datatime in programm_data.json -> file was changed.
        list_of_updated_objects = open_data.update_data(programm_data)
        # Save updated objects to json files. Literally for this procedure was changed all previous actions(;
        for updated_object in list_of_updated_objects:
            save_data.save(updated_object['path_to_save'],
                        updated_object['object_list'])
        # Update limits in programm data
        programm_data = work.update_limits(programm_data)
        save_data.save(f"files/programm_data.json", programm_data)
        # Create a new json file of day, if txt file in that day is existing.
        main_list = []
        programm_data, main_list, IsExisiting = open_data.create_file_of_new_day(
            programm_data)
        save_data.save(f"files/programm_data.json", programm_data)
        # Save data from new json file or print message which writed in what file is not existing.
        if (IsExisiting == True):
            save_data.save(
                f"files/{max(programm_data['Existing_files'])}.json", main_list)
        else:
            print(
                f"File with name - {max(programm_data['Existing_files']) + 1} is't existing.")
        # Save programm_data.
        save_data.save(f"files/programm_data.json", programm_data)
        # User part
    while True:
        inp = input()
        if (inp == "end"):
            break
        elif(inp == "wt"):
            print("How much days need to print??")
            days_for_get_data = int(input())
            print(statistic.get_data_week(days_for_get_data))
        elif(inp == "l"):
            print(programm_data['limits_for_files'][f"{len(programm_data['limits_for_files'])}"])
        elif(inp == "add_act"):
            print("Input name your activity.")
            name = input()
            print("Input period.")
            period = input()
            print("Input value from minuts for embeded activity.")
            value = input()
            activites_data = work.add_activity(activites_data, name=name, value=value, period=period)
            save_data.save('files/activites_data.json', activites_data)
        elif(inp == "p_act"):
            for period, list in dict(activites_data).items():
                print(period)
                print(*list, sep = "\n")
