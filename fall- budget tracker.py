"""
Problem Description:
This program is a personal budget tracker that allows a user to record, monitor, and control their spending based on a predefined budget. At the start, the user inputs a budget amount representing the maximum they intend to spend within a given time period.

The user interacts with the program through a menu-based interface, where they can choose to record an expense, view a financial summary, or exit the program. When recording an expense, the user selects a category from a predefined list and inputs the amount spent. The program then updates the corresponding category total using a dictionary data structure, where each key represents a category and each value represents the total amount spent.

The program operates within a loop, allowing the user to continue interacting with it until they choose to exit. At any time, the user can request a summary of their financial data. The program calculates and displays the total expenses (both overall and per category), as well as the remaining balance, which is the difference between the budget and total spending.

Based on the remaining balance, the program provides feedback. If the user is within their budget, it displays the remaining amount. If they are close to exceeding their budget, it issues a warning. If the budget has been exceeded, it indicates the amount by which the user is over budget.

Upon exiting, the program writes a summary report to an output file named summary.txt. This report includes all expense categories, total spending, and the remaining or exceeded budget, ensuring the user’s financial data is preserved beyond the execution of the program.

This program demonstrates the use of variables, arithmetic operations, conditional statements, loops, and sequence types.
"""

import math  # namespace import

# Function to calculate remaining budget
def calculate_remaining(budget, expenses):
    total = math.fsum(expenses.values())
    return budget - total

# Function to calculate percentage of budget used
def calculate_percentage_used(budget, total):
    if budget == 0:
        return 0
    return (total / budget) * 100

# Get user budget input
budget = float(input("Enter the budget for the month: "))

# Dictionary to store expenses
expenses = {
    'Food': 0,
    'Entertainment': 0,
    'Transportation': 0,
    'Rent': 0,
    'Personal': 0
}

# List of categories (explicit sequence requirement)
categories_list = list(expenses.keys())

running = True

while running:
    print("\n1. Add Expense")
    print("2. View Summary")
    print("3. Exit")

    choice = input("Please choose an option: ")

    if choice == "1":
        print("\nCategories:")
        for item in categories_list:
            print("-", item)

        category = input("Enter a category: ").title()

        if category in categories_list:
            try:
                amount = float(input("Enter amount spent: "))
                expenses[category] += amount
                print(f"${amount} added to {category}")
            except ValueError:
                print("Invalid number entered.")
        else:
            print("Invalid category")

    elif choice == "2":
        total_expenses = 0

        print("\nExpense Breakdown:")
        for category, amount in expenses.items():
            print(f"{category}: ${amount:.2f}")
            total_expenses += amount

        remaining = calculate_remaining(budget, expenses)
        percent_used = calculate_percentage_used(budget, total_expenses)

        print(f"\nTotal expenses: ${total_expenses:.2f}")
        print(f"Budget: ${budget:.2f}")
        print(f"Percentage of budget used: {percent_used:.2f}%")

        if remaining < 0:
            print(f":c You exceeded your budget by ${abs(remaining):.2f}")
        elif remaining <= 100:
            print(f"Warning: You are close to your budget. ${remaining:.2f} left")
        else:
            print(f"You are within your budget. ${remaining:.2f} left")

    elif choice == "3":
        total_expenses = sum(expenses.values())
        remaining = calculate_remaining(budget, expenses)
        percent_used = calculate_percentage_used(budget, total_expenses)

        with open("summary.txt", "w") as file:
            file.write("Expense Summary\n")
            file.write("-----------------\n")

            for category in categories_list:
                file.write(f"{category}: ${expenses[category]:.2f}\n")

            file.write(f"\nTotal expenses: ${total_expenses:.2f}\n")
            file.write(f"Budget: ${budget:.2f}\n")
            file.write(f"Percentage used: {percent_used:.2f}%\n")

            if remaining < 0:
                file.write(f"Over budget by ${abs(remaining):.2f}\n")
            elif remaining <= 100:
                file.write(f"Close to budget. ${remaining:.2f} remaining\n")
            else:
                file.write(f"Within budget. ${remaining:.2f} remaining\n")

        print("Summary saved to summary.txt")
        running = False

    else:
        print("Invalid option")