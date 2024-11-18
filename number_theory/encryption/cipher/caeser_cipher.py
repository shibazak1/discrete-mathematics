import  substitue_cipher

alpha = 'abcdefghijklmnopqrstuvwxyz'


ciphertext = 'kyv wzmv sfozex nzqriuj aldg hlztbcp'
for i in range(26):
    key  = alpha[i:] + alpha[:i]
    print(decode(ciphertext))

