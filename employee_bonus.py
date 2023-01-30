import csv

infile = open("EmployeePay.csv", "r")

employee = csv.reader(infile, delimiter=",")
next(employee)

print(
    "First Name"
    + ", "
    + "Last Name"
    + ", "
    + "ID"
    + ", "
    + "Salary"
    + ", "
    + "Bonus"
    + "\n"
)
# print("____________________________________________________" + "\n")

for x in employee:
    employee_id = x[0]
    first_name = x[1]
    last_name = x[2]
    salary = x[3]
    bonus = x[4]
    print(
        first_name
        + ", "
        + last_name
        + ", "
        + employee_id
        + ", "
        + salary
        + ","
        + bonus
        + "\n"
    )
