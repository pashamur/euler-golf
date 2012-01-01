sum = 0
prods = []
for i in range(1,50):
    for j in range(1,2000):
        prod = i*j
        string = str(i) + str(j) + str(prod)
        if ''.join(sorted(string)) == '123456789':
            print i, j, prod
            if prod not in prods:
                prods.append(prod)
                sum += prod
print sum
