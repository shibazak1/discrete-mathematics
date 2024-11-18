# find number a b c sutch that a^2 + b^2 = c^2

from itertools import combinations


for a, b ,c in combinations(range(1,20),3):
    if a**2 + b**2 == c**2:
        print(f"{a}**2 + {b}**2 = {c}**2")

        
    
