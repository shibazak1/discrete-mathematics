import math

def from_txt_to_number(text):
    result = 0
    for char in text:
        result = result *100 +ord(char)
    return result



def Encrypt(message,modulo,exponent):
    return pow(from_txt_to_number(message),exponent,modulo)

def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
    # Fix this implementation
    for k in range(len(potential_messages)-1):
        
        if ciphertext == Encrypt(potential_messages[k], modulo, exponent):
            return potential_messages[k]
        return "don't know"


modulo = 101
exponent = 12
ciphertext = Encrypt("attack", modulo, exponent)
print(ciphertext)
print(DecipherSimple(ciphertext, modulo, exponent,
                      ["attack", "don't attack", "wait"]))
