import time
import json
import os


def display_arena():

    clear_screen()
    time.sleep(1)
    print("="*60)
    print(" "*5 + "F I G H T I N G")
    print("="*60)

    print("="*30 + "|" + "="*29)
    print(" "*30+"|")
    print(" "*30+"|")
    print(" YOUR POKEMON" + " " + "vs")
    print(" "*30+"|")
    print(" "*30+"|")
    print("="*30 + "|" + "="*29)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


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


fighters = load_data('fighters')
pikamons = load_data('pikamons')


def fighter_info(fighter):
    time.sleep(1)  # bikin tidur
    clear_screen()  # bersih

    print("="*40)
    print(" " * 13 + "FIGHTER INFO")
    print("="*40 + "\n")

    print(f"Name: {fighter["fname"]}\n")
    print(f"Level: {fighter['level']}\n")
    print("="*40)

    print("'u' to edit current player name\n'd' to delete current player\n")
    action = input("Choose your action!: ")

    if action == "d":
        print("Are you sure you want to delete this fighter?")
        dchoice = input("[y] Yes, [n] No: ")
        if dchoice == "y":
            delete_fighter(fighter["id"])
            print("Fighter deleted...\nGoing back to fighter display")
            time.sleep(1)
            fighters_display()
    elif action == "u":
        update_fighter_menu(fighter["id"])


def update_fighter_menu(fighter_id):
    time.sleep(1)  # bikin tidur
    clear_screen()  # bersih

    print("="*40)
    print(" " * 9 + "FIGHTER UPDATE")
    print("="*40 + "\n")

    fname = str(input(">> New fighter name = "))
    new_data = {
        'option': "name",
        'data': fname,
    }
    update_fighter(fighter_id, new_data)

    time.sleep(1)

    print(f"\nHello {fname}!")
    print("fighter updated!\n")

    time.sleep(1)

    print("Going back to the fighter display...")

    time.sleep(1)

    fighters_display()


def add_fighters_menu():
    time.sleep(1)  # bikin tidur
    clear_screen()  # bersih

    print("="*40)
    print(" " * 7 + "NEW FIGHTER CREATION")
    print("="*40 + "\n")

    fname = str(input(">> New fighter name = "))

    time.sleep(1)

    print(f"\nHello {fname}!")
    print("Heres a list of pokemons you can choose to be your new friend!:\n")
    print("-"*60)
    print("No.| Name | Defense | Attacks[name,damage] |")
    print("-"*60)
    for i in range(3):
        current_pikamon = pikamons[i]
        pikamon_attacks = current_pikamon['attacks']
        fixed_string = ""

        for attack in pikamon_attacks:
            fixed_string += f'[{attack["name"]},{attack["dmg"]}]'

        print(
            f"{i+1}.| {current_pikamon['name']} | {current_pikamon['def']} | {fixed_string} | \n")

    starter_pikamon = int(input("\n>> Pick your starter pokemon! (e.g 1,2): "))

    add_fighter(fname, starter_pikamon)

    print("new fighter created!\n")

    time.sleep(1)

    print("Going back to the fighter display...")

    time.sleep(1)

    fighters_display()


def fighters_display():
    # inisialisasi
    nfighters = load_data('fighters')
    choice = ""  # bikin variable buat nyimpan pilihan player

    time.sleep(1)  # bikin tidur
    clear_screen()  # bersih

    # display
    print("="*40)
    print(" " * 10 + "AVAILABLE FIGHTERS")
    print("="*40 + "\n")

    for i, fighter in enumerate(nfighters):
        print(f"{i+1}. Name: {fighter["fname"]} ")
        print("   Level: " + str(fighter["level"]))

        print("\n")
    print("="*40 + "\n")

    print("Add Fighters! (a)")
    # pemilihan
    choice = str(
        input("Pick your fighters! (e.g. 1,2)\n'q' to go back to menu: "))

    if choice == "q":
        display_start_menu()
    elif choice == "a":
        print("\nGoing to add fighters menu...")
        time.sleep(1)
        add_fighters_menu()
    else:
        fighter_info(nfighters[int(choice) - 1])


def display_start_menu():
    clear_screen()
    print("===========================================================")
    print("  PPPPPP IIIIII KKK  KKK AAAAAA MMMMMMMMMM OOOOOO NNNNNN !")
    print("  PP  PP   II   KK  KKK  AA  AA MM  MM  MM OO  OO NN  NN !")
    print("  PPPPPP   II   KKKKK    AAAAAA MM  MM  MM OO  OO NN  NN !")
    print("  PP       II   KK  KKK  AA  AA MM  MM  MM OO  OO NN  NN !")
    print("  PP     IIIIII KKK  KKK AA  AA MM  MM  MM OOOOOO NN  NN !")
    print("===========================================================")
    print("           BY KELOMPOK 12 (MOAL UAS)")
    print("-----------------------------------------------------------")

    print("\n")
    print("1.  FIGHT!")
    print("2.  FIGHTER INFO!")
    print("3.  QUIT")
    print("\n")

    print("--------------------------------------------------------")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        display_arena()
    elif choice == "2":
        fighters_display()
    elif choice == "3":
        quit()


if __name__ == "__main__":
    display_start_menu()
# ----------JSON Data Functions---------
