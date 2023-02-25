import json

data = {}
data['people'] = []
data['people'].append({ 
      "id": "04", 
      "name": "John", 
      "department": "HR"
})

with open('salmoorbek_data.json', 'w') as f:
    json.dump(data, f)