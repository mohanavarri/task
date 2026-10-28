'''# University Scholarship Allocation

name = input("Enter student name: ")
marks = float(input("Enter aggregate marks: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter family income: "))

if marks >= 75 and attendance >= 75 and income <= 200000:
    print("Student Name:", name)
    print("Scholarship Status: Eligible")
else:
    print("Student Name:", name)
    print("Scholarship Status: Not Eligible")
# Progressive Electricity Billing

units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = 100 * 2 + (units - 100) * 3
else:
    bill = 100 * 2 + 100 * 3 + (units - 200) * 5

bill = bill + 50  # Fixed charge

print("Units Consumed:", units)
print("Total Electricity Bill: Rs.", bill)
# Student Marks Analysis

marks = []

for i in range(1, 4):
    mark = int(input("Enter marks for subject " + str(i) + ": "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

print("Subject Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)

if all(mark >= 35 for mark in marks):
    print("Result: PASS")
else:
    print("Result: FAIL")
# Shopping Bill Calculator

price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

if total >= 1000:
    discount = total * 0.10
else:
    discount = 0

final_bill = total - discount

print("Total Amount:", total)
print("Discount:", discount)
print("Final Bill:", final_bill)
# ATM Simulation

balance = 5000

print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")

choice = int(input("Enter your choice: "))

if choice == 1:
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount
    print("Updated Balance:", balance)

elif choice == 2:
    amount = int(input("Enter withdrawal amount: "))
    if amount <= balance and amount > 0:
        balance = balance - amount
        print("Updated Balance:", balance)
    else:
        print("Insufficient balance or invalid amount")

elif choice == 3:
    print("Current Balance:", balance)

else:
    print("Invalid choice")
# Attendance Checker

total_classes = int(input("Enter total classes: "))
attended = int(input("Enter classes attended: "))

if total_classes > 0 and 0 <= attended <= total_classes:
    attendance = attended / total_classes * 100

    print("Attendance:", attendance, "%")

    if attendance >= 75:
        print("Eligible for examination")
    else:
        print("Not eligible for examination")
else:
    print("Invalid class details")
# Fuel Cost Calculator

distance = float(input("Enter distance in km: "))
mileage = float(input("Enter vehicle mileage (km/l): "))
price = float(input("Enter fuel price per litre: "))

if distance >= 0 and mileage > 0 and price >= 0:
    fuel = distance / mileage
    cost = fuel * price

    print("Fuel Required:", round(fuel, 2), "litres")
    print("Total Fuel Cost: Rs.", round(cost, 2))
else:
    print("Enter valid values")
# Student Grade Calculator

marks = int(input("Enter marks out of 100: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")
# Library Fine Calculator

days = int(input("Enter late days: "))

if days <= 0:
    fine = 0
elif days <= 5:
    fine = days * 2
else:
    fine = 10 + (days - 5) * 5

print("Library Fine: Rs.", fine)'''
# Food Waste Calculator

prepared = int(input("Enter meals prepared: "))
served = int(input("Enter meals served: "))

if prepared > 0 and 0 <= served <= prepared:
    wasted = prepared - served
    percentage = wasted / prepared * 100

    print("Meals Wasted:", wasted)
    print("Waste Percentage:", round(percentage, 2), "%")
else:
    print("Enter valid values")


