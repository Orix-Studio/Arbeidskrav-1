from datetime import datetime
from Components.ComponentsThree.ConvertDateTime import convert_date, convert_time, convert_minutes, convert_datetime_output, sort_print_class

class_list = []

while True:
    print("\n"
          "1. Plan a study session\n"
          "2. View planned sessions\n"
          "3. Calculate days between dates\n"
          "4. Exit\n")

    try:
        menu_choice = int(input("Enter your choice: "))

        if menu_choice == 1:
            print("\nPlan your study session")
            study_start = datetime.combine(convert_date(), convert_time())

            study_length = convert_minutes()
            study_length_split = str(study_length).split(":")
            study_hours, study_minutes = study_length_split[0], study_length_split[1]

            study_end = study_start + study_length


            print(f"\nThe class starts {convert_datetime_output(study_start)}.\n"
                  f"The class ends {convert_datetime_output(study_end)}.\n"
                  f"The class lasts {study_hours} hours and {study_minutes} minutes.\n")


            # Storage format
            new_class_details = {
                "start": str(study_start),
                "hours": int(study_hours),
                "minutes": int(study_minutes),
                "end": str(study_end),
            }

            # Store class in object
            class_list.append(new_class_details)


        elif menu_choice == 2:
            if class_list == {}:
                print("\nYou have not planned any sessions.")
            else:
                print("Your planned sessions sorted by date:\n")
                sort_print_class(class_list)


        elif menu_choice == 3:
            first_date = convert_date()
            second_date = convert_date()

            print(f"There is {abs(first_date - second_date).days} days between the two dates.")

        elif menu_choice == 4:
            print("Goodbye! Thank you for using this program.")
            break
        else:
            print("Invalid choice. Please enter one of the options below.\n")

    except ValueError:
        print("Value entered is invalid.\n")
