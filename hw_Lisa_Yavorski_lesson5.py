#Ex.n-1:



def haim():
    apples = float(input("Haim, enter amount of apples (by kg): "))
    return apples

def nastya():
    apples = float(input("Nastya, enter amount of apples (by kg): "))
    return apples


def alex():
    apples = float(input("Alex, enter amount of apples (by kg): "))
    return apples


def anna():
    apples = float(input("Anna, enter amount of apples (by kg): "))
    return apples

h = haim()
n = nastya()
a = alex()
an = anna()

total_apples = h + n + a + an
average = total_apples / 4

print(f"Total apples in family: {total_apples} kg")
print(f"Average apples per person: {average} kg")

#This program calculates the total and average amount of apples of four family member.




#Ex.n-2:




def salary_calc():
    hours = float(input("Enter work hours >>> "))
    wage = float(input("Enter wage >>> "))
    tax = float(input("Enter tax >>> "))

    gross = hours * wage
    tax_amount = gross * (tax / 100)
    net_salary = gross - tax_amount

    return net_salary

nastya_salary = salary_calc()
alex_salary = salary_calc()

print(f"Nastya's net salary: {nastya_salary:.2f} nis")
print(f"Alex's net salary: {alex_salary:.2f} nis")

print("Calculation finished successfully")



#Ex.n-3:




def salaryAdv():
    hours = float(input("Enter work hours >>> "))
    wage = float(input("Enter wage >>> "))
    tax = float(input("Enter tax >>> "))
    bonus = float(input("Enter bonus >>> "))

    gross = hours * wage
    tax_amount = gross * (tax / 100)
    net_after_tax = gross - tax_amount
    bonus_amount = net_after_tax * (bonus / 100)
    final_salary = net_after_tax + bonus_amount

    return final_salary

nastya_final_salary = salaryAdv()
alex_final_salary = salaryAdv()

print(f"Nastya's net salary with bonus: {nastya_final_salary:.2f} nis")
print(f"Alex's net salary with bonus: {alex_final_salary:.2f} nis")
