def option_validation(question, minimum, maximum):
    option = int(input(question))
    while (option < minimum) or (option > maximum):
        option = int(input('Invalid option! Try again: '))
    return option

store = {
    'carrot': [0.99, 50],
    'tomato': [0.49, 100],
    'potato': [0.49, 200],
    'onion': [1.10, 75]
}

while True:
    print('Menu')
    print('1-Register', end=' | ')
    print('2-Buy', end=' | ')
    print('3-Close the program\n')

    choose = option_validation('Enter your choose here: ', 1, 3)

    if choose == 1:
        print('\nRegister option was selected.\n')

        for key, value in store.items():
            print(f'{key} = Price: {value[0]}; Quantity: {value[1]}')
        print()

        product = input('Enter the name of the product: ')
        quantity = int(input('Enter the quantity of this product that you want register: '))

        store[product][1] += quantity

        print(f'\nProduct registered: {product}')
        print(f'Quantity: {quantity}')
        print(f'Total in cash: R${quantity * store[product][0]}\n')

    elif choose == 2:
        print('\nBuy option was selected.\n')

        orders = []
        while True:
            for key, value in store.items():
                print(f'{key} = Price: {value[0]}; Quantity: {value[1]}')
            print()

            product = input('Enter the name of the product: ')
            quantity = int(input('Enter the quantity of this product that you want buy: '))

            orders.append([product, quantity])

            purchase = input('Do you want continue the purchase? [S/N] ')
            if purchase in 'Nn':
                break
        print()

        total = 0
        for item in orders:
            product = item[0]
            quantity = item[1]
            price = store[product][0]
            total_product = quantity * price

            print(f'{product}: {quantity} * {price} = R${total_product}')

            store[product][1] -= quantity
            total += total_product

        print(f'Total to pay: R${total}')

        print('\nStock: ')
        for key, value in store.items():
            print(f'{key} = Price: {value[0]}; Quantity: {value[1]}')
        print()

    else:
        print('Closing the program.')
        break
