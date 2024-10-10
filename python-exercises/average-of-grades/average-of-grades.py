grades = [] #or grades = list()
grade = 0
sum_grades = 0

while grade >= 0 :
    grade = float(input('Enter a grade (Enter a negative value to leave): '))
    if grade >= 0 :
        grades.append(grade) 

for i in grades :
    sum_grades += i

average_grades = sum_grades / len(grades)

print('\n', grades)
print('Average: %.2f' % average_grades)
