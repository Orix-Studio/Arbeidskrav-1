class Activity:
    def __init__(self, title, category, date, date_format, estimated_minutes, status):
        self.title = title
        self.category = category
        self.date = date
        self.date_format = date_format
        self.estimated_minutes = estimated_minutes
        self.status = status

    def __str__(self):
        return (f"Tittel: {self.title}\n"
                f"Kategori: {self.category}\n"
                f"Dato: {self.date}\n"
                f"Estimert tid: {self.estimated_minutes} min\n"
                f"Status: {self.status.capitalize()}\n")


def register_show_activities(activities):
    while True:
        try:
            input_choice = int(input("1. Register ny aktivitet\n"
                                     "2. Vis alle aktiviteter\n"
                                     "3. Gå tilbake til menyen\n\n"
                                     "Velg en handling: "))

            if input_choice == 1:
                while True:
                    title = input("Skriv inn en tittel på aktiviteten: ").strip()
                    if title:
                        break
                    else:
                        print("Aktiviteten må ha en tittel. Feltet kan ikke stå tomt.\n")

                while True:
                    category = input("Skriv inn en kategori på aktiviteten: ").strip()
                    if category:
                        break
                    else:
                        print("Aktiviteten må ha en kategori. Feltet kan ikke stå tomt.\n")

                while True:
                    import datetime
                    date = input("Oppgi dato for aktiviteten (dd.mm.yyyy): ").strip()
                    date_split = date.split(".")

                    if len(date_split) == 3:
                        try:
                            date_format = datetime.date(int(date_split[2]), int(date_split[1]), int(date_split[0]))
                            break
                        except ValueError:
                            print("Ugyldig dato. Prøv igjen.\n")
                    else:
                        print("Ugyldig datoformat. Prøv igjen.\n")

                while True:
                    try:
                        minutes = int(input("Oppgi estimert varighet (minutter): "))
                        if minutes > 0:
                            break
                        else:
                            print("Varigheten kan ikke være 0 eller mindre.\n")
                    except ValueError:
                        print("Minutter må oppgis som heltall. Prøv igjen.\n")

                while True:
                    status = input("Er aktiviteten 'planlagt' eller 'fullført': ").strip().lower()
                    if status == "planlagt" or status == "fullført":
                        break
                    else:
                        print("Ugyldig status. Du må velge mellom 'planlagt' eller 'fullført'.\n")


                summary = Activity(title, category, date, date_format, minutes, status)
                print(f"\nOppsummering:\n"
                      f"{summary}")

                while True:
                    save_activity = input("Vil du lagre aktiviteten (ja/nei): ").strip().lower()
                    if save_activity == "ja":
                        activities.append(summary)
                        print("Aktiviteten er registrert.")
                        break
                    elif save_activity == "nei":
                        save_delete = input("Er du sikker på at du vil slette aktiviteten (ja/nei): ").strip().lower()
                        if save_delete == "ja":
                            break
                        elif save_delete == "nei":
                            continue
                        else:
                            print("Ugyldig svar. Velg enten 'ja' eller 'nei'.\n")
                    else:
                        print("Ugyldig svar. Velg enten 'ja' eller 'nei'.\n")

                break

            elif input_choice == 2:
                if activities:
                    print("Alle registrerte aktiviteter:\n")
                    for activity in activities:
                        print(activity)
                    break

                else:
                    print("Det finnes ingen registrerte aktiviteter.\n")
                    break

            elif input_choice == 3:
                break

            else:
                print("Tallet finnes ikke i menyen. Prøv igjen.\n")

        except ValueError:
            print("Du må skrive inn et heltall fra menyen over.\n")


def search_title_category(activities):
    if activities:
        while True:
            try:
                input_choice = int(input("1. Søk i tittel\n"
                                         "2. Søk i kategori\n"
                                         "3. Gå tilbake til menyen\n\n"
                                         "Velg en handling: "))

                if input_choice == 1:
                    while True:
                        search_title = input("Søk etter tittel i aktiviteter: ").strip().lower()
                        if search_title:
                            relevant_activities = []

                            for activity in activities:
                                if search_title in activity.title.lower():
                                    relevant_activities.append(activity)

                            if relevant_activities:
                                print(f"Aktiviteter med '{search_title}' i tittel:\n")
                                for activity in relevant_activities:
                                    print(activity)
                                break
                            else:
                                print(f"Fant ingen aktiviteter med '{search_title}' i tittel.\n")
                                break

                        else:
                            print("Søkefeltet kan ikke stå tomt.\n")

                elif input_choice == 2:
                    while True:
                        search_category = input("Søk etter kategori i aktiviteter: ").strip().lower()
                        if search_category:
                            relevant_activities = []

                            for activity in activities:
                                if search_category in activity.category.lower():
                                    relevant_activities.append(activity)

                            if relevant_activities:
                                print(f"Aktiviteter med '{search_category}' i kategori:\n")
                                for activity in relevant_activities:
                                    print(activity)
                                break
                            else:
                                print(f"Fant ingen aktiviteter med '{search_category}' i kategori.\n")
                                break

                        else:
                            print("Søkefeltet kan ikke stå tomt.\n")

                elif input_choice == 3:
                    break

                else:
                    print("Tallet finnes ikke i menyen. Prøv igjen.\n")

            except ValueError:
                print("Du må skrive inn et heltall fra menyen over.\n")

    else:
        print("Det finnes ingen registrerte aktiviteter å søke i.")


