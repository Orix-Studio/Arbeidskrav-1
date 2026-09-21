# Task 1.1
def study():
    while True:
        # Lets the user enter two numbers until the values are valid.
        try:
            study_sessions = int(input("Enter the amount of study sessions: "))
            session_time = int(input("Enter the length of a session: "))
            if study_sessions <= 0 or session_time <= 0:
                print("You cannot enter zero or negative numbers.\n")
            else:
                total_study_time = session_time * study_sessions

                # Calculating hours and minutes
                total_study_hours = int(total_study_time / 60)
                total_study_minutes = total_study_time % 60

                # Final Output
                print(f"Total study time is {total_study_hours} hours and {total_study_minutes} minutes.")

                break
        except:
            print("Please enter whole numbers for both inputs.\n")