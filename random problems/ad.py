
def valid_move(x,y):
    if y<0 or x<0 or x>m-1 or y>n-1 or (x,y) in visited_squer:
        return False
    else:
        visited_squer.add((x,y))
        return True
        
        

def make_move(x,y):
    
    if valid_move(x+1,y):
        return(x+1,y,True)
    else:
        if valid_move(x-1,y):
            return(x-1,y,True)
        else:
            if valid_move(x,y+1):
                return(x,y+1,True)
            else:
                if valid_move(x,y-1):
                    return(x,y-1,True)
                else:
                    return(None,None,False)
                
def all_squer():
    return len(visited_squer)==m*n
        
        
T  = input()
visited_squer = set()
for tc in range(int(T)):
    n,m = map(int,input().split(" "))
    start_x,start_y = 0,0
    for i in range((m*n)-1):
        new_x,new_y,flag = make_move(start_x,start_y)
        if flag:
            start_x,start_y = new_x,new_y
        else:
            print("NO")
    
    if all_squer():
        print(YES)
        
        
    
              
