# Converts date input into date value
def convert_date():
    import datetime
    while True:
        date_input = input("Enter a date (dd.mm.yyyy): ").strip()
        date_split = date_input.split(".")

        if len(date_split) == 3:
            try:
                new_date = datetime.date(int(date_split[2]), int(date_split[1]), int(date_split[0]))
                return new_date
            except ValueError:
                print("Date is not valid. Try again.\n")
        else:
            print("Date format is submitted wrong. Try again.\n")


# Converts time input into time value
def convert_time():
    import datetime
    while True:
        time_input = input("Enter the starting time (hh:mm): ").strip()
        time_split = time_input.split(":")

        if len(time_split) == 2:
            try:
                new_time = datetime.time(int(time_split[0]), int(time_split[1]))
                return new_time
            except ValueError:
                print("Time is not valid. Try again.\n")
        else:
            print("Time format is submitted wrong. Try again.\n")


# Converts minutes into time format
def convert_minutes():
    from datetime import timedelta
    while True:
        try:
            length_input = int(input("Enter the length of the session (m): ").strip())

            if length_input > 0:
                total_hours = length_input // 60
                total_minutes = length_input % 60

                return timedelta(hours=total_hours, minutes=total_minutes)
        except ValueError:
            print("Time is not valid. Try again.\n")


# Converts datetime value to user-friendly output
def convert_datetime_output(current_date):
    try:
        return current_date.strftime("%A, %d. %B %Y at %H:%M")
    except:
        return "(Invalid date/time)"


# Sort and print class list
def sort_print_class(class_list):
    sorted_class_list = sorted(class_list, key=lambda item: item['start'])
    class_number = 0
    for class_item in sorted_class_list:
        class_number += 1
        print(f"{class_number}. class:\n"
            f"Start: {class_item['start']}\n"
            f"End: {class_item['end']}\n"
            f"Duration: {class_item['hours']} hours and {class_item['minutes']} minutes\n")