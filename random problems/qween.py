"""from itertools import permutations as p

for permutation in p(range(4)):
    print(permutation)
"""

from itertools import combinations, permutations
def is_solution(perm):
    pairs = combinations(range(len(perm)),2)
    return all(abs(i1-i2)!=abs(perm[i1]-perm[i2]) for i1,i2 in pairs)



def is_solution2(perm):

    pairs = combinations(range(len(perm)),2)
    for i1,i2 in pairs:

        
        return abs(i1-i2)!=abs(perm[i1]-perm[i2])
    


solution = filter(is_solution,permutations(range(8)))

print(next(solution))




    
