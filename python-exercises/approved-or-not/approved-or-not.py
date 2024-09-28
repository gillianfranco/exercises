subject1 = float(input('Enter the grade of the first subject: '))
subject2 = float(input('Enter the grade of the second subject: '))
subject3 = float(input('Enter the grade of the third subject: '))

min_for_approval = 7

average = (subject1 + subject2 + subject3) / 3

if subject1 >= min_for_approval and subject2 >= min_for_approval and subject3 >= min_for_approval:
    print('You got the approval! Your average was %.2f.' % average)
else:
    print("You don't got the approval. Your average was %.2f." % average)
