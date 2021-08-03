import random

print("\tWelcome to Employee Wage Computation ")
ATTENDANCE = random.randint(0, 1)
DAY_HOURS = 8
WAGE_PER_HOUR = 20
DAILY_WAGE = 20 * 8

if ATTENDANCE == 1:
    print("Employee is Present...........!")
    print("Full Time employee Total day wage is : ", DAILY_WAGE)

else:
    print("Employee is Absent.............!")
