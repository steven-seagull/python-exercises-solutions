lines = []

while True:
    string = input()
    if string:
        lines.append(string)
    else:
        break

[print(x.upper()) for x in lines]
    
