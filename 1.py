result = []

for i in range(2000, 3201):
    if not i %7 and i%5:
        result.append(str(i))

print(','.join(result))
