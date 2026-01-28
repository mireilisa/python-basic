#Ex.n1:

def dollars_calc():
    nis = float(input("enter amount of nis >>> "))
    rate = float(input("enter dollar rate >>> "))

    dollars = nis / rate
    print(f"total {dollars:.2f} dollars")

dollars_calc()

#Ex.n2:

def change_calc():
    price = float(input("enter total price >>> "))
    cash = float(input("enter cash >>> "))

    change = cash - price
    print(f"change {change:.2f} nis")

change_calc()

#Ex.n3:

def salary_calc():
    hours = float(input("enter work hours >>> "))
    wage = float(input("enter wage >>> "))
    tax = float(input("enter tax >>> "))

    gross = hours * wage
    tax_amount = gross * (tax / 100)
    net_salary = gross - tax_amount

    print(f"salary netto {net_salary:.2f} nis")

salary_calc()
