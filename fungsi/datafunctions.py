import json

# ----------JSON Data Functions---------


def load_data(F_or_P):
    try:
        with open(f'./data/{F_or_P}.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError as e:
        raise e


def save_data(data):
    with open('./data/fighters.json', 'w') as file:
        json.dump(data, file, indent=4)


# ----------Fighters Data Functions-----------


def add_fighter(fname, starter_pokemon_id):
    fighters = load_data('fighters')
    last_fighter_id = fighters[len(fighters) - 1]["id"]
    new_fighter = {
        "id": last_fighter_id+1,
        "fname": fname,
        "level": 1,
        "pikamons": [starter_pokemon_id]
    }  # dummy data

    fighters.append(new_fighter)
    save_data(fighters)


def update_fighter(fid, data):
    fighterz = load_data('fighters')
    if data["option"] == 'name':
        user_found = False
        for fighter in fighterz:
            if fighter["id"] == fid:
                fighter["fname"] = data["data"]
                user_found = True
                break
        if user_found:
            save_data(fighterz)
        else:
            print("ga bisa coy")


def delete_fighter(fid):
    fighterz = load_data('fighters')
    user_yang_akan_di_delete = {}

    for fighter in fighterz:
        if fighter["id"] == fid:
            user_yang_akan_di_delete = fighter
            break
    if user_yang_akan_di_delete:
        fighterz.remove(user_yang_akan_di_delete)
        save_data(fighterz)
