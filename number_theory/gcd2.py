

def gcd(a,b):

    assert a>=0 and b>=0 and a+b>0

    while a>0 and b>0:

        if a>b:
            a = a-b
        else:
            b = b-a

    return max(a,b)



print(gcd(10,2))
