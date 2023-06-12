import os
import json
import pandas as pd

directory = 'D:\\TAU\\intents'
lang = 'es'

def get_json_responses(file):
    messages = []
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for i in range(len(data['responses'])):
            for j in range(len(data['responses'][i]['messages'])):
                if 'speech' in data['responses'][i]['messages'][j]:
                    if data['responses'][i]['messages'][j]['lang'] == lang:
                        messages.append(data['responses'][i]['messages'][j]['speech'][0])
                else:
                    print(f"Warning: 'speech' key not found in file: {file}")
        return messages

def get_json_queries(file):
    queries = []
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                for item in data:
                    text = ''.join(fragment['text'] for fragment in item.get('data', []))
                    queries.append(text)
            elif isinstance(data, dict):
                text = ''.join(fragment['text'] for fragment in data.get('data', []))
                queries.append(text)
    except FileNotFoundError:
        print(f'File not found: {file}')
    return queries

# create a DataFrame to store the data
data = {'Intents': [], 'Query': [], 'Response': []}

# loop through all files in the directory
for file in os.listdir(directory):
    if file.endswith('.json'):
        try:
            file_name, ext = file.rsplit(".")
        except:
            print(f'====Error===={file}')
            continue
        if file.rfind('_usersays_') == -1:
            file_path_response = os.path.join(directory, file)
            file_path_query = os.path.join(directory, file_name + '_usersays_' + lang + '.json')
            responses = get_json_responses(file_path_response)
            queries = get_json_queries(file_path_query)
            for q in queries:
                if responses:
                    r = responses[0]
                else:
                    r = ''
                data['Intents'].append(file_name)
                data['Query'].append(q)
                data['Response'].append(r.replace('\u202f', ' ', 99).replace('\u0301', ' '))

# create a DataFrame from the data
df = pd.DataFrame(data)

# write the DataFrame to an Excel file
excel_file = 'ab.xlsx'
df.to_excel(excel_file, index=False)
