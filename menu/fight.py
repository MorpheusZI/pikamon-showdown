from main import clear_screen

import time


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
