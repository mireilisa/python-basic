def get_income():
    income = float(input("Enter your monthly income: "))
    return income

def get_expenses(category):
    amount =float(input(f"Enter your monthly expenses for {category}:"))
    return amount

def collect_expenses(categories):
    expenses = []
    for category in categories:
        amount = get_expenses(category)
        expenses.append((category, amount))
    return expenses

def calculate_total(expenses):
    total = sum(amount for category, amount in expenses)
    return total

def main():
    income = get_income()

    categories = ["Rent", "Food", "Transport", "Internet"]
    categories.append("Pets")

    expenses = collect_expenses(categories)
    
    total = calculate_total(expenses)
    balance = income - total

    print_report(income, expenses, total, balance)

def print_report(income, expenses, total, balance):
    print("\n--- Monthly Budget Report ---")
    print(f"Total Income: {income:.2f}")
    
    print("Expenses:")
    for category, amount in expenses:
        print(f"- {category}: {amount:.2f}")

    print(f"\nTotal Expenses: {total:.2f}")
    print(f"Balance: {balance:.2f}")

    if balance < 0:
        print("\033[91m❌ WARNING: You are over budget!\033[0m")
    
    elif balance < 500: 
        print("\033[93m⚠️ Attention: Budget is tight!\033[0m")

    else:
        print("\033[92m✅ Budget under control!\033[0m")

if __name__ == "__main__":
    main()