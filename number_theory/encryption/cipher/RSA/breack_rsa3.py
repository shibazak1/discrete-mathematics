# attack on RSA when the difference between p and q are small

# written by ViiBug

#2024/7/21


#-----------------------------------------------------------------------------------------------------------------#
#                                             RSA Attack 3                                                        #
#-----------------------------------------------------------------------------------------------------------------#






import math

def FromTextToNum(txt):
    result = 0
    for symbol in txt:
        result = result*100+ ord(symbol)
    print(f" message :{result}")
    return result


def Encrypt(m,n,e):
    m = FromTextToNum(m)
    #print(f"ciphertext {m}")
    return pow(m,e,n)


def Decrypt(ciphertext,small_prime,big_prime,exponent):
    phi = (small_prime-1)*(big_prime-1)
    d = pow(exponent,-1,phi)

    return pow(ciphertext,d,n)


def IntSqrt(modulo):

    return int(math.sqrt(modulo))



def DecipherSmallDiff(ciphertext, modulo, exponent):
    sqr_modulo = IntSqrt(modulo)
    for j in range(sqr_modulo-5000,sqr_modulo):
        if modulo%j==0:
            small_prime = j
            break
        
        
    big_prime = modulo // small_prime
    return Decrypt(ciphertext, small_prime, big_prime, exponent)


p = 1000000007
q = 1000000009
n = p * q
e = 239
ciphertext = Encrypt("attack", n, e)
message = DecipherSmallDiff(ciphertext, n, e)
print(ciphertext)
print(message)
