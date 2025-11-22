import menu.fight as fightmenu
import menu.fighters as fighters
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


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
        fightmenu.display_arena()
    elif choice == "2":
        fighters.fighters_display()
    elif choice == "3":
        quit()


if __name__ == "__main__":
    display_start_menu()
