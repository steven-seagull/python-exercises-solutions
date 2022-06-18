from typing import List

def determine_if_all_digits_are_even(number: int) -> bool:
    for digit in str(number):
        if int(digit) % 2 != 0:
            return False
    return True


result: List[str] = []
for i in range(1000, 3001):
    if determine_if_all_digits_are_even(i):
        result.append(str(i))

print(",".join(result))
