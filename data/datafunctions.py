import json


def load_data():
    try:
        with open('./data/fighters.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError as e:
        raise e


def save_data(data):
    with open('./data/fighters.json', 'w') as file:
        json.dump(data, file, indent=4)
