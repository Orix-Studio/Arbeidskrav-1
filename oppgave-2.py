def test():
    print("test")

def exit_program():
    print("\nAvslutter programmet. Ha en fin dag!")
    return False


menu = [
    {"title": "Registrer en studieøkt", "action": test},
    {"title": "Vis alle studieøkter", "action": test},
    {"title": "Vis bare fullførte studieøkter", "action": test},
    {"title": "Søke etter et ord i temaet", "action": test},
    {"title": "Sorter øktene etter varighet, lengst først", "action": test},
    {"title": "Vis samlet og gjennomsnittlig varighet for fullførte økter", "action": test},
    {"title": "Avslutt programmet", "action": exit_program},
]

program_status = True

while program_status:
    for i, menu_item in enumerate(menu, start=1):
        print(f"{i}. {menu_item['title']}")

    while True:
        try:
            menu_input = int(input("\nVelg en handling: ").strip())

            if 0 < menu_input <= len(menu):
                chosen_function = menu[menu_input - 1]["action"]()
                print()

                if chosen_function is False:
                    program_status = False
                break
            else:
                print(f"Ugyldig valg. Velg et tall mellom 1 og {len(menu)}.")

        except ValueError:
            print("Du må oppgi et gyldig tall. Se i menyen ovenfor.")