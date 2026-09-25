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
        return (f"{self.title}\n"
                f"{self.category}\n"
                f"{self.date}\n"
                f"{self.estimated_minutes}\n"
                f"{self.status}\n")


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