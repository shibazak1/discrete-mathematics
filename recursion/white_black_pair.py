

def search_white_black(lst):

    print(f"searching for [0,1] in {lst}")
    if len(lst)==2:
        #print(lst)
        return lst
    elif lst[len(lst)//2]==1:
        return search_white_black(lst[:len(lst)//2+1])
    elif lst[len(lst)//2]==0:
        return search_white_black(lst[len(lst)//2:])

    
        
