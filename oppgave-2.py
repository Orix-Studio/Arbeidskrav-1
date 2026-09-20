def test(session_list):
    print("test")

def register_session(session_list):
    # Tema for økten
    while True:
        topic = input("Hva er tema for økten? ").strip().capitalize()
        if topic == "":
            print("Du må fylle ut dette feltet.\n")
        else:
            break

    # Varighet på økten
    while True:
        try:
            duration = int(input("Hvor lenge varer økten (m)? ").strip())
            if duration > 0:
                break
            else:
                print("Øktens lengde kan ikke være under 1 minutt.\n")
        except ValueError:
            print("Lengden må oppgis som antall minutter.\n")

    # Status på økten
    while True:
        status = input("Er økten 'Planlagt' eller 'Fullført'? ").strip().lower()
        if status == "planlagt":
            status = "planned"
            break
        elif status == "fullført":
            status = "completed"
            break
        else:
            print("Du må velge mellom 'Planlagt' eller 'Fullført'. Prøv igjen.\n")

    # Lagre økten med oppgitt data
    session_list.append({"topic": topic, "duration": duration, "status": status})
    print("Økten er registrert og lagret!")


def exit_program(session_list):
    # Enkel mulighet til å lagre listen i en ekstern fil ved ønske
    print("\nAvslutter programmet. Ha en fin dag!")
    return False


menu = [
    {"title": "Registrer en studieøkt", "action": register_session},
    {"title": "Vis alle studieøkter", "action": test},
    {"title": "Vis bare fullførte studieøkter", "action": test},
    {"title": "Søke etter et ord i temaet", "action": test},
    {"title": "Sorter øktene etter varighet, lengst først", "action": test},
    {"title": "Vis samlet og gjennomsnittlig varighet for fullførte økter", "action": test},
    {"title": "Avslutt programmet", "action": exit_program},
]

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