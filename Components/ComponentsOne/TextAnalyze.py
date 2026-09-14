# Task 1.2
def text_analyze():
    while True:
        text_analyze_value = input("Enter the text you want to analyze: ").strip()
        if text_analyze_value:

            # Amount of characters with and without spaces
            all_char = len(text_analyze_value)
            all_char_no_space = len(text_analyze_value.replace(" ", ""))

            # Text transformed to lowercase
            lower_char = text_analyze_value.lower()

            # Text backwards
            backwards = text_analyze_value[::-1]

            # Detect "python" in the text
            contains_python = "python" in text_analyze_value.lower()  # Could have also used the lowercase value above.

            # Final analyze output
            print(f"Character count incl. spaces: {all_char}\n"
                  f"Character count excl. spaces: {all_char_no_space}\n\n"
                  f"Text in lowercase: \n{lower_char}\n\n"
                  f"Text backwards: \n{backwards}\n\n"
                  f"Contains 'Python': {'Yes' if contains_python else 'No'}")

            break
        else:
            print("You cannot submit an empty text field.\n")