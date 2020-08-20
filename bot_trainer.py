import json
from collections import defaultdict
import os
directory = 'Botdata/'
knowledge = defaultdict(list)
key_value = []
special_char = ['@','_','!','#','$','%','^','&','*','(',')','<','>',
                '?','/','\\','|','{','}','~',';',':','\'','"']

for filename in os.listdir(directory):
    counter = 0
    keys = []
    values = []

    f = open(f"Botdata/{filename}")

    for line in f:
        if("- - " in line):
            keys.append(line)
        elif("  -" in line):
            values.append(line)
        else:
            continue
    f.close()
    for key,value in zip(keys,values):
        keys[counter] = key.replace("- - ", "")
        values[counter] = value.replace("  - ","")
        counter += 1

    counter = 0

    # removing \n characters
    for key,value in zip(keys,values):
        keys[counter] = key.replace("\n", "")
        keys[counter] = keys[counter].lower()
        values[counter] = value.replace("\n","")
        values[counter] = values[counter].lower()
        counter += 1

    counter = 0

    # removing special characters
    for key,value in zip(keys,values):
        for i in special_char:
            if i in key:
                keys[counter] = key.replace(i,"")
            if i in value:
                values[counter] = value.replace(i,"")
        counter += 1



    for key,value in zip(keys,values):
        a = (key,value)
        key_value.append(a)



for key, value in key_value:
    knowledge[key].append(value)

with open("mainknowledge/MainKnowledge.json", "w") as file:
    json.dump(knowledge, file)

