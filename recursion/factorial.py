
def factorail(n):
    if n>=1:
        result = 1
        for i in range(1,n+1):
            result *=i
        return result

def factorail2(n):
    
    if n==0:
        print(f"the n value is {n} ")
        return 1
    else:
        print(f"computing the factorial of {n}")
        shorter_fact = n*factorail2(n-1)
        print(f" the factorail of {n} is {shorter_fact}")
        return shorter_fact


