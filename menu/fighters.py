import time
import main as start
import data.datafunctions as df

fighters = df.load_data()


def fighter_picker(fname):
    picked_fighter = {}
    for fighter in fighters:
        if fighter['fname'] == fname:
            picked_fighter = fighter

    return picked_fighter


def fighter_info(fighter):
    time.sleep(1)  # bikin tidur
    start.clear_screen()  # bersih

    print("="*40)
    print(" " * 13 + "FIGHTER INFO")
    print("="*40 + "\n")

    print(f"Name: {fighter["fname"]} ")
    print(f"Level: {fighter['level']}")
    print("\n")
    print("="*40)

    print("'e' to edit current player name\n'd' to delete current player\n")
    action = input("Choose your action!: ")

    if action == "d":
        print("Are you sure you want to delete this fighter?")
        dchoice = input("[y] Yes, [n] No: ")
        if dchoice == "d":
            print("deleting...")


def add_fighters_menu():
    time.sleep(1)  # bikin tidur
    start.clear_screen()  # bersih
    name = str(input("New fighter name = "))

    time.sleep(0.9)

    print("new fighter created!\n")
    print("")

    time.sleep(1)

    print("Going back to the fighter display...")

    time.sleep(1)

    fighters_display()


def fighters_display():
    # inisialisasi
    choice = ""  # bikin variable buat nyimpan pilihan player
    fighter = {}

    time.sleep(1)  # bikin tidur
    start.clear_screen()  # bersih

    # display
    print("="*40)
    print(" " * 10 + "AVAILABLE FIGHTERS")
    print("="*40 + "\n")

    for i, fighter in enumerate(fighters):
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
        fighter_info(fighters[int(choice) - 1])
