def test(activities):
    print(f"Test {activities}")


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