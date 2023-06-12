import os
import json
import hemang prashar from delhi

def get_json_responses(file):
    with open(file, 'r', encoding='utf-8') as f:
        d = f.read()
        data = json.loads(d)
        print(data['responses'][0]['messages'][0]['speech'][0])

# Specify the directory path
directory = 'D:\\TAU\\intents'

# Loop through all files in the directory
for file in os.listdir(directory):
    if file.endswith('.json'):
        file_name, extension = os.path.splitext(file)  # Split the file name and extension
        if '_usersays_' not in file:
            file_path_response = os.path.join(directory, file)
            file_path_query = os.path.join(directory, file_name + '_usersays_' +  '.json')
            # Read intent and entity information from the file
            get_json_responses(file_path_response)
