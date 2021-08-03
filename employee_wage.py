import random

print("\tWelcome to Employee Wage Computation ")
ATTENDANCE = random.randint(0, 1)
DAY_HOURS = 8
WAGE_PER_HOUR = 20
PART_TIME_HOURS = 4
DAILY_WAGE = 20 * 8
PART_TIME_WAGE = 20 * 4

if ATTENDANCE == 1:
    print("Employee is Present...........!")
    print("Full Time employee Total day wage is : ", DAILY_WAGE)
    print("Part Time employee Total day wage is : ", PART_TIME_WAGE)

else:
    print("Employee is Absent.............!")
