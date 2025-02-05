''' this extension of GCD function that in addition of returning the GCD d
    return the x , y integer that form d = ax+ by
'''


def extended_gcd(a,b):

    assert a>=b and b>=0 and a+b>0

    if b==0:
        d , x y = a,1,0
    else:
        (d,p,q) = extended_gcd(b,a%b)
        x =q
        y = p-q(a/b)

    assert a%d==0 and b%d==0
    assert d =a*x +b*y
    return (d,x,y)
