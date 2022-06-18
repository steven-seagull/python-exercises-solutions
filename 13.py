input_str = input()

result: dict = {"digits": 0, "letters": 0}

for i in input_str:
    if i.isdigit():
        result["digits"] += 1
    elif i.isalpha():
        result["letters"] += 1
    else:
        pass

print(f"DIGITS: {result.get('digits')}")
print(f"LETTERS: {result.get('letters')}")
