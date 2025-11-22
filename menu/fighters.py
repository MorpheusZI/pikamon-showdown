import time
import main as start
import fungsi.datafunctions as df
import fungsi.helperfunctions as hf

fighters = df.load_data('fighters')
pikamons = df.load_data('pikamons')


def fighters_display():
    hf.wiper()
    # inisialisasi
    nfighters = df.load_data('fighters')

    # display
    hf.list_of_fighters(nfighters)

    print("Type a fighter index to see their info!")
    print("'a' to add a fighter")
    print("'q' to go back to start menu")

    # pemilihan
    choice = str(
        input("\nChoose your action!: "))

    if choice == "q":
        start.display_start_menu()
    elif choice == "a":
        print("\nGoing to add fighters menu...")
        time.sleep(1)
        add_fighters_menu()
    else:
        fighter_info(nfighters[int(choice) - 1])


def fighter_info(fighter):
    hf.wiper()

    fighter_pikamons = hf.fighter_pikamon_pickers(fighter, pikamons)

    print("="*40)
    print(" " * 13 + "FIGHTER INFO")
    print("="*40 + "\n")

    print(f"Name: {fighter["fname"]}\n")
    print(f"Level: {fighter['level']}\n")

    print("="*40)
    print(" " * 13 + "THEIR PIKAMONS")
    print("="*40 + "\n")

    hf.list_of_pikamons(fighter_pikamons)

    print("\n'u' to edit current player name\n'd' to delete current player")
    print("'q' to go back to fighters menu")
    action = input("\nChoose your action!: ")

    while action not in ["d", "u", "q"]:
        action = input("\nInvalid choice. Choose your action!: ")

    if action == "d":
        print("Are you sure you want to delete this fighter?")
        dchoice = input("[y] Yes, [n] No: ")

        if dchoice == "y":
            df.delete_fighter(fighter["id"])
            print("\nFighter deleted...\nGoing back to fighters menu")
            time.sleep(1)
            fighters_display()

        elif dchoice == "n":
            print("deletion action cancelled. going back to fighters menu..")
            time.sleep(1)
            fighters_display()

    elif action == "u":
        update_fighter_menu(fighter["id"])

    elif action == "q":
        print("going back to fighters menu...")
        time.sleep(1)
        fighters_display()


def update_fighter_menu(fighter_id):
    hf.wiper()

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
    print("fighter updated!\n")
    print(f"\nHello {fname}!")

    time.sleep(1)

    print("Going back to the fighter display...")

    time.sleep(1)

    fighters_display()


def add_fighters_menu():
    hf.wiper()

    print("="*40)
    print(" " * 7 + "NEW FIGHTER CREATION")
    print("="*40 + "\n")

    fname = str(input(">> New fighter name = "))

    time.sleep(1)

    print(f"\nHello {fname}!")
    print("Heres a list of pokemons you can choose to be your new friend!:\n")

    hf.list_of_pikamons(pikamons[:3])
    starter_pikamon = int(input("\n>> Pick your starter pokemon! (e.g 1,2): "))

    df.add_fighter(fname, starter_pikamon)

    time.sleep(1)
    print("new fighter created!\n")

    time.sleep(1)
    print("Going back to the fighter display...")

    time.sleep(1)
    fighters_display()
