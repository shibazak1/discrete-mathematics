
def apply(word,prem):

    first,second  = prem

    word[first] , word[second] = word[second] , word[first]



word  = ['S', 'T', 'O', 'P']

transpositions = [(0,0),(0, 1), (1, 2), (2, 3)]

for transposition in transpositions:
    apply(word ,transposition)
    print(word)

print(word)

