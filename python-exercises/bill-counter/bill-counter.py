value = int(input("Enter a value in Reais (R$): "))

quantity100 = 0
quantity50 = 0
quantity20 = 0
quantity10 = 0
quantity5 = 0
quantity1 = 0

while True :
    if value >= 100 :
        quantity100 += value // 100
        value -= quantity100 * 100
        print(f'Quantity of 100 bills: {quantity100}')
        if not value :
            break

    if value >= 50 :
        quantity50 += value // 50
        value -= quantity50 * 50
        print(f'Quantity of 50 bills: {quantity50}')
        if not value :
            break

    if value >= 20 :
        quantity20 += value // 20
        value -= quantity20 * 20
        print(f'Quantity of 20 bills: {quantity20}')
        if not value :
            break

    if value >= 10 :
        quantity10 += value // 10
        value -= quantity10 * 10
        print(f'Quantity of 10 bills: {quantity10}')
        if not value :
            break

    if value >= 5 :
        quantity5 += value // 5
        value -= quantity5 * 5
        print(f'Quantity of 5 bills: {quantity5}')
        if not value :
            break

    if value >= 1 :
        quantity1 += value // 1
        value -= quantity1 * 1
        print(f'Quantity of 1 bills: {quantity1}')
        break
