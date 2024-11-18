from extended_euclid_algo import extended_gcd
from gcd3 import gcd

def diophontine(a,b,c):
    assert c%gcd(a,b)==0

    (d,x,y) = extended_gcd(a,b)

    k = c//gcd(a,d)
    x = x*k
    y = y*k

    return (x,y)
