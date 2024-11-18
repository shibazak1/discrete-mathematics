

def transform_by_3_cycles(first,second):
    

    assert len(first)==len(second)
    n = len(first)
    
    current  = list(first)
    cycles=[]
    
    for i in range(n-2):
        if current[i]!=second[i]:
            idx  = current.index(second[i])
            spare = i+1 if idx!=i+1 else i+2
            cycles.append((idx,i,spare))
            current[i],current[idx],current[spare]= current[idx],current[spare],current[i]

            assert current[i]==second[i]


    return cycles









print(transform_by_3_cycles(
[3, 4, 0, 2, 1, 5],
[0, 5, 1, 4, 3, 2]
))


            





