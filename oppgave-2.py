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


def view_sessions(session_list):
    # Går gjennom alle økter og printer dem ut i brukervennlig format, hvis det finnes registrerte økter
    if session_list:
        for num, session in enumerate(session_list, start=1):
            print(f"Økt {num}:\n"
                  f"Tema: {session['topic']}\n"
                  f"Varighet: {session['duration']} minutter\n"
                  f"Status: {'Planlagt' if session['status'] == 'planned' else 'Fullført'}\n")

    # Gir feilmelding hvis det ikke finnes noen registrerte økter
    else:
        print("Det finnes ingen registrerte økter.")


def completed_sessions(session_list):
    if session_list:
        completed_sessions_list = [] # Liste for fullførte økter

        # Sjekker gjennom hver økt og legger den til i den nye listen hvis status == "completed"
        for session in session_list:
            if session["status"] == "completed":
                completed_sessions_list.append(session)

        # Sjekker om det er noen fullførte økter som er lagt til i den nye listen, deretter går gjennom hver økt og printer ut dataene for øktene.
        if completed_sessions_list:
            for num, session in enumerate(completed_sessions_list, start=1):
                print(f"Økt {num}:\n"
                      f"Tema: {session['topic']}\n"
                      f"Varighet: {session['duration']} minutter\n"
                      f"Status: {'Planlagt' if session['status'] == 'planned' else 'Fullført'}\n")

        # Gir feedback hvis det ikke finnes noen fullførte økter
        else:
            print("Det er ikke registrert noen fullførte økter.")

    # Gir feilmelding til bruker hvis det ikke finnes noen registrerte økter
    else:
        print("Det finnes ingen registrerte økter.")


def search_sessions(session_list):
    if session_list:
        search_sessions_list = [] # Liste for økter som matcher søkeord
        while True:
            # Etterspør søkeord, godtar ikke et tomt felt
            search_input = input("Søk etter tema i øktene dine: ").strip().lower()
            if search_input != "":
                break

        # Går gjennom alle sessions, og legger økter som matcher søkeord inn i egen liste
        for session in session_list:
            if search_input in session["topic"].lower():
                search_sessions_list.append(session)

        # Sjekker om den nye listen med matchende økter er tom, deretter printer ut øktene om listen inneholder økter
        if search_sessions_list:
            print(f"Økter med søkeordet '{search_input}':\n")
            for session in search_sessions_list:
                print(f"Tema: {session['topic']}\n"
                      f"Varighet: {session['duration']} minutter\n"
                      f"Status: {'Planlagt' if session['status'] == 'planned' else 'Fullført'}\n")

        else:
            print(f"Det finnes ingen temaer med søkeordet '{search_input}'.")

    # Printer feilmelding hvis det ikke finnes noen økter å matche søkeord mot
    else:
        print("Det finnes ingen registrerte økter.")


def exit_program(session_list):
    # Enkel mulighet til å lagre listen i en ekstern fil ved ønske
    print("\nAvslutter programmet. Ha en fin dag!")
    return False


menu = (
    {"title": "Registrer en studieøkt", "action": register_session},
    {"title": "Vis alle studieøkter", "action": view_sessions},
    {"title": "Vis bare fullførte studieøkter", "action": completed_sessions},
    {"title": "Søke etter et ord i temaet", "action": search_sessions},
    {"title": "Sorter øktene etter varighet, lengst først", "action": test},
    {"title": "Vis samlet og gjennomsnittlig varighet for fullførte økter", "action": test},
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