x, y = (input("First digit"), input("Second digit"))

rows = int(x)
cols = int(y)


result = [[]]
for i in range(0, rows):
    for j in range(0, cols):
        result[i][j] = i * j

print(results)
