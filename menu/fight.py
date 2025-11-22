import fungsi.datafunctions as df
import fungsi.helperfunctions as hf
import main as start
import random
import time

pikamons = df.load_data('pikamons')
nfighters = df.load_data('fighters')

# Fighter Picking


def fighting_sequence():

    # pick fighter
    fighter = fighter_pick_display()
    fighter_pikamons = hf.fighter_pikamon_pickers(fighter, pikamons)

    # pick pikamons
    pikamon = pikamon_pick_display(fighter_pikamons)
    # randomly select opponents
    opp_pikamon = opponent_pikamon_picker()

    pikamon["health"] = 100
    opp_pikamon["health"] = 100


def fighter_pick_display():
    time.sleep(1)
    start.clear_screen()

    hf.list_of_fighters(nfighters)

    choice = int(
        input("\nChoose your fighter!: "))

    while choice > len(nfighters):
        choice = int(input("bad option.. \nChoose your fighter!: "))

    return nfighters[choice-1]


def pikamon_pick_display(pikamons):

    time.sleep(1)
    start.clear_screen()

    hf.list_of_pikamons(pikamons)

    choice = int(
        input("\nChoose your pikamon to fight!: "))

    while choice > len(pikamons):
        choice = int(input("bad option.. \nChoose your fighter!: "))

    return pikamons[choice-1]


def opponent_pikamon_picker():
    random_pikamon_id = random.randint(1, 10) - 1
    return pikamons[random_pikamon_id]
