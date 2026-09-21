from Components.ComponentsTwo.FunctionLibrary import register_session, view_sessions, completed_sessions, search_sessions, sort_duration, combined_average_time, exit_program

menu = (
    {"title": "Registrer en studieøkt", "action": register_session},
    {"title": "Vis alle studieøkter", "action": view_sessions},
    {"title": "Vis bare fullførte studieøkter", "action": completed_sessions},
    {"title": "Søke etter et ord i temaet", "action": search_sessions},
    {"title": "Sorter øktene etter varighet, lengst først", "action": sort_duration},
    {"title": "Vis samlet og gjennomsnittlig varighet for fullførte økter", "action": combined_average_time},
    {"title": "Avslutt programmet", "action": exit_program},
)

sessions = []
program_status = True

while program_status:
    print()
    for i, menu_item in enumerate(menu, start=1):
        print(f"{i}. {menu_item['title']}")

    while True:
        try:
            menu_input = int(input("\nVelg en handling: ").strip())

            if 0 < menu_input <= len(menu):
                print()
                chosen_function = menu[menu_input - 1]["action"](sessions)

                if chosen_function is False:
                    program_status = False
                break
            else:
                print(f"Ugyldig valg. Velg et tall mellom 1 og {len(menu)}.")

        except ValueError:
            print("Du må oppgi et gyldig tall. Se i menyen ovenfor.")