C = 50
H = 30

import math

def compute(x):
    intermediate = (2 * C * x) / H
    return int(math.sqrt(intermediate))
   

for i in input("").split(','):
    print(compute(int(i)))


