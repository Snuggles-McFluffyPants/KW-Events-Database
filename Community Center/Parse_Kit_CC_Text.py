"""
Parse all the text into something easier to navigate
"""

import json
import re

# Opening JSON file
file_name = "Kitchener_CC_Programs"

# Function to insert character to a particular point in a string
def insert_chars(string, index, char):
    return string[:index] + char + string[index:]

# Open the nested list with a string and get a list from it
def json_to_list(filename):
    f = open(file_name, )

    # returns JSON object
    raw_data = json.load(f)

    """ 
    Processing the raw data 
    """
    # Inserting line spaces between event endings
    raw_data = "\n".join(raw_data)
    raw_data = raw_data.replace("View Registration Info","View Registration Info\n")
    raw_data = raw_data.replace("View fee details","View fee details\n")
    raw_data = raw_data.replace("\nFree\n","\nFree\n\n")
    raw_data = raw_data.replace("\nIn progress\n","\n\nIn progress\n")
    raw_data = raw_data.replace("\nFull\n","\n\nFull\n")



    # Dealing with cases which finish with event costs
    cost_occurances = []
    for m in re.finditer('\$', raw_data):
        x = m.start()
        cost_occurances.append(x)

    cost_occurances.reverse()

    for i in cost_occurances:
        x = raw_data.find("\n", i)
        raw_data = insert_chars(raw_data, x, "\n")

    # Seperate events with only 2 new lines
    raw_data = raw_data.replace("\n\n\n","\n\n")
    raw_data = raw_data.replace("\n\n\n","\n\n")

    # Remove white space at the end of raw_data
    raw_data.rstrip()
    # print(raw_data)

    # divide everything into lists
    event_list = raw_data.split("\n\n")
    # print(type(raw_data))

    event_list2 = []
    for item in event_list:
        i = item.split("\n")
        # print(i)
        if i[0] != "Full":
                if i[0] != "In progress":
                    if i[0] != "Starting soon":
                        if "space(s) left" not in i[0]:
                            i.insert(0, "All good")
        # Remove list items that are too short
        new_list = [x for x in i if len(x) >= 3]

        # Add to the end of a list if the list is too short
        if len(new_list) < 7:
            new_list.append("")

        event_list2.append(new_list)
        if len(new_list) != 7:
            print("\n".join(new_list))

    return event_list2

if __name__ == "__main__":
    events = json_to_list("Weekend_Events.json")
    print(events)
    for i in events:
        print(len(i))
