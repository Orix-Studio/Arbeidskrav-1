# Task 4.1

valid_tickets = []
invalid_tickets = []

with open("supporthenvendelser.csv", "r", encoding="utf-8") as file:
    for i, line in enumerate(file, start=1):
        if i > 1:
            split = line.strip().split(",")
            support_id = split[0]
            support_category = split[1]
            support_minutes_raw = split[2]
            support_status = split[3]

            # Validation
            validation = True

            print(f"Row {i}")

            # ID Validation
            try:
                support_id_int = int(support_id)
                if support_id_int > 0:
                    print(f"✅ Request #{support_id_int}")
                else:
                    print("❌ Negative id")
                    validation = False
            except ValueError:
                print("❌ ID is not valid.")
                validation = False

            # Category Validation
            if support_category:
                print(f"✅ #{support_category}")
            else:
                print("✅ No category") # It is not invalid just because of empty category

            # Duration Validation
            try:
                support_minutes = int(support_minutes_raw)
                if support_minutes >= 0:
                    print(f"✅ {support_minutes} minutes")
                else:
                    print("❌ Negative duration.")
                    validation = False
            except ValueError:
                print("❌ Invalid duration")
                validation = False

            # Status Validation
            if support_status.lower() == "yes":
                print("✅ Resolved")
            elif support_status.lower() == "no":
                print("✅ Unresolved")
            else:
                print("❌ Invalid status")
                validation = False

            # Sort Valid/Invalid
            if validation:
                valid_tickets.append(line.strip())
            else:
                invalid_tickets.append(line.strip())

            print()