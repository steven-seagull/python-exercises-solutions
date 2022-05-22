def compute_factorial(number: int) -> int:
    if number == 0:
        return 1
    return number * (compute_factorial(number-1)) # tail recursive approach

fac = input("Provide a number to compute x!")

factorial = compute_factorial(int(fac))

print(f"Computed factorial for {fac}! = {factorial}")
