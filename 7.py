x, y = (input("First digit"), input("Second digit"))

rows = int(x)
cols = int(y)


result = []

for i in range(0, rows):
    row = []
    for j in range(0, cols):
        row.append(i * j)
    result.append(row)

print(result)

