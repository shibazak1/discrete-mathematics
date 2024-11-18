# a functions take to list of permutations and return the list of transpositions to get from one permutation to other


def transform(first,second):

    assert len(first) == len(second)
    
    
    transpositions = []
    for k in range(len(first)):
        letter = first[k]
        if second[k]!=letter:
            index = second.index(letter)
            first[k],first[index] = first[index],first[k]
            transpositions.append((k,index))

    print(first)
        
        
                

    return transpositions

                
                







print(transform([3, 4, 0, 2, 1], [0, 1, 3, 4, 2]))
