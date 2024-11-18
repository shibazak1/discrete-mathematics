
"""Does there exist a six-digit integer that starts with 100 and is a multiple of 9 127?"""

for n in range(10**7):
    if n-(n%1000)==100000 and n%127==0 and n%9==0:
        print(n)
    
