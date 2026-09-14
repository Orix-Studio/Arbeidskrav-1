# Task 1.3
def number_row():
    while True:
        try:
            start_number = int(input("Enter the starting number: "))
            end_number = int(input("Enter the ending number: "))
            if start_number == end_number:
                print("You have to enter two different numbers.\n")
            elif start_number > end_number:
                print("The starting number cannot be higher than the ending number.\n")
            else:

                print("Even numbers between start and end:")
                for i in range(start_number, end_number + 1):
                    if i % 2 == 0:
                        print(i)

                print("")

                print("All numbers that can be divided by 3:")
                for i in range(start_number, end_number + 1):
                    if i % 3 == 0:
                        print(i)

                print("")

                print("Every number in the line summed up:")
                all_numbers = []
                for i in range(start_number, end_number + 1):
                    all_numbers.append(i)

                print(sum(all_numbers))

                break
        except:
            print("Please enter whole numbers for both inputs.\n")