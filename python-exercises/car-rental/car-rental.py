km_driven = float(input('Enter the number of kilometers driven: '))
days_rented = int(input('Enter the number of days rented: '))

price_per_day = 60
price_per_km = 0.15

total = (km_driven * price_per_km) + (days_rented * price_per_day)
res = f'You have to pay R${total}'

print(res)