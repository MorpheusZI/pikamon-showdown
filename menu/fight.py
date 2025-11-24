import fungsi.datafunctions as df
import fungsi.helperfunctions as hf
import random
import math
import time

from main import display_start_menu

pikamons = df.load_data('pikamons')
nfighters = df.load_data('fighters')

# Fighter Picking


def fight_initiation():
    # pick fighter
    fighter = fighter_pick_display()
    fighter_pikamons = hf.fighter_pikamon_pickers(fighter, pikamons)

    # pick pikamons
    pikamon = pikamon_pick_display(fighter_pikamons)
    # randomly select opponents
    opp_pikamon = opponent_pikamon_picker()

    battle_stats = fighting_sequence(fighter, pikamon, opp_pikamon)
    result_display(battle_stats)


def fighter_pick_display():
    hf.wiper()

    hf.list_of_fighters(nfighters)

    print("'q' to go back to start menu")
    choice = input("\nChoose your fighter!: ")

    if choice == 'q':
        display_start_menu()
        return

    return nfighters[int(choice)-1]


def pikamon_pick_display(pikamons):
    hf.wiper()

    hf.list_of_pikamons(pikamons)

    print("'q' to go back to start menu")
    choice = input("\nChoose your Pikamon!: ")

    if choice == 'q':
        display_start_menu()
        return

    while int(choice) > len(pikamons):
        choice = int(input("bad option.. \nChoose your fighter!: "))

    return pikamons[int(choice)-1]


def opponent_pikamon_picker():
    hf.wiper()

    hf.boring_loading_lines()

    selected_opponent = random.choice(pikamons)

    hf.wiper()

    print("Opponent Found!\n")
    time.sleep(0.9)
    print(f"your opponent is {selected_opponent['name']}")

    return selected_opponent


def get_health_bar(current_hp, max_hp=100, length=20):
    current_hp = max(0, current_hp)
    filled_len = int((current_hp / max_hp) * length)
    bar = "█" * filled_len + "-" * (length - filled_len)
    return f"[{bar}] {current_hp}/{max_hp}"


def draw_scene(player, enemy):

    hf.wiper()

    print("=" * 60)
    print(f" {player['name'].ljust(25)} VS {enemy['name'].rjust(25)} ")
    print(f" {get_health_bar(player['health']).ljust(25)}    {
          get_health_bar(enemy['health']).rjust(25)} ")
    print("=" * 60)
    print("\n")

    p_art = [
        "    ( ^_^)/   ",
        "   /|   |    ",
        "    |   |   ",
        "   /     \   "
    ]

    e_art = [
        "   \(ò_ó )   ",
        "    |   |\   ",
        "    |   |    ",
        "   /    \   "
    ]

    # Print them side by side
    for p_line, e_line in zip(p_art, e_art):
        # 25 spaces for player side, some gap, then enemy side
        print(f"{p_line.center(28)}      {e_line.center(28)}")

    print("\n" + "-" * 60)


