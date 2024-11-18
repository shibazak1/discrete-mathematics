alpha = 'abcdefghijklmnopqrstuvwxyz'
#key = 'jsuyfhkpicomxrqatlbvznewgd'
def substitute(text,substitute_what ,substitute_by):

    result = ""
    for litter in text:
        if litter in substitute_what:
            result += substitute_by[substitute_what.index(litter)]
        else:
            result += litter

    return result


def encode(plaintext):
    return substitute(plaintext,alpha,key)

def decode(ciphertext):
    return substitute(ciphertext,key,alpha)

#----------------------------------------------------
'''
ciphertext = 'kyv wzmv sfozex nzqriuj aldg hlztbcp'                             
for i in range(26):                                                             
    key  = alpha[i:] + alpha[:i]
    print(decode(ciphertext))
'''
#------------------------------------------------------

cipher_text  = "livitcswpiyvewhevsriqmxleyveoiewhrxexipfemvewhkvstylxzixlikiixpijvszeyperrgerimwqlmglmxqeriwgpsrihmxqerekietxmjtprgevekeitrewhexxlexxmzitwawsqwxswextvepmrxrsjgstvrieyviexcvmuimwergmiwxmjmgcsmwxsjomiqxliviqivixqsvstwhkpegarcsxrwievswiibxvizmxfsjxlikegaewhepswyswiwievxlisxlivxlirgepirqiviibgiihmwypflevhewhypsrrfqmxleppxlieccievewgisjktvwmrlihysphxliqimylxsjxlimwrigxqeroivfvizevaekpiewhxeamwyeppxlmwyrmwxsgswrmhivexmswmgstphlevhpfkpezintcmxivjsvlmrscmwmswvircigxmwymx"


freq = {}

for litter in cipher_text:
    if litter not in freq:
        freq[litter] =1
    else:
        freq[litter] +=1

highest_frequency_letter = max(freq, key=freq.get)

for i in "etaosi":
    mapp = alpha.index(highest_frequency_letter) - alpha.index(i)
    key = alpha[mapp:] + alpha[:mapp]
    
    print(decode(cipher_text))
    print()
    
    

    
                                                                                
                              
