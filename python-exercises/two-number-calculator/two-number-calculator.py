print('CALCULATOR:\n')
print('(*) Multiplication')
print('(/) Division')
print('(+) Addition')
print('(-) Subtraction')

operation = input('Enter the symbol corresponding to the desired mathematical operation: ')

number_1 = float(input('Enter the first number: '))
number_2 = float(input('Enter the second number: '))

if operation == '*':
    print('The multiplication of %.2f and %.2f is %.2f.' % (number_1, number_2, number_1 * number_2))
elif operation == '/':
    print('The division of %.2f and %.2f is %.2f.' % (number_1, number_2, number_1 / number_2))
elif operation == '+':
    print('The addition of %.2f and %.2f is %.2f.' % (number_1, number_2, number_1 + number_2))
elif operation == '-':
    print('The subtraction of %.2f and %.2f is %.2f.' % (number_1, number_2, number_1 - number_2))
else:
    print('The operation you chose is invalid.')
