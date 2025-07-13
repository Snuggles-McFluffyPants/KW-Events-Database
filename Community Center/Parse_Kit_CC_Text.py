"""
Take text from community center websites from json file and put it into a Panda Dataframe
"""

import json
import pandas as pd


delimeters = ["Full", "View sub-activities", "View fee details"]

# A function specifically for parsing all the text from Kitchener Community center website returning a nested list
# largest nested list is of all programs with lists of containing program attributes
def parse_text(raw_string):
    # print(raw_string,"\n\n_-_-_-_\n\n")

    raw_data_list = raw_string.split("\n")

    program_list_1 = []
    program = []
    next_program = []

    for item in raw_data_list:
        # if "#" in row, add this and the last item to the next program, then with the other stuff append program_list_1
        if "#" in item:
            next_program.append(program[-1])
            next_program.append(item)
            program = program [0:-1]

            program_list_1.append(program)
            program = next_program
            next_program = []
            # print(program_list_1[-1])
        else:
            program.append(item)

    program_list_1.append(program)

    program_list_2 = []
    for item in program_list_1:
        if len(item) > 8:
            for line in item:
                print(line)
                pass
            print("\n")
        else:
            program_list_2.append(item)

    print("Amount of programs = ",len(program_list_1))




if __name__ == "__main__":

    file_name = "Kitchener_CC_Programs"

    f = open(file_name, )

    # returns JSON object
    raw_string = json.load(f)

    program_list = parse_text(raw_string)


    # print("Skip to main content\nEnglish\nSign In |Create an Account\nHome\nRegister for Activities\nFacilities\nActivity Calendars\nMemberships\nMy Cart\nhome>\nactivity search\nActivity search\nSearch by keyword OR by number\nSearch\nWhen\nWhere\nWho\nActivities\nOpen spots\nIn progress / Future\nFound 2064 matching result(s)\nSort by:\nDate range\nMap view\nFull\nKnitting (In stitches)\n#160347/55 yrs +/Openings 0\nBreithaupt Centre\nSeptember 5, 2024 to August 28, 2025\nThu 1:00 PM - 3:00 PM\nFree\nIn progress\nEuchre\n#160345/18 yrs +/Openings 23\nBreithaupt Centre\nSeptember 6, 2024 to August 29, 2025\nFri 12:45 PM - 3:45 PM\nFree\nEnroll Now\nIn progress")
