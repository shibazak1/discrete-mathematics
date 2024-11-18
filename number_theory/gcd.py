
def gcd(a,b):

    assert a>=0 and  b>=0 and  a+b>0

    if a==0 or b==0:
        return min(a,b)

    for i in range(min(a,b),0,-1):
        print(i)
        if a%i==0 and b%i==0:
            return i

    return 1



print(gcd(12,2))
