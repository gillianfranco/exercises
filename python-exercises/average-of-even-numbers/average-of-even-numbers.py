sum_evens = 0
quantity = 0

for i in range(1, 101) :
    if i % 2 == 0 :
        sum_evens += i
        quantity += 1

average = sum_evens / quantity

print('Total: %d' % sum_evens)
print('Amount: %d' % quantity)
print('Average: %.2f' % average)
