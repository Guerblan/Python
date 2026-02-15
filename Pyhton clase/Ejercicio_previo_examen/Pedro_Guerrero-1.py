num = [1, 2, 2, 3, 4, 4, 5, 6]
num.insert(1, 7)
print(num)

unicos = set(num)
print(unicos)

pares = [x for x in unicos if x % 2 == 0]
print(pares)
