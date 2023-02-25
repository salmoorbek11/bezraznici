import json

def readJson(file):
    with open (f'{file}') as json_file:
        data = json.load(json_file)
    return data['people']


file = 'salmoorbek_data.json'
print(readJson(file))