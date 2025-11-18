import json

# ----------JSON Data Functions---------


def load_data():
    try:
        with open('./data/fighters.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError as e:
        raise e


def save_data(data):
    with open('./data/fighters.json', 'w') as file:
        json.dump(data, file, indent=4)


# ----------Fighters Data Functions-----------

fighters = load_data()


def add_fighter(fname):

    new_fighter = {
        "id": len(fighters)+1,
        "fname": fname,
        "level": 1,
        "pikamons": []
    }
