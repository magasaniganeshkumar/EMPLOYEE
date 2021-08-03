import random

print("\tWelcome to Employee Wage Computation ")
ATTENDANCE = random.randint(0, 1)
DAY_HOURS = 8
WAGE_PER_HOUR = 20
PART_TIME_HOURS = 4
WORK_DAYS = 20
DAILY_WAGE = 20 * 8
PART_TIME_WAGE = 20 * 4
MONTHLY_FULL_WAGE = 20 * 20 * 8
MONTHLY_PART_TIME_WAGE = 20 * 20 * 4

if ATTENDANCE == 1:
    emp_type = random.randint(0, 1)
    break_hour = 0
    break_day = 0
    month_wage = 0
    if emp_type == 1:
        for day in range(20):
            if break_day == 20 or break_hour >= 100:
                print(" max hours or max day are reached ")
                print("Full Time employee Total month wage when max hours or max day are reached : ", month_wage - 80)
                break
            break_hour += 8
            break_day += 1
            month_wage += DAILY_WAGE
        print("full time Employee is Present...........!")
        print("Full Time employee Total day wage is : ", DAILY_WAGE)
        print("Full Time employee Total month wage is : ", MONTHLY_FULL_WAGE)

    else:
        month_wage = 0
        for day in range(20):
            if break_day == 20 or break_hour >= 100:
                print(" max hours or max day are reached ")
                print("Part Time employee Total month wage when max hours or max day are reached : ", month_wage)
                break
            break_hour += 4
            break_day += 1
            month_wage += DAILY_WAGE
        print("part time Employee is Present...........!")
        print("Part Time employee Total day wage is : ", PART_TIME_WAGE)
        print("Part Time employee Total month wage is : ", MONTHLY_PART_TIME_WAGE)


else:
    print("Employee is Absent.............!")
