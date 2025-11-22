def fighter_pikamon_pickers(fighter, pikamons):
    fighter_pikamons = []
    for pikamonid in fighter["pikamons"]:
        for pikamon in pikamons:
            if pikamon["id"] == pikamonid:
                fighter_pikamons.append(pikamon)
    return fighter_pikamons


def list_of_fighters(ifighters):

    print("="*40)
    print(" " * 10 + "AVAILABLE FIGHTERS")
    print("="*40 + "\n")

    for i, fighter in enumerate(ifighters):
        print(f"{i+1}. Name: {fighter["fname"]} ")
        print("   Level: " + str(fighter["level"]) + "\n")
    print("="*40 + "\n")


def list_of_pikamons(pikamons):

    print("No.| Name | Defense | Attacks[name,damage] |")
    print("-"*60)

    for i, pikamon in enumerate(pikamons):
        pikamon_attacks = pikamon['attacks']
        fixed_string = ""

        for attack in pikamon_attacks:
            fixed_string += f'[{attack["name"]},{attack["dmg"]}], '

        print(
            f"{i+1}.| {pikamon['name']} | {pikamon['def']} | {fixed_string}|")
    print("-"*60)
