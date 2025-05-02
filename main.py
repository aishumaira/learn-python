import json
data = {
    'firstname' : 'Ahmad',
    'lastname' : 'Maulana',
    'age' : 26,
    'hobbies' : [
        'swimming',
        'programming'
    ]
}

data_json = json.dumps(data)
print(data_json)