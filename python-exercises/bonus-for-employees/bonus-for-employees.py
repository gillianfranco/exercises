year_of_entry = int(input('Which year did you join the company? '))
salary = float(input("What's your salary? "))
actual_year = 2024

years = actual_year - year_of_entry

if years >= 10 :
    bonus = (30 / 100) * salary
else:
    if years >= 5 :
        bonus = (20 / 100) * salary
    else:
        bonus = (10 / 100) * salary

print('Your salary is %.2f. Your bonus is of %d percent. And your final salary is %.2f' % (salary, bonus, salary + bonus))
