import json
import requests


# Classes accotiations
#####################
#####   people ######
#####################
# 1 : pedestrian
# 2 : cyclist
# 3 : person-sitting
#####################
##### venicle   #####
#####################
# 4 : car
# 5 : van
# 6 : tram
# 7 : truck
# 8 : misc
def id_to_ano(class_id):
    if class_id == 1:
        class_name = 'pedestrian    '
    elif class_id == 2:
        class_name = 'cyclist       '
    elif class_id == 3:
        class_name = 'person-sitting'
    elif class_id == 4:
        class_name = 'car           '
    elif class_id == 5:
        class_name = 'van           '
    elif class_id == 6:
        class_name = 'tram          '
    elif class_id == 7:
        class_name = 'truck         '
    else: #class_id == 8:
        class_name = 'misc          '
    return class_name


# Read JSON
with open("0000.json", "r") as read_file:
    data = json.load(read_file)

# Create JSON result structure
result = {}
res = []
# Read elements from {lists of dicts}

with open("data_file.json", "w") as write_file:
    for current in data:
        if current["score"] > 0.30:
            result["Slide"] = current["image_id"]
            result["Object"] = id_to_ano(current["category_id"])
            result["Score"] = current["score"]

            print("Slide number:", end=" ")
            print(result["Slide"], end=" ")
            print("Object:", end=" ")
            print(result["Object"], end=" ")
            print("Score:", end=" ")
            print(result["Score"])

            json.dump(result, write_file)
            #res.append(result)


# Create result json


print('hello')
