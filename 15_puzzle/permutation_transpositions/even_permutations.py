# take list of n object and return true if and only if the permutation is even (require an even number of transpositions )


def is_even(perm):

    for k in range(len(perm)):

        count  = 0 
        if perm[k] !=k:
            target = perm.index(k)
            perm[k],perm[target] = perm[target],perm[k]
            count +=1 
            print(perm)

            
    if count%2 ==0:
        return True
    else:
        return False

    

print(is_even([4,0,1,3,2]))

