from gcd3 import gcd

def lcm(a,b):
    assert a>0 and b>0 and a+b>0

    return (a*b)//gcd(a,b)


