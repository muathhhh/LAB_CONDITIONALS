
age = int(input("Enter your age:"))
d = input("Enter the day:")

day = ["Saturday", "Sunday", "Monday", "Tuesday",
       "Wednesday", "Thursday", "Friday"]

pay = 0

if age < 0:
    print("Invalid age")

elif d not in day:
    print("Invalid day")

else:
    if age < 5:
        pay = 0
    elif age <= 12:
        pay = 6
    elif age <= 59:
        pay = 10
    else:
        pay = 7

    if d == "Friday" and age >= 5:
        pay += 2

    stu = input("Are you Student?")

    if stu == "yes" and age >= 5: #to apply discount of Student
        pay = pay * 0.8

    print("Ticket Price: $", pay)