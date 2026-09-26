from itertools import product

W, N = 12, 4
for order in product(range(W), repeat=N):
    print(order)
    for c in order:
        print('   c =', c)