#6.Dictionary

# 1. Create a list of friends' names and generate tuples with their names and the length of their names
def friends_names():
    friends = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    name_length_tuples = [(name, len(name)) for name in friends]
    print(f"Friends and their name lengths: {name_length_tuples}")

# 2. Create two dictionaries for trip expenses and compare spending
def trip_expenses():
    # Your expenses
    your_expenses = {
        "Hotel": 1200,
        "Food": 800,
        "Transportation": 500,
        "Attractions": 300,
        "Miscellaneous": 200
    }
    # Partner's expenses
    partner_expenses = {
        "Hotel": 1000,
        "Food": 900,
        "Transportation": 600,
        "Attractions": 400,
        "Miscellaneous": 150
    }
    # Calculate total expenses
    your_total = sum(your_expenses.values())
    partner_total = sum(partner_expenses.values())
    print(f"Your total expenses: ${your_total}")
    print(f"Partner's total expenses: ${partner_total}")
    # Compare total spending
    if your_total > partner_total:
        print("You spent more overall.")
    elif your_total < partner_total:
        print("Your partner spent more overall.")
    else:
        print("You and your partner spent the same amount.")
    # Find the category with the most significant difference
    max_diff_category = None
    max_diff_amount = 0
    for category in your_expenses:
        diff = abs(your_expenses[category] - partner_expenses[category])
        if diff > max_diff_amount:
            max_diff_amount = diff
            max_diff_category = category
    print(f"Category with the most significant difference: {max_diff_category} (Difference: ${max_diff_amount})")
# Run the functions
print("Task 1: Friends' Names and Lengths")
friends_names()
print("\nTask 2: Trip Expenses Comparison")
trip_expenses()
