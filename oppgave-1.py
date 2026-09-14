from Components.ComponentsOne.StudyFunction import study
from Components.ComponentsOne.TextAnalyze import text_analyze
from Components.ComponentsOne.NumberRow import number_row

# Menu, Task 1.4
while True:
    print("\n"
          "1. Calculate study time\n"
          "2. Text Analytics\n"
          "3. Analyze number interval\n"
          "4. Exit\n")

    try:
        menu_choice = int(input("Enter your choice: "))

        if menu_choice == 1:
            study()
        elif menu_choice == 2:
            text_analyze()
        elif menu_choice == 3:
            number_row()
        elif menu_choice == 4:
            print("Goodbye! Thank you for using this program.")
            break
        else:
            print("Invalid choice. Please enter one of the options below.\n")

    except:
        print("Value entered is invalid.\n")