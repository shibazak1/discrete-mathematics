

def to_hex(plaintext):
    hex_codes = []
    for symbol in plaintext:
        hex_code = hex(ord(symbol)).replace('0x','')
        if hex_code == 1:
            hex_code = '0' + hex_code
        hex_codes.append(hex_code)
    return ''.join(hex_codes)


def to_str(hex_codes):
    if hex_codes:
        return chr(int(hex_codes[:2],base=16))+to_str(hex_codes[2:])
    return ''

def bitwise_xor(first_text,second_text):
    assert len(first_text)==len(second_text)

    return ''.join(format(int(s1,16)^int(s2,16),'01x')
                   for s1,s2 in zip(first_text,second_text))


m = "hellow"
k = "myfood"

cipher_text  = bitwise_xor(to_hex(m),to_hex(k))
plaintext = to_str(bitwise_xor(cipher_text,to_hex(k)))

print(cipher_text)
print(plaintext)
