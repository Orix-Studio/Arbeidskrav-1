from Components.ComponentsFive.FunctionLibrary import Activity, register_show_activities, search_title_category, filter_status, sort_date_duration, mark_completed, activity_statistics, save_exit_program

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

# Check for saved activities and import
try:
    with open("activities.txt", "r", encoding="utf-8") as file:
        for line in file:
            split_line = line.strip().split(",")

            if len(split_line) == 6:
                try:
                    title = split_line[0]
                    category = split_line[1]
                    date = split_line[2]
                    date_format = (split_line[3])
                    estimated_minutes = int(split_line[4])
                    status = split_line[5]

                    imported_activity = Activity(title, category, date, date_format, estimated_minutes, status)
                    activities.append(imported_activity)

                except ValueError:
                    print(f"En feil oppstod ved formattering av følgende aktivitet:\n"
                          f"{split_line}\n")

except FileNotFoundError:
    # Catch Error if file doesn't exist
    print("Fant ingen lagrede aktiviteter å importere i activities.txt.")

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