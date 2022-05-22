number = int(input("Provide number"))


result: dict = {}
for i in range(1, number + 1):
    result[i] = pow(i, 2)

print(result)
