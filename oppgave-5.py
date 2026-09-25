from Components.ComponentsFive.FunctionLibrary import register_show_activities, search_title_category, filter_status, sort_date_duration, mark_completed, activity_statistics, save_exit_program

menu = (
    {"title": "Registrer og vis aktiviteter", "action": register_show_activities},
    {"title": "Søk etter tittel eller kategori", "action": search_title_category},
    {"title": "Filtrer etter status", "action": filter_status},
    {"title": "Sorter etter dato eller varighet", "action": sort_date_duration},
    {"title": "Marker en aktivitet som fullført", "action": mark_completed},
    {"title": "Vis antall aktiviteter, planlagte/fullførte og samlet estimert tid", "action": activity_statistics},
    {"title": "Lagre og avslutt program", "action": save_exit_program},
)

activities = []
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
                chosen_function = menu[menu_input - 1]["action"](activities)

                if chosen_function is False:
                    program_status = False
                break
            else:
                print(f"Ugyldig valg. Velg et tall mellom 1 og {len(menu)}.")

        except ValueError:
            print("Du må oppgi et gyldig tall. Se i menyen ovenfor.")