def fighting_sequence(fighter, pikamon, opp):
    round = 1

    pikamon["health"] = 100
    opp["health"] = 100

    battle_stats = {
        "fighter": fighter,
        "pikamon": pikamon["name"],
        "opponent_pikamon": opp,
        "rounds": round,
        "fighter_damage_made": 0,
        "opp_damage_made": 0,
        "result": ''
    }

    print(f"--- BATTLE START: {pikamon['name']} VS {opp['name']} ---")

    while pikamon["health"] > 0 and opp["health"] > 0:
        draw_scene(pikamon, opp)
        print("="*25 + f" ROUND {round} " + "="*26 + "\n")

        # =================== PLAYER ======================
        time.sleep(1)
        print(f"Choose your attack for {pikamon['name']}:")

        time.sleep(0.7)
        for i, atk in enumerate(pikamon["attacks"]):
            print(f"{i+1}. {atk['name']} (DMG: {atk['dmg']})")

        choice = input("\nEnter attack number (1 or 2): ")
        while choice not in ["1", "2"]:
            choice = input("Invalid choice. Enter 1 or 2: ")

        player_attack = pikamon["attacks"][int(choice) - 1]

        dmg_to_opp = math.floor(player_attack["dmg"] - (opp["def"] / 100))
        battle_stats["fighter_damage_made"] += dmg_to_opp
        opp["health"] -= dmg_to_opp

        time.sleep(0.3)
        print(f"> {pikamon['name']} used {player_attack['name']}!")
        time.sleep(0.4)
        print(f"> It hit {opp['name']} for {dmg_to_opp} damage!\n")

        if opp["health"] <= 0:
            time.sleep(0.7)
            print(f"\n*** {opp['name']} has fainted! YOU WIN! ***")
            time.sleep(2)
            battle_stats["result"] = "won"
            break

        # ============= AI ================
        opp_attack = random.choice(opp["attacks"])

        dmg_to_player = math.floor(opp_attack["dmg"] - (pikamon["def"]/100))
        battle_stats["opp_damage_made"] += dmg_to_player
        pikamon["health"] -= dmg_to_player

        time.sleep(1.5)
        print(f"\n> {opp['name']} attacks back with {opp_attack['name']}!")
        time.sleep(0.7)
        print(f"> It hit {pikamon['name']} for {dmg_to_player} damage!")
        time.sleep(1.3)
        print("\n!>>Round ended. going to the next round...")
        time.sleep(2)

        if pikamon["health"] <= 0:
            time.sleep(0.7)
            print(f"\n*** {pikamon['name']} has fainted! YOU LOSE! ***")
            battle_stats["result"] = "lost"
            break

        round += 1

    return battle_stats


def result_display(result):
    fighter_name = result["fighter"]["fname"]
    opp_pikamon_name = result["opponent_pikamon"]["name"]
    fighter_id = result["fighter"]["id"]
    opp_pikamon_id = result["opponent_pikamon"]["id"]

    update_data = {
        "option": "level"
    }

    hf.wiper()

    print("-"*40)
    print("BATTLE STATS".ljust(20))
    print("-"*40+"\n")

    time.sleep(1)
    print(f"1. Fighter: {fighter_name}")
    time.sleep(0.7)
    print(f"2. Pikamon: {result['pikamon']}")
    time.sleep(0.7)
    print(f"3. Opponent Pikamon: {opp_pikamon_name}")
    time.sleep(1)
    print(f"4. Pikamon total damage made: {result['fighter_damage_made']}")
    time.sleep(1)
    print(f"5. Opponent total damage made: {result['opp_damage_made']}")
    time.sleep(1)
    print(f"6. Result: {result['result']}")
    time.sleep(1)
    print("-"*40+"\n")

    if result["result"] == "won":
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!! Congrats on WINNING !!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        time.sleep(1)

        df.update_fighter(fighter_id, update_data)
        print("Your fighter has just leveled up!\n")

        if opp_pikamon_name != result['pikamon']:

            time.sleep(1)
            print(f"Would you like to capture {
                  opp_pikamon_name} as your own pikamon?\n")
            print(">[y] Capture the Pikamon")
            print(">[n] let the Pikamon free\n")
            time.sleep(0.7)
            choice = str(input(">> Choose your action!: "))

            while choice not in ["y", "n"]:
                choice = str(input(">>Invalid option. Choose your action!: "))

            if choice == "y":
                update_data = {
                    "option": "capture",
                    "data": opp_pikamon_id
                }
                df.update_fighter(fighter_id, update_data)
                time.sleep(0.5)
                print(f"\nNow {opp_pikamon_name} is yours! ")
                time.sleep(1.5)
                print("\ngoing back to start menu...")
                time.sleep(1)
                display_start_menu()

            elif choice == "n":
                print("\ngoing back to start menu...")
                time.sleep(1)
                display_start_menu()
        else:
            print("\ngoing back to start menu...")
            time.sleep(1)
            display_start_menu()
    else:
        print("you suck!")
        time.sleep(1)
        print("going back to start menu...")
        time.sleep(1)
        display_start_menu()
