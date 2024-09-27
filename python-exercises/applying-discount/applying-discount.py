price = float(input('Enter the price of the product: '))
percentage = float(input('Enter a discount percentage: '))

discount = price * (percentage / 100)

calculation = float(price - discount)

print('The initial price of the product is %.2f, with a discount of %.2f%%, the final price is %.2f.' % (price, percentage, calculation))