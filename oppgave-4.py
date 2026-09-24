# Task 4.1

valid_tickets = []
invalid_tickets = []

print("Validation checking all support tickets:\n")

with open("supporthenvendelser.csv", "r", encoding="utf-8") as file:
    for i, line in enumerate(file, start=1):
        if i > 1:
            split = line.strip().split(",")
            support_id = split[0]
            support_category = split[1]
            support_minutes_raw = split[2]
            support_status = split[3].lower()

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
            if support_status == "yes":
                print("✅ Resolved")
            elif support_status == "no":
                print("✅ Unresolved")
            else:
                print("❌ Invalid status")
                validation = False

            # Sort Valid/Invalid
            if validation:
                valid_tickets.append([support_id_int, support_category, support_minutes, support_status])
            else:
                invalid_tickets.append(split)

            print()


print("*" * 30 + "\n") # Spacer


# Task 4.2
print("Support Ticket Analysis:\n")


# Valid/Invalid ticket count
valid_count, invalid_count = len(valid_tickets), len(invalid_tickets)

print(f"Valid tickets: {valid_count}\n"
      f"Invalid tickets: {invalid_count}\n")


# Total/Average duration
total_minutes = 0

for ticket in valid_tickets:
    ticket_minutes = int(ticket[2])
    total_minutes += ticket_minutes

average_minutes = total_minutes / valid_count

print(f"Total minutes: {total_minutes}\n"
      f"Average minutes: {average_minutes:.1f}\n")


# Total resolved/unresolved tickets
resolved_count = 0
unresolved_count = 0

for ticket in valid_tickets:
    if ticket[3] == "yes":
        resolved_count += 1
    elif ticket[3] == "no":
        unresolved_count += 1

print(f"Resolved tickets: {resolved_count}\n"
      f"Unresolved tickets: {unresolved_count}\n")


# Sorted Category Count
category_count = {}

for ticket in valid_tickets:
    if ticket[1]:
        if ticket[1] in category_count:
            category_count[ticket[1]] += 1
        else:
            category_count[ticket[1]] = 1
    else:
        if "Uncategorized" in category_count:
            category_count["Uncategorized"] += 1
        else:
            category_count["Uncategorized"] = 1

sorted_category_list = sorted(category_count.items(), key=lambda item: item[1], reverse=True)

print("Ticket category count (high-low):")
for category, count in sorted_category_list:
    print(f"{category.capitalize()}: {count}")

print()


# Sorted Unresolved ticket duration
unresolved_tickets = []

for ticket in valid_tickets:
    if ticket[3] == "no":
        unresolved_tickets.append(ticket)

sorted_unresolved_tickets = sorted(unresolved_tickets, key=lambda item: item[2], reverse=True)

print("Unresolved tickets sorted by duration (high-low):\n")
for unresolved_ticket in sorted_unresolved_tickets:
    print(f"Unresolved ticket #{unresolved_ticket[0]}\n"
          f"Duration: {unresolved_ticket[2]} minutes\n")