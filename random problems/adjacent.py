b = [1,0,1,0]
a = []

def find_valid_pair(N,target):
    for i in range(1,N):
        for j in range(i+1,N):
            if (i+j)%2 == target:
                return i,j



x,y = find_valid_pair(4,0)
print(x,y)
            
        
            
        
