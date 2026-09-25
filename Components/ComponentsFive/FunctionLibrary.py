def test(activities):
    print(f"Test {activities}")


class Activity:
    def __init__(self, title, category, date, estimated_minutes, status):
        self.title = title
        self.category = category
        self.date = date
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
                            datetime.date(int(date_split[2]), int(date_split[1]), int(date_split[0]))
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


                summary = Activity(title, category, date, minutes, status)
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


def save_exit_program(activities):
    if activities:
        with open("activities.txt", "w", encoding="utf-8") as file:
            for activity in activities:
                file.write(f"{activity}\n")

            print("Lagrer og avslutter programmet. Ha en fin dag!")
            return False
    else:
        print("Avslutter programmet.")
        return False