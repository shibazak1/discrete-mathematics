# function take 2 permutation and return list of neighbor transpostions required

def transform(first ,second):

    transpositions = []
    x,y = 1,2
    for k in range(len(first)):
        targ_position = second.index(first[k])
        while first.index(first[k])!=targ_position:
            first[k] ,first[k+1] = first[k+1],first[k]
            
            transpositions.append((k,k+1))
            k+=1

    for j in reversed(range(len(first)-1)):
        targ_position2 = second.index(first[j])
        while first.index(first[j])!=targ_position2:
            first[j], first[j-1] = first[j-1],first[j]
            
            transpositions.append((j,j-1))
            j-=1
            
            
        
    print(transpositions)

    print(first)

#transform([1,2,3,4,5],[1,5,3,4,2])
#--------------------------------------------------------------------------------------------------------------

def convert(transposition):
# take transpoaition and converted to list neighbor transposition
    k,j = transposition
    neighbor_trans = []
    for i in range(k,j):
        neighbor_trans.append((i,i+1))
    for i in reversed(range(k,j-1)):
        # {j-1} to not touch the last item and returned bach 
        neighbor_trans.append((i,i+1))


    print(neighbor_trans)
    
convert((2,5))        
       

#--------------------------------------------------------------------------------------------------------------
# another way of writing convert function

def convert2(trans_positions):

    k,j = trans_positions

    return [(i,i+1) for i in range(k,j)]+
           [(i,i+1) for i in reversed(range(k,j-1))]




           
    





