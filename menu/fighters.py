import time
import main as start
import fungsi.datafunctions as df

fighters = df.load_data('fighters')
pikamons = df.load_data('pikamons')


def fighters_display():
    # inisialisasi
    nfighters = df.load_data('fighters')
    choice = ""  # bikin variable buat nyimpan pilihan player

    time.sleep(1)  # bikin tidur
    start.clear_screen()  # bersih

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
        start.display_start_menu()
    elif choice == "a":
        print("\nGoing to add fighters menu...")
        time.sleep(1)
        add_fighters_menu()
    else:
        fighter_info(nfighters[int(choice) - 1])


def fighter_info(fighter):
    time.sleep(1)  # bikin tidur
    start.clear_screen()  # bersih

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
            df.delete_fighter(fighter["id"])
            print("Fighter deleted...\nGoing back to fighter display")
            time.sleep(1)
            fighters_display()
    elif action == "u":
        update_fighter_menu(fighter["id"])


def update_fighter_menu(fighter_id):
    time.sleep(1)  # bikin tidur
    start.clear_screen()  # bersih

    print("="*40)
    print(" " * 9 + "FIGHTER UPDATE")
    print("="*40 + "\n")

    fname = str(input(">> New fighter name = "))
    new_data = {
        'option': "name",
        'data': fname,
    }
    df.update_fighter(fighter_id, new_data)

    time.sleep(1)

    print(f"\nHello {fname}!")
    print("fighter updated!\n")

    time.sleep(1)

    print("Going back to the fighter display...")

    time.sleep(1)

    fighters_display()


def add_fighters_menu():
    time.sleep(1)  # bikin tidur
    start.clear_screen()  # bersih

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

    df.add_fighter(fname, starter_pikamon)

    print("new fighter created!\n")

    time.sleep(1)

    print("Going back to the fighter display...")

    time.sleep(1)

    fighters_display()
