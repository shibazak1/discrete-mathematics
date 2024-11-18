import math

def from_txt_to_number(text):
    result = 0
    for char in text:
        result =  result *100 +ord(char)
    return result

def from_number_to_txt(number):
    number_string  = str(number)
    chars = [number_string[:3]for chunck in range(0,len(number_string),3)]

    text  = ''.join(chr(int(char)) for char in chars)

    return text
    
    

    
def is_prime(x):
    for k in range(2,int(math.sqrt(x))):
        if math.sqrt(x)%k == 0:
            return False
    return True

def find_small_prime_factor():
    for j in range(2,10**6):
        if is_prime(j):
            if modulo % j==0:
                print(j)
                return j
    return "not found"


def Encrypt(m,modulo,exponent):
    return pow(from_txt_to_number(m),exponent,modulo)
    
def Decrypt(cipher_text,small_prime,big_prime,exponent):
    phi = (small_prime-1)*(big_prime-1)
    d = pow(exponent,-1,phi)

    return pow(cipher_text,d,modulo)



def DecipherSmallPrime(ciphertext, modulo, exponent):
        small_prime = find_small_prime_factor()
        big_prime = modulo // small_prime
        return Decrypt(ciphertext, small_prime, big_prime, exponent)
    


modulo = 101 * 18298970732541109011012304219376080251334480295537316123696052970419466495220522723330315111017831737980079504337868198011077274303193766040393009648852841770668239779097280026631944319501437547002412556176186750790476901358334138818777298389724049250700606462316428106882097210008142941838672676714188593227684360287806974345181893018133710957167334490627178666071809992955566020058374505477745993383434501768887090900283569055646901291270870833498474402084748161755197005050874785474707550376333429671113753137201128897550014524209754619355308207537703754006699795711188492048286436285518105948050401762394690148387
exponent = 239
ciphertext = Encrypt("attack", modulo, exponent)
print(ciphertext)
print(from_number_to_txt(DecipherSmallPrime(ciphertext, modulo, exponent)))
