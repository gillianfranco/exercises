preco = float(input('Enter the price of a product: '))
p = int(input('Enter a discount percentage (0-100%): '))

desconto = preco * (p / 100)

calculo = float(preco - desconto)

print('\nThe product with an initial price of %.2f and a discount of %d percent comes to %.2f' % (preco, p, calculo))