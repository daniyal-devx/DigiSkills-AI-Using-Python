salary = float(input("Enter your salary: "))

if salary < 30000:
    tax_rate = 0.05
    tax = salary * tax_rate
    print(f"Salary: {salary}")
    print(f"Tax Rate: 5%")
    print(f"Tax Amount: {tax}")
elif 30000 <= salary <= 70000:
    tax_rate = 0.15
    tax = salary * tax_rate
    print(f"Salary: {salary}")
    print(f"Tax Rate: 15%")
    print(f"Tax Amount: {tax}")
else:
    tax_rate = 0.25
    tax = salary * tax_rate
    print(f"Salary: {salary}")
    print(f"Tax Rate: 25%")
    print(f"Tax Amount: {tax}")