def filter_status(activities):
    if activities:
        while True:
            try:
                input_choice = int(input("1. Vis planlagte aktiviteter\n"
                                         "2. Vis fullførte aktiviteter\n"
                                         "3. Gå tilbake til menyen\n\n"
                                         "Velg en handling: "))

                if input_choice == 1:
                    relevant_activities = []

                    for activity in activities:
                        if activity.status == "planlagt":
                            relevant_activities.append(activity)

                    if relevant_activities:
                        for activity in relevant_activities:
                            print(activity)

                    else:
                        print("Det finnes ingen planlagte aktiviteter.\n")

                elif input_choice == 2:
                    relevant_activities = []

                    for activity in activities:
                        if activity.status == "fullført":
                            relevant_activities.append(activity)

                    if relevant_activities:
                        for activity in relevant_activities:
                            print(activity)

                    else:
                        print("Det finnes ingen fullførte aktiviteter.\n")

                elif input_choice == 3:
                    break

                else:
                    print("Tallet finnes ikke i menyen. Prøv igjen.\n")

            except ValueError:
                print("Du må skrive inn et heltall fra menyen over.\n")

    else:
        print("Det finnes ingen registrerte aktiviteter å filtrere.")


def sort_date_duration(activities):
    if activities:
        while True:
            try:
                input_choice = int(input("1. Sorter på dato\n"
                                         "2. Sorter på varighet\n"
                                         "3. Gå tilbake til menyen\n\n"
                                         "Velg en handling: "))

                if input_choice == 1:
                    sorted_date = sorted(activities, key=lambda item: item.date_format)

                    print("Aktiviteter sortert på dato:\n")
                    for activity in sorted_date:
                        print(activity)

                elif input_choice == 2:
                    sorted_duration = sorted(activities, key=lambda item: item.estimated_minutes)

                    print("Aktiviteter sortert på varighet:\n")
                    for activity in sorted_duration:
                        print(activity)

                elif input_choice == 3:
                    break

                else:
                    print("Tallet finnes ikke i menyen. Prøv igjen.\n")

            except ValueError:
                print("Du må skrive inn et heltall fra menyen over.\n")

    else:
        print("Det finnes ingen registrerte aktiviteter å sortere.")


def mark_completed(activities):
    if activities:
        planned_activities = []

        for activity in activities:
            if activity.status == "planlagt":
                planned_activities.append(activity)

        if planned_activities:
            while True:
                for i, activity in enumerate(planned_activities, start=1):
                    print(f"Valg: {i}")
                    print(activity)

                try:
                    choose_activity = int(input("Velg aktivitet du vil sette til 'fullført': "))

                    if 0 < choose_activity <= len(planned_activities):
                        planned_activities[choose_activity - 1].status = "fullført"
                        print(f"\nNy status for aktivitet:\n"
                              f"{planned_activities[choose_activity - 1]}")
                        break

                    else:
                        print("Valget ditt tilsvarer ingen aktiviteter i listen. Prøv igjen.\n")

                except ValueError:
                    print("Du må skrive inn et heltall tilsvarende aktiviteten du vil endre. Prøv igjen.\n")

        else:
            print("Alle aktiviteter er fullført.\n")

    else:
        print("Det finnes ingen registrerte aktiviteter.")


def activity_statistics(activities):
    if activities:
        activities_count = len(activities)

        total_minutes = 0
        planned_count = 0
        complete_count = 0
        for activity in activities:
            total_minutes += activity.estimated_minutes

            if activity.status == "planlagt":
                planned_count += 1

            elif activity.status == "fullført":
                complete_count += 1

        print(f"\nAntall aktiviteter: {activities_count}\n"
              f"Antall planlagte aktiviteter: {planned_count}\n"
              f"Antall fullførte aktiviteter: {complete_count}\n"
              f"Totalt estimert tid: {total_minutes} min\n")

    else:
        print("Det finnes ingen registrerte aktiviteter.")


def save_exit_program(activities):
    if activities:
        with open("activities.txt", "w", encoding="utf-8") as file:
            for activity in activities:
                file.write(f"{activity.title},{activity.category},{activity.date},{activity.date_format},{activity.estimated_minutes},{activity.status}\n")

            print("Lagrer og avslutter programmet. Ha en fin dag!")
            return False
    else:
        print("Avslutter programmet.")
        return False