from math import gcd

p,q = 5,11
n  = p*q


def encode(m):
    phi = (p-1)*(q-1)
    for i in range(1,phi):
        if gcd(i,phi)==1:
            e = i

        break
    return pow(m,e,n)

def decode(c):

    d = pow(e,-1,phi)
    assert d*e % phi ==1


    return pow(c,d,n)



m = 1234567
print(f"message : {m}")

c = encode(m)
print(f"cipher : {c}")

m2 = decode(c)
print(f"message : {m2}")



        
